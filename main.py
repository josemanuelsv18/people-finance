#finance management software with api and database connection
import customtkinter
from interface import home
import os

class Main:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    #main execution
    def main(self):
        self.frame_interface()

    def frame_interface(self):
        #theme
        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("green")
        #screen size
        self.root.geometry("450x550")
        #blank frame
        frame = customtkinter.CTkFrame(master=self.root)
        frame.pack(pady=20, padx=60,fill="both", expand=True)
        obj_home = home.Home(frame)
        obj_home.interface_exe()
        self.root.mainloop()
    #method to close correctly the interface
    def on_closing(self):
        self.root.destroy()
        os._exit(0)
#main call
if __name__ == '__main__':
    app= Main()
    app.main()