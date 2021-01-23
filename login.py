from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import os

class login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x600+50+25")
        #BG Image
        self.bg = ImageTk.PhotoImage(file="images/lbg.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        #Login Frame
        Frame_login=Frame(self.root, bg="white")
        Frame_login.place(x=150, y=150, height=340, width=500)


        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="skyblue",bg="white").place(x=135,y=30)
        desc=Label(Frame_login,text="Student Login for Attendance",font=("Goudy old style",15,"bold"),fg="skyblue",bg="white").place(x=100,y=100)

        lbl_user = Label(Frame_login, text="Username", font=("Goudy old style", 10, "bold"),fg="gray", bg="white").place(x=90, y=145)
        self.txt_user=Entry(Frame_login,font=("times new roman",10),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)

        lbl_pass = Label(Frame_login, text="Password", font=("Goudy old style", 10, "bold"), fg="gray",bg="white").place(x=90, y=210)
        self.txt_pass = Entry(Frame_login, font=("times new roman", 10), bg="lightgray")
        self.txt_pass.place(x=90, y=240, width=350, height=35)

        forget=Button(Frame_login,text="Forget Password?",bg="white",cursor="hand2",fg="blue",bd=0,font=("times new roman",8)).place(x=90,y=280)
        register = Button(Frame_login, command= self.register_here, text="To Register, Click Here", bg="white", cursor="hand2", fg="blue", bd=0,
                        font=("times new roman", 8)).place(x=330, y=280)
        login_btn = Button(self.root, command=self.login_function, cursor="hand2", text="Login", fg="white", bg="skyblue", font=("times new roman", 15,"bold")).place(x=300, y=470,width=180,height=40)

    def register_here(self):
        os.system('python registration.py')


    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_pass.get()!="12345" or self.txt_user.get()!="SPS":
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
        else:
            messagebox.showinfo("Welcome",f"Welcome {self.txt_user.get()}\nYour Password: {self.txt_pass.get()}")
            os.system('python Mainpage.py')

root = Tk()
obj = login(root)
root.mainloop()
