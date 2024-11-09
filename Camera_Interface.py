from abc import ABC, abstractmethod

class CameraInterface(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def capture_frames(self):
        pass

    @abstractmethod
    def process_faces(self):
        pass

    @abstractmethod
    def start(self):
        pass