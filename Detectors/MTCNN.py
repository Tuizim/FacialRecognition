import cv2
from mtcnn.mtcnn import MTCNN
import matplotlib.pyplot as plt
import numpy as np

class Mtcnn():
    def __init__(self):
        self.detector = MTCNN()

    def face_detect(self,image):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return self.detector.detect_faces(image_rgb)


        for face in faces:
            # Pega as coordenadas da bounding box
            x, y, largura, altura = face['box']
            
            # Desenha a bounding box
            cv2.rectangle(image, (x, y), (x+largura, y+altura), (0, 255, 0), 2)
            
            # Desenha os pontos faciais (landmarks)
            for key, point in face['keypoints'].items():
                cv2.circle(image, point, 2, (0, 0, 255), -1)

        return image
    
