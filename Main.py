import time
import threading
import Services.Face_Reader as faceReader
import Commum.terminal_Controll as TC
import Resources.Message_Ressources as sysMsg
from Classes.Credential import Credential
from Detectors.MTCNN import mtcnnDetector



def start_camera():
    mtcnn.start()

def start_image_detection_register(user: Credential):
    register = faceReader.register_face(user)
    if register:
        mtcnn.running=False

def start_image_detection_finder():
    user:Credential=faceReader.execute_recognizer()
    TC.clear_terminal()
    if user !=None:
        print("Bem vindo ",user.name)
    else:
        print(sysMsg.Messages.Warming.NOT_MATCHED)
    input(TC.TERMINAL_MESSAGE_TRY_AGAIN + TC.TERMINAL_MESSAGE_WRITE_SOMETHING)
    mtcnn.running=False

def Create_user(user: Credential):
    thread1 = threading.Thread(target=start_camera)
    thread1.daemon = True
    thread1.start()

    thread2 = threading.Thread(target=start_image_detection_register, args=(user,))
    thread2.daemon = True
    thread2.start()
    try:
        while mtcnn.running:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Encerrando o programa.")

def Verify_user():
    thread1 = threading.Thread(target=start_camera)
    thread1.daemon = True
    thread1.start()

    thread2 = threading.Thread(target=start_image_detection_finder)
    thread2.daemon = True
    thread2.start()
    
    try:
        while mtcnn.running:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Encerrando o programa.")

def execute():
    while True:
        try:
            mtcnn.reset_atributtes()
            TC.clear_terminal()
            print(TC.TERMINAL_MESSAGE_MENU)
            menuSelected = int(input('R:'))
            TC.clear_terminal()
            if menuSelected==1:
                name = str(input(TC.TERMINAL_MESSAGE_REGISTER_NAME))
                cpf = str(input(TC.TERMINAL_MESSAGE_REGISTER_CPF))
                status = bool(TC.status_user())
                user = Credential(name=name,cpf=cpf,status=status,face=None)
                Create_user(user)
            elif menuSelected == 2:
                Verify_user()
            elif menuSelected == 0:
                exit()
            else:
                print(sysMsg.Messages.Errors.TerminalError.INVALID_VALUE)
            
        except ValueError:
            print(sysMsg.Messages.Errors.TerminalError.INVALID_VALUE)
            input(TC.TERMINAL_MESSAGE_WRITE_SOMETHING)
if __name__ == "__main__":
    mtcnn = mtcnnDetector()
    execute()