class Messages:
    class Errors:
        GENERIC_ERROR= "Error"
        class CameraError:
            NOT_OPPENED = "Erro ao abrir a camera"
            CAPTURE_FAIL ="Falha na captura"
        class ImageError:
            NOT_ACCESS= "Erro ao acessar imagem."
        class DirError:
            CANT_DELETE= "Falha ao deletar."
            NOT_EXIST= "O diretório especificado não existe ou não é um diretório válido."
        class JsonError:
            DECODE_ERROR= "Erro ao decodificar o arquivo JSON."
        class TerminalError:
            INVALID_VALUE= "Valor invalido"
    class Success:
        GENERIC_SUCCESS= "Sucesso!"
    class Warming:
        GENERIC_WARMING= "Atenção!"
        class CaptureWarming:
            MULT_FACE_DETECTED= "Mais de um rosto detectado"    
