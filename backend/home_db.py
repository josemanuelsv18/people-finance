from database import db_connection
from classes import user

class HomeDB:
    def __init__(self, id_user):
        self.id_user = id_user

    def fetch_user_data(self):
        #connect to database to bring info for specific user
        obj_database = db_connection.DbConnector()
        obj_database.connection_sql()
        connection = obj_database.get_my_db()
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE id_user = %s"
        cursor.execute(query,(self.id_user,))
        result = cursor.fetchone()
        #Save result in user object
        obj_user = user.User()