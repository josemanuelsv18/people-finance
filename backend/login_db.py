from database import db_connection
from backend import login_user_db
import base64

class LoginDB(login_user_db.LoginUserDB):
    def __init__(self, name, surname, email, password):
        super().__init__(name, surname, email, password)
        self.user_email = ""
        self.user_password = ""
    
    def user_login(self):
        obj_db = db_connection.DbConnector()
        connection = None
        cursor = None
        if not(not self.email or not self.password):
            try:
                #database connection and cursor creation
                obj_db.connection_sql()
                connection = obj_db.get_my_db()
                cursor = connection.cursor()
                #query exec
                query = "SELECT email, password FROM users WHERE email = %s"
                cursor.execute(query,(self.email,))
                result = cursor.fetchone()
                self.user_email = result[0]
                self.user_password = result[1]  
            except Exception as ex:
                print("error in login", ex)
            finally:
                obj_db.close_connection(cursor, connection)

            
            #decode password from the server
            try:
                decoded_bytes = base64.b64decode(self.user_password)
                decoded_password = decoded_bytes.decode('utf-8')
            except Exception as e:
                print("Couldn't decode the password", e)
            if self.user_email == self.email and decoded_password == self.password:
                #find user id using the email
                result_email = self.find_id_user(self.email)
                self.user_id = result_email[0]
                return True
            else:
                self.show_message('Login failed, email or password are incorrect')
                return False