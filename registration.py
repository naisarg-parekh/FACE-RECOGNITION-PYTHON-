from tkinter import *
from PIL import ImageTk
import os
from tkinter import messagebox


class register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration")
        self.root.geometry("1199x600+50+25")

        self.bg = ImageTk.PhotoImage(file="images/rbg1.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        Frame_register = Frame(self.root, bg="white")
        Frame_register.place(x=350, y=50, height=450, width=600)

        global username
        global password
        username = StringVar()
        password = StringVar()

        title = Label(Frame_register, text="Register", font=("Impact", 35, "bold"), fg="skyblue", bg="white").place(
            x=220, y=10)

        lbl_name = Label(Frame_register, text="Enter Name", font=("Goudy old style", 10, "bold"), fg="gray",
                         bg="white").place(x=120, y=120)
        self.txt_name = Entry(Frame_register, font=("times new roman", 10), bg="lightgray")
        self.txt_name.place(x=120, y=145, width=350, height=35)

        lbl_user = Label(Frame_register, text="Username", font=("Goudy old style", 10, "bold"), fg="gray",
                         bg="white").place(x=120, y=200)
        self.txt_user = Entry(Frame_register, textvariable=username, font=("times new roman", 10), bg="lightgray")
        self.txt_user.place(x=120, y=225, width=350, height=35)

        lbl_pass = Label(Frame_register, text="Password", font=("Goudy old style", 10, "bold"), fg="gray",
                         bg="white").place(x=120, y=280)
        self.txt_pass = Entry(Frame_register, textvariable=password, font=("times new roman", 10), bg="lightgray")
        self.txt_pass.place(x=120, y=305, width=350, height=35)

        back_btn = Button(Frame_register, command=self.back, text="Back to Login Page", bg="white", cursor="hand2",
                          fg="blue", bd=0,
                          font=("times new roman", 8)).place(x=480, y=420)

        register_btn = Button(Frame_register, cursor="hand2", text="REGISTER", fg="white",
                              bg="skyblue", font=("times new roman", 15, "bold")).place(x=200, y=360, width=180,
                                                                                        height=40)

    def back(self):
        os.system('python login.py')

    def reg_function(self):
        username_info = self.txt_user.get()
        password_info = self.txt_pass.get()

        file = open(username_info + ".txt", "w")
        file.write(username_info)
        file.write(password_info)
        file.close()

        self.txt_user.delete(0, END)
        self.txt_pass.delete(0, END)

        messagebox.showinfo("Message", "Registration Successful")


root = Tk()
obj = register(root)
root.mainloop()
