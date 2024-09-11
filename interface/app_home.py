from interface import interface_template
import customtkinter
from backend import user_db

class AppHome(interface_template.InterfaceTemplate):
    def __init__(self, frame, id_user):
        super().__init__(frame)
        self.id_user = id_user
        self.obj_user_db =  user_db.UserDB(self.id_user)
        self.obj_user = self.obj_user_db.fetch_user_data()

    #Main page interface
    def interface_exe(self):
        #clean frame
        for widget in self.frame.winfo_children():
            widget.destroy()
        #theme
        customtkinter.set_appearance_mode('system')
        customtkinter.set_default_color_theme('green')
        #Screen size
        self.root.geometry('1000x600')
        #Inner frame
        self.frame.pack(pady=20, padx=60, fill='both', expand=True)
        #Clean frame
        for widget in self.frame.winfo_children():
            widget.destroy()
        #inner frame
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)
        #title
        label = customtkinter.CTkLabel(master=self.frame, text="People Finance", font=("Roboto", 24))
        label.pack(pady=12, padx=10)
        label_welcome = customtkinter.CTkLabel(master=self.frame, text=f"Welcome {self.obj_user.get_name()}", font=("Roboto",24))
        label_welcome.pack(pady=12, padx=10)
        #return button
        button_return = customtkinter.CTkButton(self.frame, text='Return', command=self.home_return)
        button_return.pack(pady=0,padx=20)