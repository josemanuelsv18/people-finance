from database import db_connection

class RegisterUser:
    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

    #getters
    def get_name(self):
        return self.name
    def get_surname(self):
        return self.surname
    def get_email(self):
        return self.email
    def get_password(self):
        return self.password
    
    #create
    def create_new_user(self):
        obj_db = db_connection.DbConnector()
        try:
            obj_db.connection_sql()
            connection = obj_db.get_my_db()
            cursor = connection.cursor
            #call database stored procedure with new users parameters
            cursor.callproc('userRegister', [self.name, self.surname, self.email, self.password])
            connection.commit()
            print('new user created')

        except:
            print('Error in user data')
        finally:
            #close connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()
