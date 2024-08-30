#register new user page
import customtkinter
from interface import interface_template
from backend import register_user
from tkinter import messagebox
from interface import app_home

class Register(interface_template.InterfaceTemplate):
    def __init__(self, frame):
        super().__init__(frame)
        self.name=''
        self.surname=''
        self.email=''
        self.password=''
    #Register Interface
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
        #Title
        label = customtkinter.CTkLabel(master=self.frame,text="Register\nCreate your user", font=("roboto", 24))
        label.pack(pady=12, padx=10)
        #Inputs
        self.name = customtkinter.CTkEntry(self.frame, placeholder_text='Name')
        self.name.pack(pady=20, padx=0)

        self.surname = customtkinter.CTkEntry(self.frame, placeholder_text='Surname')
        self.surname.pack(pady=20, padx=0)

        self.email = customtkinter.CTkEntry(self.frame, placeholder_text='Email')
        self.email.pack(pady=20, padx=0)

        self.password = customtkinter.CTkEntry(self.frame, placeholder_text='Password', show='*')
        self.password.pack(pady=20, padx=0)
        #buttons
        self.button = customtkinter.CTkButton(self.frame, text='Register', command=self.db_register)
        self.button.pack(pady=40, padx=40)

        self.button_return = customtkinter.CTkButton(self.frame, text='Return', command=self.home_return)
        self.button_return.pack(pady= 0, padx=20)

    
    def db_register(self):
        obj_user_register = register_user.RegisterUser(self.name.get(), self.surname.get(), self.email.get(), self.password.get())
        if obj_user_register.create_new_user():
            messagebox.showinfo("People Finance","Your user has been created succesfully")
            #From here user has to go to app homepage
            obj_home_page = app_home.AppHome(self.frame, obj_user_register.get_id_new_user())
            obj_home_page.interface_exe()
        else:
            messagebox.showinfo("People Finance","Your user could not be created")