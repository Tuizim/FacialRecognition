import os
import cv2
import Resources.Message_ressources as msgSys
from Detectors.Haar_Cascade import Haar
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
            
        pass
    
    def start(self):
        while self.running == True:
            ret, frame = self.video.read()
            frame = cv2.flip(frame,1)
            if not ret:
                print(msgSys.Messages.Errors.CameraError.CAPTURE_FAIL)
                break
            haar_detector = Haar()
            qntFaces = haar_detector.detect_face(frame)
            self.draw_retangle(qntFaces,frame) 
            cv2.imshow('Detect',frame)
            if self.image_captured == False:
                self.capture_image(frame,qntFaces)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        self.running=False
        self.video.release()
        cv2.destroyAllWindows()
        
    def draw_retangle(self,qntFaces,frame):
        COLOR_SUCCESS= (0, 255, 0)
        COLOR_FAIL= (0, 0, 255)
        height, width, _ = frame.shape
        start_point = (10, 10)
        end_point = (width - 10, height - 10)
        
        if qntFaces ==True:
            rectangle_color = COLOR_SUCCESS
        else:
            rectangle_color = COLOR_FAIL
        cv2.rectangle(frame,start_point,end_point,rectangle_color,2)

    def capture_image(self, frame, qntFaces):
        if self.tryDetect < self.camera_fps and qntFaces==1:
            self.tryDetect+=1
        elif qntFaces!=1:
            self.tryDetect =0
        else:
            if not os.path.exists("captured_images"):
                os.makedirs("captured_images")
            image_path = "captured_images/captured_image.jpg"
            cv2.imwrite(image_path, frame)
            print(f"Imagem capturada e salva em {image_path}")
            self.image_captured=True