import os
import cv2
import time
import Detectors.FaceAnalysis as PDMTcnn
import Commum.Directorys_Controll as DC
import Commum.Global_Vars as Global_Vars
import Resources.Message_Ressources as sysMsg
import Commum.Json_Controll as jsonC
from Classes.Credential import Credential
import numpy as np
from scipy.spatial.distance import cosine, euclidean

def construct_user(user:Credential=None):
    if user == None:
        user = Credential(name=None,cpf=None,status=None,face=None)
    embedding= read_image()
    user.face = embedding
    return user

def read_image():
    while True:
        if Global_Vars.global_image_save_path != None:
            try:
                embedding= PDMTcnn.get_face_embedding(Global_Vars.global_image_save_path)
                os.remove(Global_Vars.global_image_save_path)
                Global_Vars.global_image_save_path=None
                return embedding
            except Exception as ex:
                print(sysMsg.Messages.Errors.ImageError.NOT_ACCESS + ':' + str(ex))     
                return None
        time.sleep(0.1)

def write_embedding(user):
    try:
        Jsondir=DC.get_master_dir()+"\\Data\\"+Global_Vars.JSON_EMBEDDING
        jsonC.Write_Json(dir=Jsondir,data=user.__dict__)
        return True
    except:
        return False

def user_finder_by_face(embedding):
    jsonDir=DC.get_master_dir()+"\\Data\\"+Global_Vars.JSON_EMBEDDING
    jsonLines = jsonC.Read_Json(jsonDir)
    if jsonLines is None or len(jsonLines) == 0:
        return None
    credentials=[]
    for line in jsonLines:
        credential = Credential(
            name=line["name"],
            cpf=line["cpf"],
            status=line["status"],
            face=line["face"],
        )
        credentials.append(credential)
    if len(credentials)>0:
        for credential in credentials:
            isCompatible = find_if_is_face(embedding,credential.face)
            if isCompatible:
                return credential

def find_if_is_face(embedding1,embedding2):
    cosine_distance = cosine(embedding1, embedding2)
    return cosine_distance < 0.6

def register_face(user:Credential):
    while True:
        if Global_Vars.global_image_save_path != None:
            try:
                user = construct_user(user)
                write_embedding(user)
                Global_Vars.global_image_save_path=None
                return True
            except Exception as ex:
                print(sysMsg.Messages.Errors.ImageError.NOT_ACCESS + ':' + str(ex))
                Global_Vars.global_image_save_path=None
                return False 
        time.sleep(0.1)

def execute_recognizer():
    embedding = read_image()
    user= user_finder_by_face(embedding=embedding)
    return user
        
        