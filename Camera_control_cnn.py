import cv2
import MTCNN
import Message_ressources
import threading
from Camera_Interface import CameraInterface

class CameraControlCNN(CameraInterface):
    def __init__(self):
        self.camera = cv2.VideoCapture(0)
        if not self.camera.isOpened():
            print(Message_ressources.Messages.Errors.CameraError.NOT_OPPENED)
            exit()
        
        self.frame_count = 0
        self.processed_frame = None
        self.lock = threading.Lock()
        self.running = True
    
    def capture_frames(self):
        try:
            while self.running:
                captured, frame = self.camera.read()
                
                if not captured:
                    print(Message_ressources.Messages.Errors.CameraError.CAPTURE_FAIL)
                    break
                
                frame = cv2.flip(frame, 1)
                frame = cv2.resize(frame, (640, 480))

                if self.frame_count % 5 == 0:
                    # Envia o frame para a thread de processamento
                    with self.lock:
                        self.processed_frame = frame.copy()
                
                self.frame_count += 1

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.running = False
                    break
        except Exception as e:
            print(f"Erro na captura de frames: {e}")

    def process_faces(self):
        try:
            while self.running:
                frame_to_process = None
                
                with self.lock:
                    if self.processed_frame is not None:
                        frame_to_process = self.processed_frame.copy()
                        self.processed_frame = None  # Limpa o frame para o próximo
                
                if frame_to_process is not None:
                    face = MTCNN.face_detect(frame_to_process)
                    faceBox = MTCNN.draw_bounding_box(frame_to_process, face)
                    
                    cv2.imshow("Camera", faceBox)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.running = False  # Para encerrar as threads
                    # Libera a câmera e fecha as janelas abertas
                    self.camera.release()
                    cv2.destroyAllWindows()
                    break
        except Exception as e:
            print(f"Erro no processamento de faces: {e}")

    def start(self):
        capture_thread = threading.Thread(target=self.capture_frames)
        process_thread = threading.Thread(target=self.process_faces)

        capture_thread.start()
        process_thread.start()

        capture_thread.join()
        process_thread.join()

