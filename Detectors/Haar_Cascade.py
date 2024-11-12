import cv2
import Resources.Message_ressources as msgSys
class Haar:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def detect_face(self,frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=40, minSize=(30, 30))
        if len(faces) == 1:
            return True
        elif len(faces)>1:
            return False
        else:
            return None