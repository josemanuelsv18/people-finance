import customtkinter
from interface import login
from interface import interface_template
from interface import register

class Home(interface_template.InterfaceTemplate):
    def __init__(self, frame):
        super().__init__(frame)

    #login interface
    def interface_exe(self):
        #clean frame
        for widget in self.frame.winfo_children():
            widget.destroy()
        #inner frame
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)
        #title
        label = customtkinter.CTkLabel(master=self.frame, text="People Finance", font=("Roboto", 24))
        label.pack(pady=12, padx=10)
        #login and register buttons
        log_button = customtkinter.CTkButton(master=self.frame, text="Login", command=self.button_login)
        log_button.pack(pady=25, padx=10)
        reg_button = customtkinter.CTkButton(master=self.frame, text="Register", command=self.bot_fnc)
        reg_button.pack(pady=25, padx=10)

    def button_login(self):
        obj_login = login.Login(self.frame)
        obj_login.interface_exe()

    def bot_fnc(self):
        obj_register = register.Register(self.frame)
        obj_register.interface_exe()