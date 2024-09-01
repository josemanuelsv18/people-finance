class User:
    def __init__(self, name, surname, email, init_day):
        self.name = name
        self.surname = surname
        self.email = email
        self.init_day = init_day
        #Dont include password yet for security and not necesity

    def get_name(self):
        return self.name
    def get_surname(self):
        return self.surname
    def get_email(self):
        return self.email
    def get_init_day(self):
        return self.init_day