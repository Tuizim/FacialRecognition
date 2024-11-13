import cv2
import time
import threading
import os
from Detectors.MTCNN import Mtcnn
import Commum.Directorys_Controll as DC
from Services.Camera_detect import Camera_detect
from Services.Face_Reader import Face_Reader
import Commum.terminal_Controll as TC
import Resources.Message_Ressources as sysMsg
from Classes.Credential import Credential


def start_camera():
    camera.start()

def start_image_detection_register(user: Credential):
    user = image_detector.read_image(user)
    image_detector.write_embedding(user=user)
    camera.running=False

def start_image_detection_finder():
    user = image_detector.read_image()
    image_detector.face_compare(user)

def Create_User(user: Credential):
    thread1 = threading.Thread(target=start_camera)
    thread1.daemon = True
    thread1.start()

    thread2 = threading.Thread(target=start_image_detection_register, args=(user,))
    thread2.daemon = True
    thread2.start()
    try:
        while camera.running:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Encerrando o programa.")

def Verify_User():
    thread1 = threading.Thread(target=start_camera)
    thread1.daemon = True
    thread1.start()

    thread2 = threading.Thread(target=start_image_detection_finder)
    thread2.daemon = True
    thread2.start()
    
    try:
        while camera.running:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Encerrando o programa.")

while True:
    camera = Camera_detect()
    image_detector = Face_Reader()
    TC.clear_terminal()
    print(TC.TERMINAL_MESSAGE_MENU)
    menuSelected = int(input('R:'))
    TC.clear_terminal()
    try:
        if menuSelected==1:
            name = str(input(TC.TERMINAL_MESSAGE_REGISTER_NAME))
            cpf = str(input(TC.TERMINAL_MESSAGE_REGISTER_CPF))
            status = bool(input(TC.TERMINAL_MESSAGE_REGISTER_STATUS))
            user = Credential(name=name,cpf=cpf,status=status,face=None)
            Create_User(user)
        elif menuSelected == 2:
            Verify_User()
        elif menuSelected == 0:
            exit()
        else:
            print(sysMsg.Messages.Errors.TerminalError.INVALID_VALUE)
        
    except ValueError:
        print(sysMsg.Messages.Errors.TerminalError.INVALID_VALUE)


