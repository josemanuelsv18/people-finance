import xml.etree.ElementTree as ET
import base64
#class for xml reader and base 64 decoder

class XmlReader:
    def __init__(self, xml_doc):
        self.host = ""
        self.port = ""
        self.username = ""
        self.password = ""
        self.dbname = ""
        #use same format as "archives/connection.xml"
        self.xml_doc = xml_doc
        
    
    #getters
    def get_host(self):
        return self.host
    
    def get_port(self):
        return self.port
    
    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password
    
    def get_dbname(self):
        return self.dbname
    
    #decoder
    def data_xml(self):
        tree = ET.parse(self.xml_doc)
        root = tree.getroot()
        #root[][].text to bring specific data from xml
        self.host = root[0][0].text.encode('ascii')
        self.host = base64.b64decode(self.host)
        self.host = self.host.decode('ascii')

        self.username = root[0][2].text.encode('ascii')
        self.username = base64.b64decode(self.username)
        self.username = self.username.decode('ascii')

        self.password = root[0][3].text.encode('ascii')
        self.password = base64.b64decode(self.password)
        self.password = self.password.decode('ascii')