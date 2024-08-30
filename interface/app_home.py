from interface import interface_template
import customtkinter

class AppHome(interface_template.InterfaceTemplate):
    def __init__(self, frame, id_user):
        super().__init__(frame)
        self.id_user = id_user

    #Main page interface
    def interface_exe(self):
        #return super().interface_exe()
        #Clean frame
        for widget in self.frame.winfo_children():
            widget.destroy()
        #inner frame
        self.frame.pack(pady=20, padx=60, fill="")
        #inner frame
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)
        #title
        label = customtkinter.CTkLabel(master=self.frame, text="People Finance", font=("Roboto", 24))
        label.pack(pady=12, padx=10)
        label = customtkinter.CTkLabel(master=self.frame, text="Welcome ", font=("Roboto",24))