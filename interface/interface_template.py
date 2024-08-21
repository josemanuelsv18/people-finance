import customtkinter
from interface import home
from abc import ABC, abstractmethod

class InterfaceTemplate(ABC):
    def __init__(self, frame):
        self.root = customtkinter.CTk()
        self.frame = frame

    #template interdace
    @abstractmethod
    def interface_exe(self):
        pass
    
    def home_return(self):
        obj_home = home.Home(self.frame)
        obj_home.interface_exe()

    