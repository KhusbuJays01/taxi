import mysql.connector
import sys
from tkinter import messagebox

class maindatabse():
    def databaseConnection(self):
        conn = None
        try:
            conn = mysql.connector.connect(host = "localhost", user="root", password="", database="khusbu")
        except:
            messagebox.showerror("Error", sys.exc_info())
        finally:
            return conn
