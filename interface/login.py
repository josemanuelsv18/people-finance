#login page
import customtkinter
from interface import interface_template
from backend import login_db
from interface import app_home

class Login(interface_template.InterfaceTemplate):
    def __init__(self, frame):
        super().__init__(frame)
        self.email=None
        self.password=None
    #login interface
    def interface_exe(self):
        #clean frame
        for widget in self.frame.winfo_children():
            widget.destroy()
        #theme
        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("green")
        #screen size
        self.root.geometry("500x400")
        #Inner frame
        self.frame.pack(pady=20, padx=60,fill="both", expand=True)
        #title
        label = customtkinter.CTkLabel(master=self.frame,text="Login\nInsert your user", font=("roboto", 24))
        label.pack(pady=12, padx=10)
        #login input and button
        self.email = customtkinter.CTkEntry(self.frame, placeholder_text="Email")
        self.email.pack(pady=20, padx=0)

        self.password = customtkinter.CTkEntry(self.frame, placeholder_text= "Password", show="*")
        self.password.pack(pady=20, padx=0)

        button = customtkinter.CTkButton(self.frame, text="Login", command=self.db_login)
        button.pack(pady=40, padx=20)

        button_return = customtkinter.CTkButton(self.frame, text='Return', command=self.home_return)
        button_return.pack(pady=0,padx=20)

    def db_login(self):
        #connect with the database to check if the user and password exist
        obj_login = login_db.LoginDB(name=None, surname=None, email=self.email.get(), password=self.password.get())
        if obj_login.user_login():
            obj_home = app_home.AppHome(obj_login.get_user_id())