#login page
import customtkinter
from interface import home
from interface import interface_template

class Login(interface_template):
    

    #login interface
    #def interface_exe(self):
    #def in_exe(self):
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
        email_entry = customtkinter.CTkEntry(self.frame, placeholder_text="Email")
        email_entry.pack(pady=20, padx=0)

        password_entry = customtkinter.CTkEntry(self.frame, placeholder_text= "Password", show="*")
        password_entry.pack(pady=20, padx=0)

        button = customtkinter.CTkButton(self.frame, text="Login", command=self.db_login)
        button.pack(pady=40, padx=20)

        button_return = customtkinter.CTkButton(self.frame, text='return', command=self.home_return)
        button_return.pack(pady=0,padx=20)

    def home_return(self):
        obj_home =  home.Home(self.frame)
        obj_home.interface_exe()

    def db_login():
        #connect with the database to check if the user and password exist
        
        pass