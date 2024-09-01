from database import db_connection
from backend import login_user_db
import re

class RegisterUser(login_user_db.LoginUserDB):
    def __init__(self, name, surname, email, password):
        super().__init__(name, surname, email, password)

    #verify if another account have the same email, if it alredy exist cant create a new user
    def verify_email(self):
        #Verify if string is in email format
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not(re.match(email_regex, self.email)):
            self.show_message('Email is not valid')
            return False
        #verify if email is not duplicated
            #create connection to db
        obj_query = db_connection.DbConnector()
        obj_query.connection_sql()
        connection = obj_query.get_my_db()
        cursor = connection.cursor()
        #create and execute the query
        query = "SELECT COUNT(*) FROM users WHERE email = %s"
        cursor.execute(query,(self.email,))
        result = cursor.fetchone()
        if result[0]>0:
            self.show_message("This email alredy have an account")
            obj_query.close_connection(cursor, connection)
            return False
        else:
            obj_query.close_connection(cursor, connection)
            return True

    #insert new user in database
    def user_login(self):
        obj_db = db_connection.DbConnector()
        connection = None
        cursor = None
        if self.name and self.email and self.password:
            if self.verify_email():
                #debug prints
                print(self.name, self.surname, self.email, self.encode_password())
                try:
                    obj_db.connection_sql()
                    connection = obj_db.get_my_db()
                    cursor = connection.cursor()
                    #call database stored procedure with new users parameters
                    cursor.callproc('userRegister', [self.name, self.surname, self.email, self.encode_password()])
                    connection.commit()
                    print('new user created')
                    return True            
                except Exception as e:
                    print('Error in user data',e)
                    return False
                finally:
                    #Query to return new user id to automatically initiate sesion after user created
                    result = self.find_id_user(self.email)
                    self.user_id = result[0]
                    #close connection
                    obj_db.close_connection(cursor, connection)
        else:
           self.show_message("user data incomplete")
           return False