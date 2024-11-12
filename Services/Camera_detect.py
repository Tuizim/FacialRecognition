import os
import cv2
import Resources.Message_ressources as msgSys
from Detectors.Haar_Cascade import Haar
import Commum.Directorys_Controll as DC
import Commum.globalVars as globalVars

class Camera_detect:
    def __init__(self):
        self.image_captured = False
        self.tryDetect = 0
        self.running = True
        self.video = cv2.VideoCapture(0)
        if not self.video.isOpened():
            print(msgSys.Messages.Errors.CameraError.NOT_OPPENED)
            exit()
        self.camera_fps = self.video.get(cv2.CAP_PROP_FPS)
    
    def start(self):
        while self.running == True:
            ret, frame = self.video.read()
            frame = cv2.flip(frame,1)
            if not ret:
                print(msgSys.Messages.Errors.CameraError.CAPTURE_FAIL)
                break
            haar_detector = Haar()
            anyFace = haar_detector.detect_face(frame)
            self.draw_retangle(anyFace,frame) 
            cv2.imshow('Detect',frame)
            if self.image_captured == False:
                self.capture_image(frame,anyFace)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        self.running=False
        self.video.release()
        cv2.destroyAllWindows()
        
    def draw_retangle(self,anyFaces,frame):
        COLOR_SUCCESS= (0, 255, 0)
        COLOR_FAIL= (0, 0, 255)
        COLOR_NONE= (10, 10, 10)
        
        height, width, _ = frame.shape
        start_point = (10, 10)
        end_point = (width - 10, height - 10)
        
        if anyFaces ==True:
            rectangle_color = COLOR_SUCCESS
        elif anyFaces == False:
            rectangle_color = COLOR_FAIL
        else:
            rectangle_color = COLOR_NONE
        cv2.rectangle(frame,start_point,end_point,rectangle_color,2)

    def capture_image(self, frame, qntFaces):
        try:
            if self.tryDetect < self.camera_fps and qntFaces == 1:
                self.tryDetect += 1
            elif qntFaces != 1:
                self.tryDetect = 0
            else:
                if not os.path.exists("./captured_images"):
                    os.makedirs("./captured_images")
                path = DC.get_master_dir() + '\\captured_images'
                imageName = '\\captured.jpg'
                DC.clear_directory(path)
                cv2.imwrite(path + imageName, frame)
                self.image_captured = True
                globalVars.global_image_save_path = path + imageName
        except Exception as e:
            print(msgSys.Messages.Errors.GENERIC_ERROR + ':' + str(e))
                