import json
import Resources.Message_Ressources as sysMsg
import Commum.Directorys_Controll as DC
import logging
def Read_Json(dir):
    try:
        with open(dir,'r',encoding='utf-8') as file:
            files = []
            for line in file:
                files.append(json.loads(line.strip()))
            return files
    except FileNotFoundError:
        logging.critical(sysMsg.Messages.Errors.DirError.NOT_EXIST)
        return None
    except json.JSONDecodeError:
        logging.critical(sysMsg.Messages.Errors.JsonError.DECODE_ERROR)
        return None
def Write_Json(dir,data):
    try:
        with open(dir,'a',encoding='utf-8') as file:
            file.write(json.dumps(data,ensure_ascii=False) + "\n")
    except Exception as e:
        logging.critical(sysMsg.Messages.Errors.GENERIC_ERROR)