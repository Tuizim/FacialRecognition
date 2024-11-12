import os
import shutil
import Resources.Message_ressources as sysMsg

def clear_directory(directory_path):
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(sysMsg.Messages.Errors.DirError.CANT_DELETE + ':' + str(e))
    else:
        print(sysMsg.Messages.Errors.DirError.NOT_EXIST)
        
def get_master_dir():
    return os.path.dirname(os.path.dirname(__file__))
    
    