import cv2
import time
from Detectors.MTCNN import Mtcnn
import Commum.Directorys_Controll as DC
import Commum.globalVars as globalVars
import Resources.Message_ressources as sysMsg

class Image_detector:
    def __init__(self):
        self.cnnDetector = Mtcnn()
    def read_image(self):
        while True:
            if globalVars.global_image_save_path != None:
                try:
                    image = cv2.imread(globalVars.global_image_save_path)
                    face = self.cnnDetector.face_detect(image)
                except Exception as ex:
                    print(sysMsg.Messages.Errors.ImageError.NOT_ACCESS +':'+ ex)         
                finally:
                    globalVars.global_image_save_path=None
            time.sleep(0.1)                