import cv2
import CNN_FACE_DETECT
import MESSAGES_RESOURCES
import threading

camera = cv2.VideoCapture(0)
frame_count = 0
processed_frame = None
lock = threading.Lock()  # Para sincronizar acesso ao frame processado

def capture_frames():
    global frame_count, processed_frame
    while True:
        captured, frame = camera.read()
        
        if not captured:
            print(MESSAGES_RESOURCES.Messages.Errors.CameraError.CAPTURE_FAIL)
            break
        
        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (640, 480))

        if frame_count % 5 == 0:
            # Envia o frame para a thread de processamento
            with lock:
                processed_frame = frame.copy()
        
        frame_count += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def process_faces():
    global processed_frame
    while True:
        # Aguarda por um frame para processar
        if processed_frame is not None:
            with lock:
                frame_to_process = processed_frame.copy()
                processed_frame = None  # Limpa o frame para o próximo
            
            face = CNN_FACE_DETECT.face_detect(frame_to_process)
            faceBox = CNN_FACE_DETECT.draw_bounding_box(frame_to_process, face)
            
            cv2.imshow("Camera", faceBox)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if not camera.isOpened():
    print(MESSAGES_RESOURCES.Messages.Errors.CameraError.NOT_OPPENED)
    exit()

# Inicia as threads de captura e processamento
capture_thread = threading.Thread(target=capture_frames)
process_thread = threading.Thread(target=process_faces)

capture_thread.start()
process_thread.start()

# Aguarda as threads terminarem
capture_thread.join()
process_thread.join()

# Libera a câmera e fecha as janelas abertas
camera.release()
cv2.destroyAllWindows()
