import cv2
import time
import Detectors.DeepFace_MTCNN as PDMTcnn
import Commum.Directorys_Controll as DC
import Commum.Global_Vars as Global_Vars
import Resources.Message_Ressources as sysMsg
import Commum.Json_Controll as jsonC
from Classes.Credential import Credential

class Face_Reader:
    def read_image(self,user:Credential=None):
        while True:
            if Global_Vars.global_image_save_path != None:
                try:
                    if user == None:
                        user = Credential(name=None,cpf=None,status=None,face=None)
                    embedding=PDMTcnn.get_face_embedding(Global_Vars.global_image_save_path)
                    user.face = embedding
                except Exception as ex:
                    print(sysMsg.Messages.Errors.ImageError.NOT_ACCESS + ':' + str(ex))      
                finally:
                    Global_Vars.global_image_save_path=None
                    return user
            time.sleep(0.1)
    def write_embedding(self,user):
        Jsondir=DC.get_master_dir()+"\\Data\\"+Global_Vars.JSON_EMBEDDING
        jsonC.Write_Json(dir=Jsondir,data=user.__dict__)
    def face_compare(self,user:Credential):
        jsondir=DC.get_master_dir()+"\\Data\\"+Global_Vars.JSON_EMBEDDING
        jsonlines = jsonC.Read_Json(jsondir)
        credentials=[]
        for line in jsonlines:
            credential = Credential(
                name=line["name"],
                cpf=line["cpf"],
                status=line["status"],
                face=line["face"],
            )
            credentials.append(credential)
        if len(credentials)>0:
            for credential in credentials:
                isCompatible = PDMTcnn.find_if_is_face(user.face,credential.face)
                if isCompatible:
                    return credential