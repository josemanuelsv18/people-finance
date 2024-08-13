import mysql.connector
import xml_reader

class DbConnector:
    def __init__(self):
        self.my_db = ''
    
    def get_my_db(self):
        return self.my_db

    def connection_sql(self):
        obj_xmlreader = xml_reader.XmlReader('archives/connection.xml')
        obj_xmlreader.data_xml()
        print(type(obj_xmlreader.get_host()))
        self.my_db = mysql.connector.connect(
            host=obj_xmlreader.get_host(),
            user=obj_xmlreader.get_username(),
            password=obj_xmlreader.get_password()
        )
        print(self.my_db)

obj_prueba = DbConnector()
obj_prueba.connection_sql()
    

#mydb = mysql.connector.connect(
#    host="localhost",
#    user="peoplef_connect",
#    password="P30pl3.123"
#)