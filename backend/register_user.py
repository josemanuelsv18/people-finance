from database import db_connection
import base64
from tkinter import messagebox

class RegisterUser:
    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.id_new_user = None

    #getters
    def get_name(self):
        return self.name
    def get_surname(self):
        return self.surname
    def get_id_new_user(self):
        return self.id_new_user
    #def get_password(self):
    #    return self.password
    #encodes password in base64 for security
    def encode_password(self):
        password_bytes = self.password.encode('utf-8')
        encoded_password = base64.b64encode(password_bytes)
        encoded_password = encoded_password.decode('utf-8')
        return encoded_password
    
    def verify_email_ex(self):
        obj_query = db_connection.DbConnector()
        obj_query.connection_sql()
        connection = obj_query.get_my_db()
        cursor = connection.cursor()
        query = "SELECT COUNT(*) FROM users WHERE email = %s"
        cursor.execute(query,(self.email,))
        result = cursor.fetchone()
        if result[0]>0:
            messagebox.showinfo("People Finance","This email alredy have an account")
        cursor.close()
        connection.close()

    #insert new user in database
    def create_new_user(self):
        obj_db = db_connection.DbConnector()
        connection = None
        cursor = None
        if not(not self.name or not self.email or not self.password):
            self.verify_email_ex()
            try:
                obj_db.connection_sql()
                connection = obj_db.get_my_db()
                cursor = connection.cursor()
                #call database stored procedure with new users parameters
                cursor.callproc('userRegister', [self.name, self.surname, self.email, self.encode_password()])
                connection.commit()
                print('new user created')
                #Query to return new user id to automatically initiate sesion after user created
                query = "SELECT id_user FROM users WHERE email = %s"
                cursor.execute(query,(self.email,))
                result = cursor.fetchone()
                self.id_new_user = result[0]
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
           messagebox.showinfo("People Finance","user data incomplete")
           return False