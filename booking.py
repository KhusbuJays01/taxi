from tkinter import *
from PIL import ImageTk, Image

class Booking (Tk):
    def __init__(self):
        super().__init__()
        self.title("make_booking")
        self.resizable(0, 0)
        self.geometry('1360x700')
        self.frame = Frame(self)
        self.frame.pack()

# # image size
        image = Image.open('pro.png').resize((1360,700), Image.ANTIALIAS)

        bgImage=ImageTk.PhotoImage(image)
#
        bgLabel=Label(self,image=bgImage, width=1440, height=700)
        bgLabel.pack()
#
        head = Label(text=" Online Booking System", bg="#373662",font=("", 27, "bold"), fg= "White")
        head.place(x=520, y=20)

        label_win =Label(bgLabel, bg="white", width=50, height=80)
        label_win.place(x=990, y=10)

        lbl2 = Button(self, text="Make Booking", bg="white", font=("", 15, "bold"), fg="Black")
        lbl2.place(x=1070, y=150)

        lbl2 = Button (self, text = "View Booking", bg = "white", font=("", 15, "bold"), fg= "Black")
        lbl2.place(x=1070, y=230)

        lbl3 = Button (self, text = "Edit Booking", bg = "white", font=("", 15, "bold"), fg= "Black")
        lbl3.place(x=1070, y=300)

        lbl4 = Button (self, text = "Confirm Booking", bg = "white", font=("", 15, "bold"), fg= "Black")
        lbl4.place(x=1070, y=370)

        lbl6 = Button(self, text="Cancel Booking", bg="white", font=("", 15, "bold"), fg="Black")
        lbl6.place(x=1070, y=440)

        lbl5 = Button(self, text="Payment", bg="white", font=("", 15, "bold"), fg="Black")
        lbl5.place(x=1080, y=500)

        lbl4 = Button(self, text="Exit", bg="white", font=("", 15, "bold"), fg="Red")
        lbl4.place(x=1090, y=570)







        self.mainloop()
if __name__ == '__main__':
    login = Booking()



