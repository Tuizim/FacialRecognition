import cv2
import time
import threading
import os
from Detectors.MTCNN import Mtcnn
import Commum.Directorys_Controll as DC
from Services.Camera_detect import Camera_detect
from Services.Image_detect import Image_detector

camera = Camera_detect()
image_detector = Image_detector()

def start_camera():
    camera.start()

def start_image_detection():
    image_detector.read_image()

thread1 = threading.Thread(target=start_camera)
thread1.daemon = True
thread1.start()

thread2 = threading.Thread(target=start_image_detection)
thread2.daemon = True
thread2.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Encerrando o programa.")
    camera.running = False