import cv2
import time
import Detectors.DeepFace_MTCNN as PDMTcnn
import Commum.Directorys_Controll as DC
import Commum.Global_Vars as Global_Vars
import Resources.Message_Ressources as sysMsg
import Commum.Json_Controll as jsonC
from Classes.Credential import Credential

class Face_Reader:
    def read_image(self,user:Credential):
        while True:
            if Global_Vars.global_image_save_path != None:
                try:
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
    def face_compare(self,user):
        Jsondir=DC.get_master_dir()+"\\Data\\"+Global_Vars.JSON_EMBEDDING
        teste = jsonC.Read_Json(Jsondir)
        return teste