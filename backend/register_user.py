from database import db_connection
import base64

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
    #def get_password(self):
    #    return self.password
    #encodes password in base64 for security
    def encode_password(self):
        password_bytes = self.password.encode('utf-8')
        encoded_password = base64.b64encode(password_bytes)
        encoded_password = encoded_password.decode('utf-8')
        return encoded_password
    
    #create
    def create_new_user(self):
        obj_db = db_connection.DbConnector()
        connection = None
        cursor = None
        if not(not self.name and not self.email and not self.password):
            try:
                obj_db.connection_sql()
                connection = obj_db.get_my_db()
                cursor = connection.cursor()
                #call database stored procedure with new users parameters
                cursor.callproc('userRegister', [self.name, self.surname, self.email, self.encode_password()])
                connection.commit()
                print('new user created')
                return True            
            except:
                print('Error in user data')
                return False
            finally:
                #close connection
                if cursor:
                    cursor.close()
                    print('Cursor has been closed')
                if connection:
                    connection.close()
                    print('Connection has been closed')
        else:
            print("User data incomplete")
            return False
    
    