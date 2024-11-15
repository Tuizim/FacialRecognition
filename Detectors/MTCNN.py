import cv2
from mtcnn.mtcnn import MTCNN
import time
import logging
import Commum.Directorys_Controll as DC
import Commum.Global_Vars as globalVars

class mtcnnDetector():
    def __init__(self):
        self.detector = MTCNN()
        self.running = True
        self.last_keypoints = None
        self.start_time = None

    def is_face_frontal(self, keypoints, tolerance=0.05):
        left_eye = keypoints['left_eye']
        right_eye = keypoints['right_eye']
        nose = keypoints['nose']
        eye_center_x = (left_eye[0] + right_eye[0]) / 2
        symmetry_horizontal = abs(nose[0] - eye_center_x) / eye_center_x
        symmetry_vertical = abs(left_eye[1] - right_eye[1]) / max(left_eye[1], right_eye[1])
        return symmetry_horizontal < tolerance and symmetry_vertical < tolerance

    def is_face_stationary(self, keypoints, max_movement=100):
        if self.last_keypoints is None:
            self.last_keypoints = keypoints
            return True
        total_movement = 0
        for point in keypoints:
            movement = abs(keypoints[point][0] - self.last_keypoints[point][0]) + \
                       abs(keypoints[point][1] - self.last_keypoints[point][1])
            total_movement += movement
        self.last_keypoints = keypoints
        return total_movement < max_movement

    def start(self):
        video = cv2.VideoCapture(0)
        if not video.isOpened():
            logging.error("Erro ao abrir a câmera!")
        while self.running:
            ret, frame = video.read()
            if not ret:
                break
            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            detections = self.detector.detect_faces(rgb_frame)

            for detection in detections:
                if detection['confidence'] < 0.9:
                    continue

                keypoints = detection['keypoints']

                COLOR_NONE=(0,0,255)
                COLOR_WAIT=(255,0,0)
                color_box=COLOR_WAIT
                
                if self.is_face_frontal(keypoints) and self.is_face_stationary(keypoints):
                    if self.start_time is None:
                        self.start_time = time.time()

                    elapsed_time = time.time() - self.start_time
                    color_box=COLOR_WAIT
                    if elapsed_time >= 2:
                        path = DC.get_master_dir() + "\\captured_images\\captured_face.jpg"
                        globalVars.global_image_save_path=path
                        cv2.imwrite(path, frame)
                        logging.info("Imagem capturada!")
                        video.release()
                        cv2.destroyAllWindows()
                else:
                    self.start_time = None
                    color_box=COLOR_NONE

                x, y, w, h = detection['box']
                cv2.rectangle(frame, (x, y), (x + w, y + h), color_box, 2)

            cv2.imshow("Real-Time Face Detection", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        video.release()
        cv2.destroyAllWindows()
