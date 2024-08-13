import mysql.connector
import xml_reader
from mysql.connector import Error

class DbConnector:
    def __init__(self):
        self.my_db = ''
    
    def get_my_db(self):
        return self.my_db

    def connection_sql(self):
        try:
            obj_xmlreader = xml_reader.XmlReader('archives/connection.xml')
            obj_xmlreader.data_xml()
            try:
                #stablish connection with the database
                self.my_db = mysql.connector.connect(
                    host=obj_xmlreader.get_host(),
                    database=obj_xmlreader.get_dbname(),
                    user=obj_xmlreader.get_username(),
                    password=obj_xmlreader.get_password()
                )
                if self.my_db.is_connected():
                    db_info = self.my_db.get_server_info()
                    print('Connected to MySql version ',db_info)
            except Error as e:
                print('Failed to connect with the database')
        except:
            print("XML document couldn't be readed")
        finally:
            #close connection if open
            if self.my_db.is_connected():
                self.my_db.close()
                print('MySql connection has been closed')