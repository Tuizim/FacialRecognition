import logging
import cv2
import numpy as np
from insightface.app import FaceAnalysis
import Resources.Message_Ressources as sysMsg

def get_face_embedding(image_path):
    try:
        app= FaceAnalysis(name='buffalo_l')
        app.prepare(ctx_id=0)
        image = cv2.imread(image_path)
        faces = app.get(image)
        return faces[0].embedding.tolist()
    except:
        logging.critical(sysMsg.Messages.Errors.GENERIC_ERROR)

    