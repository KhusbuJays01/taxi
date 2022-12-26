from mysql import connector

conn = mysql.connect("""
    host="localhost",
    user = "root",
    password="",
    database = "Middleware"
""")

print(conn)