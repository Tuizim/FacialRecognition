import cv2
from mtcnn.mtcnn import MTCNN
import matplotlib.pyplot as plt


detector = MTCNN()

def face_detect(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return detector.detect_faces(image_rgb)

def draw_bounding_box(image, resultados):
    for res in resultados:
        # Pega as coordenadas da bounding box
        x, y, largura, altura = res['box']
        
        # Desenha a bounding box
        cv2.rectangle(image, (x, y), (x+largura, y+altura), (0, 255, 0), 2)
        
        # Desenha os pontos faciais (landmarks)
        for key, point in res['keypoints'].items():
            cv2.circle(image, point, 2, (0, 0, 255), -1)

    return image