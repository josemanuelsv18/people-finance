from abc import ABC, abstractmethod
import base64
from tkinter import messagebox
from database import db_connection

class LoginUserDB(ABC):
    def __init__(self, name, surname, email, password):
        self.user_id = None
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

    #getters
    def get_user_id(self):
        return self.user_id
    def get_name(self):
        return self.name
    def get_surname(self):
        return self.surname
    def get_email(self):
        return self.email
    #encodes password in base64 for security
    def encode_password(self):
        password_bytes = self.password.encode('utf-8')
        encoded_password = base64.b64encode(password_bytes)
        encoded_password = encoded_password.decode('utf-8')
        return encoded_password
    
    @abstractmethod
    def user_login(self):
        pass

    def show_message(self, message):
        messagebox.showinfo("People Finance", message)
    
    def find_id_user(self, email):
        obj_db = db_connection.DbConnector()
        connection = None
        cursor = None
        try:
            obj_db.connection_sql()
            connection = obj_db.get_my_db()
            cursor = connection.cursor()
            #Query to return new user id to automatically initiate sesion after user created
            query = "SELECT id_user FROM users WHERE email = %s"
            cursor.execute(query,(email,))
            result = cursor.fetchone()
            return result
        except:
            self.show_message('Email not found in the database')
        finally:
            obj_db.close_connection(cursor, connection)