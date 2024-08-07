import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="peoplef_connect",
    password="P30pl3.123"
)
print(mydb)