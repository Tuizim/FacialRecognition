from deepface import DeepFace
import numpy as np

def get_face_embedding(image_path):
    embedding = DeepFace.represent(img_path=image_path, model_name="Facenet", detector_backend="mtcnn")
    return embedding[0]["embedding"] if embedding else None

def find_if_is_face(embedding1,embedding2):
    euclidean_distance= np.linalg.norm(np.array(embedding1) - np.array(embedding2))
    return euclidean_distance < 0.6
    