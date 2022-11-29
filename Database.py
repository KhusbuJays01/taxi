import mysql.connector
conn = mysql.connector.connect(host = "localhost", user="root", password="", database="sample")

print(conn)
cursor = conn.cursor()
# cursor.execute('CREATE DATABASE Sample; ')
cursor.execute('USE Sample;')

# cursor.execute('''CREATE TABLE Userlogin ( userid int PRIMARY KEY,
#                username varchar(30) unique,
#                password varchar(15));''')

cursor.execute("INSERT INTO userlogin(userid ,username, password) VALUES (001, 'khusbu', 'password');")
conn.commit()