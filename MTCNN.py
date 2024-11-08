import cv2
from mtcnn.mtcnn import MTCNN
import matplotlib.pyplot as plt

# Inicializa o detector MTCNN
detector = MTCNN()

# Carrega uma imagem usando OpenCV
image = cv2.imread('Resources/poucaLuzLowQ.png')

# Converte a imagem de BGR (formato padrão do OpenCV) para RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Realiza a detecção facial
resultados = detector.detect_faces(image_rgb)

# Função para desenhar as bounding boxes e os pontos faciais
def desenhar_bounding_box(image, resultados):
    for res in resultados:
        # Pega as coordenadas da bounding box
        x, y, largura, altura = res['box']
        
        # Desenha a bounding box
        cv2.rectangle(image, (x, y), (x+largura, y+altura), (0, 255, 0), 2)
        
        # Desenha os pontos faciais (landmarks)
        for key, point in res['keypoints'].items():
            cv2.circle(image, point, 2, (0, 0, 255), -1)

    return image

# Desenha as boxes e os landmarks na imagem
image_com_deteccao = desenhar_bounding_box(image_rgb, resultados)

# Exibe a imagem com as detecções
plt.imshow(image_com_deteccao)
plt.axis('off')
plt.show()
