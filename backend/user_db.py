from database import db_connection
from classes import user
from tkinter import messagebox

class UserDB:
    def __init__(self, id_user):
        self.id_user = id_user

    def fetch_user_data(self):
        #connect to database to bring info for specific user
        try:
            obj_database = db_connection.DbConnector()
            obj_database.connection_sql()
            connection = obj_database.get_my_db()
            cursor = connection.cursor()
            query = """
                SELECT id_user, name, email, registry_date
                FROM users 
                WHERE id_user = %s
                """
            cursor.execute(query,(self.id_user,))
        except:
            print('Error with id user')    
        finally:
            result = cursor.fetchone()
            #Save result in user object
            if result:
                if len(result) <= 4:
                    obj_user = user.User(result[0],result[1],None,result[2], result[3])
                else:
                    obj_user = user.User(result[0],result[1],result[2],result[3], result[4])
                return obj_user
            else:
                messagebox.showinfo("People Finance","user not found")
            obj_database.close_connection(cursor, connection)