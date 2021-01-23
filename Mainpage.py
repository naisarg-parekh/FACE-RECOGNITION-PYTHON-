
import os
from tkinter import *
from PIL import ImageTk, Image

def enter():
    os.system('python AttendanceProject1.py')

def view():
    os.system('Attendance.csv')


class login:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance System")
        self.root.geometry("1199x600+50+25")

        self.bg = ImageTk.PhotoImage(file="images/rbg1.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        Frame_main = Frame(self.root, bg="white")
        Frame_main.place(x=350, y=50, height=450, width=600)

        title = Label(Frame_main, text="Online Attendance", font=("Impact", 35, "bold"), fg="skyblue", bg="white").place(
            x=120, y=10)

        Label(Frame_main, text="*Since you have logged in successfully, please enter you image!*", fg="red", bg="beige",
                            font=("Calibri",15)).place(x=30, y=80)

        Label(Frame_main, text="To Enter your Attendance, Click on 'ENTER'", fg="black", bg="white",
              font=("Calibri", 15)).place(x=30, y=145)

        Button(Frame_main, command=enter, text="ENTER", bg="skyblue", cursor="hand2",
                          fg="white", font=("times new roman", 12, "bold"), width=15, height=1).place(x=220, y=190)

        Label(Frame_main, text="To View your Attendance, Click on 'VIEW'", fg="black", bg="white",
              font=("Calibri", 15)).place(x=30, y=230)

        Button(Frame_main, command=view, text="VIEW", bg="skyblue", cursor="hand2",
               fg="white", font=("times new roman", 12, "bold"), width=15, height=1).place(x=220, y=275)

        Button(Frame_main, command=root.quit, text="EXIT", bg="red", cursor="hand2",
               fg="white", font=("times new roman", 12, "bold"), width=15, height=1).place(x=220, y=400)


root = Tk()
obj = login(root)
root.mainloop()
