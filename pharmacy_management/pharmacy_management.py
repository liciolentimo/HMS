import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

def main():
    root = Tk()
    app = window_one(root)
    root.mainloop()

class window_one():
    def __init__(self,master):
        self.master = master
        self.master.title("Pharmacy Management System")
        self.master.geometry('1350x750+0+0') # x-axis,y-axis,0,0
        self.frame = Frame(self.master)
        self.frame.pack()

        self.username = StringVar()
        self.password = StringVar()

        self.LabelTitle = Label(self.frame,text = "  Pharmacy Management System  ",font=("arial",40,"bold"),bd=10,relief="sunken")
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=20)

        self.Loginframe_one = Frame(self.frame,width=1000,height=300,bd=10,relief="groove")
        self.Loginframe_one.grid(row=1,column=0)

        self.Loginframe_two = Frame(self.frame,width=1000,height=100,bd=10,relief="groove")
        self.Loginframe_two.grid(row=2,column=0,pady=15)

        self.Loginframe_three = Frame(self.frame,width=1000,height=200,bd=10,relief="groove")
        self.Loginframe_three.grid(row=6,column=0,pady=5)

        self.button_reg = Button(self.Loginframe_three,text="Patient Registration Window",state=DISABLED,font=("roboto",15,"bold"),command=self.registration_window)
        self.button_reg.grid(row=0,column=0,padx=10,pady=10)

        self.button_hospital = Button(self.Loginframe_three,text="Patient Registration Window",state=DISABLED,font=("roboto",15,"bold"),command=self.hospital_window)
        self.button_hospital.grid(row=0,column=1,padx=10,pady=10)

        self.button_dr_appointment = Button(self.Loginframe_three,text="Patient Registration Window",state=DISABLED,font=("roboto",15,"bold"),command=self.dr_appointment_window)
        self.button_dr_appointment.grid(row=1,column=0,padx=10,pady=10)

        self.button_med_stock = Button(self.Loginframe_three,text="Patient Registration Window",state=DISABLED,font=("roboto",15,"bold"),command=self.medicine_stock_window)
        self.button_med_stock.grid(row=1,column=1,padx=10,pady=10)

        self.LabelUsername = Label(self.Loginframe_one,text="Username",font=("roboto",20,"bold"),bd=3)
        self.LabelUsername.grid(row=0,column=0)

        self.text_username = Entry(self.Loginframe_one,font=("roboto",20,"bold"),bd=3,textvariable=self.username)
        self.text_username.grid(row=0,column=1,padx=40,pady=15)

        self.LabelPassword = Label(self.Loginframe_one,text="Password",font=("roboto",20,"bold"),bd=3)
        self.LabelPassword.grid(row=1,column=0)

        self.text_password = Entry(self.Loginframe_one,font=("roboto",20,"bold"),show="*",bd=3,textvariable=self.password)
        self.text_password.grid(row=1,column=1,padx=40,pady=15)

        self.button_login = Button(self.Loginframe_two,text="Login",width=20,font=("roboto",18,"bold"),command=self.login)
        self.button_login.grid(row=0,column=0,padx=10,pady=10)

        self.button_reset = Button(self.Loginframe_two,text="Reset",width=20,font=("roboto",18,"bold"),command=self.reset)
        self.button_reset.grid(row=0,column=3,padx=10,pady=10)

        self.button_exit = Button(self.Loginframe_two,text="Exit",width=20,font=("roboto",18,"bold"),command=self.exit)
        self.button_exit.grid(row=0,column=6,padx=10,pady=10)

    def login(self):
        user = self.username.get()
        pwd = self.password.get()

        if(user == str("admin") and (pwd == str("admin"))):
            self.button_reg.config(state=NORMAL)
            self.button_hospital.config(state=NORMAL)
            self.button_dr_appointment.config(state=NORMAL)
            self.button_med_stock.config(state=NORMAL)
        else:
            tkinter.messagebox.askyesno("Pharmacy Management System","You have entered an invalid username or password")
            self.button_reg.config(state=DISABLED)
            self.button_hospital.config(state=DISABLED)
            self.button_dr_appointment.config(state=DISABLED)
            self.button_med_stock.config(state=DISABLED)

            self.username.set("")
            self.password.set("")
            self.text_username.focus()

    def reset(self):
        self.button_reg.config(state=DISABLED)
        self.button_hospital.config(state=DISABLED)
        self.button_dr_appointment.config(state=DISABLED)
        self.button_med_stock.config(state=DISABLED)

        self.username.set("")
        self.password.set("")
        self.text_username.focus()

    def exit(self):
        self.exit = tkinter.messagebox.askyesno("Pharmacy Management System","Are you sure you want to exit?")
        if self.exit > 0:
            self.master.destroy()
            return

    def registration_window(self):
        self.new_window = Toplevel(self.master)
        self.app = window_two(self.new_window)

    def hospital_window(self):
        self.new_window = Toplevel(self.master)
        self.app = window_three(self.new_window)

    def dr_appointment_window(self):
        self.new_window = Toplevel(self.master)
        self.app = window_four(self.new_window)

    def medicine_stock_window(self):
        self.new_window = Toplevel(self.master)
        self.app = window_five(self.new_window)

class window_two():
    def __init__(self,master):
        self.master = master
        self.master.title("Patient Management System")
        self.master.geometry('1350x750+0+0') # x-axis,y-axis,0,0
        self.frame = Frame(self.master)
        self.frame.pack()

class window_three():
    def __init__(self,master):
        self.master = master
        self.master.title("Hospital Management System")
        self.master.geometry('1350x750+0+0') # x-axis,y-axis,0,0
        self.frame = Frame(self.master)
        self.frame.pack()

class window_four():
    def __init__(self,master):
        self.master = master
        self.master.title("Doctor Management System")
        self.master.geometry('1350x750+0+0') # x-axis,y-axis,0,0
        self.frame = Frame(self.master)
        self.frame.pack()

class window_five():
    def __init__(self,master):
        self.master = master
        self.master.title("Medicine Stock System")
        self.master.geometry('1350x750+0+0') # x-axis,y-axis,0,0
        self.frame = Frame(self.master)
        self.frame.pack()

if __name__ == "__main__":
    main()
