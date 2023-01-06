import mysql.connector
import sys
from tkinter import messagebox

class maindatabse():
    def databaseConnection(self):
        conn = None
        try:
            conn = mysql.connector.connect(host = "localhost", user="root", password="", database="taxi_booking")
        except:
            messagebox.showerror("Error", sys.exc_info())
        finally:
            return conn

    def get_booking_table_data(self):
        sql = 'select * from Booking'
        conn = self.databaseConnection()
        cursor = conn.cursor(prepared=True)
        cursor.execute(sql)
        data = cursor.fetchall()
        if not data:
            return False
        conn.close()
        return data


    # ----edit------------------------------
    def edit(self, sql, conn, cursor, value):
        if sql and cursor:
            try:
                cursor.execute(sql, value)
            except mysql.connector.Error as e:
                messagebox.showerror("ERROR", e.msg)
            else:
                conn.commit()
                return True


#     -----------delete-------------------




