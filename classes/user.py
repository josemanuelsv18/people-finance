class User:
    def __init__(self,id_user, name, surname, email, init_day):
        self.id_user = id_user
        self.name = name
        self.surname = surname
        self.email = email
        self.init_day = init_day
        #Dont include password yet for security and not necesity

    def get_id_user(self):
        return self.id_user
    def get_name(self):
        return self.name
    def get_surname(self):
        return self.surname
    def get_email(self):
        return self.email
    def get_init_day(self):
        return self.init_day