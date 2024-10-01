from database import db_connection
from classes import user
from tkinter import messagebox

class UserDB:
    def __init__(self, id_user):
        self.id_user = id_user

    def fetch_user_data(self):
        #connect to database to bring info for specific user
        obj_db = db_connection.DbConnector()
        connection = None
        cursor = None
        try: 
            obj_db.connection_sql()
            connection = obj_db.get_my_db()
            cursor = connection.cursor()
            #query = """
            #    SELECT id_user, name, email, registry_date
            #    FROM users 
            #   WHERE id_user = %s
            #   """
            #cursor.execute(query,(self.id_user,))
            cursor.callproc('userData',[self.id_user])
            for result in cursor.stored_results():
                user_data = result.fetchone()
        except:
            print('Error with id user')    
        finally:
            #Save result in user object
            if user_data:
                if len(user_data) <= 4:
                    obj_user = user.User(user_data[0],user_data[1],None,user_data[2],user_data[3])
                else:
                    obj_user = user.User(user_data[0],user_data[1],user_data[2],user_data[3],user_data[4])
                return obj_user
            else:
                messagebox.showinfo("People Finance","user not found")
            obj_db.close_connection(cursor, connection)