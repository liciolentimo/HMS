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

        self.button_hospital = Button(self.Loginframe_three,text="Hospital Management Window",state=DISABLED,font=("roboto",15,"bold"),command=self.hospital_window)
        self.button_hospital.grid(row=0,column=1,padx=10,pady=10)

        self.button_dr_appointment = Button(self.Loginframe_three,text="Doctor Management Window",state=DISABLED,font=("roboto",15,"bold"),command=self.dr_appointment_window)
        self.button_dr_appointment.grid(row=1,column=0,padx=10,pady=10)

        self.button_med_stock = Button(self.Loginframe_three,text="Medicine Stock Window",state=DISABLED,font=("roboto",15,"bold"),command=self.medicine_stock_window)
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
        self.app = Registration(self.new_window)

    def hospital_window(self):
        self.new_window = Toplevel(self.master)
        self.app = window_three(self.new_window)

    def dr_appointment_window(self):
        self.new_window = Toplevel(self.master)
        self.app = window_four(self.new_window)

    def medicine_stock_window(self):
        self.new_window = Toplevel(self.master)
        self.app = window_five(self.new_window)

class Registration:
    def __init__(self,root):
        self.root = root
        self.root.title("Patient Registration System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="black")

        registration_date = StringVar()
        registration_date.set(time.strftime("%d/%m/%y"))
        Ref = StringVar()
        mobile_no = StringVar()
        pincode = StringVar()
        address = StringVar()
        firstname = StringVar()
        lastname = StringVar()

        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = StringVar()
        var5 = IntVar()

        membership = StringVar()
        membership.set("0")

        def exit_btn():
            exit_btn = tkinter.messagebox.askyesno("Member Registration Form","Are you sure you want to exit?")
            if exit_btn > 0:
                root.destroy()
            else:
                self.new_window = Toplevel(self.master)
                self.app = Registration(self.new_window)
                return

        def reset_btn():
            firstname.set("")
            lastname.set("")
            mobile_no.set("")
            pincode.set("")
            address.set("")
            Ref.set("")
            var1.set("")
            var2.set("")
            var3.set("")
            var4.set("")
            var5.set("")
            membership.set("0")
            member_gendercmb.current(0)
            member_id_proofcmb.current(0)
            member_memtypecmb.current(0)
            member_paymentcmb.current(0)
            member_membershiptxt(state=DISABLED)

        def reset_btn_msg():
            reset_btn_msg = tkinter.messagebox.askokcancel("Member Registration Form","You want to add as new record?")
            if reset_btn_msg > 0:
                reset_btn()
            elif reset_btn_msg <= 0:
                reset_btn()
                detail_labeltxt.delete("1.0",END)
                return

        def reference_number():
            ranumber = random.randint(10000,9999999)
            randomnumber = str(ranumber)
            Ref.set(randomnumber)

        def membership_fees():
            if(var5.get() == 1):
                member_membershiptxt.configure(state=NORMAL)
                item = float(15000)
                membership.set(str(item)+ "KES")
            elif(var5.get() == 0):
                member_membershiptxt.configure(state=DISABLED)
                membership.set("0")

        def receipt():
            reference_number()
            detail_labeltxt.insert(END,"\t"+registration_date.get()+"  \t"+Ref.get()+"\t\t"+firstname.get()+'  \t'+lastname.get()+"\t"+mobile_no.get()+"  \t"+'\t\t'+address.get()+"  \t\t"+pincode.get()+"  \t"+member_gendercmb.get()+"\t\t"+membership.get()+"\n")
        

        title = Label(self.root,text="Member Registration Form",font=("montserrat",30,"bold"),bd=5,relief=GROOVE,bg="#1E88E5",fg="#000000")
        title.pack(side=TOP,fill=X)

        manage_frame = Frame(self.root,bd=4,relief=RIDGE,bg="#303F9F")
        manage_frame.place(x=20,y=100,width=450,height=630)

        customer_title = Label(manage_frame,text="Customer Details",font=("montserrat",20,"bold"),bg="#303F9F",fg="white")
        customer_title.grid(row=0,columnspan=2,pady=5)

        member_datelbl = Label(manage_frame,text="Date",font=("montserrat",15,"bold"),bg="#303F9F",fg="white")
        member_datelbl.grid(row=1,column=0,pady=5,padx=10,sticky="w")

        member_datetxt = Entry(manage_frame,font=("montserrat",15,"bold"),textvariable=registration_date)
        member_datetxt.grid(row=1,column=1,pady=5,padx=10,sticky="w")

        member_reflbl = Label(manage_frame,text="Reference ID",font=("montserrat",15,"bold"),bg="#303F9F",fg="white")
        member_reflbl.grid(row=2,column=0,pady=5,padx=10,sticky="w")

        member_reftxt = Entry(manage_frame,font=("montserrat",15,"bold"),state=DISABLED,text=Ref)
        member_reftxt.grid(row=2,column=1,pady=5,padx=10,sticky="w")

        member_fnamelbl = Label(manage_frame,text="FirstName",font=("montserrat",15,"bold"),bg="#303F9F",fg="white")
        member_fnamelbl.grid(row=3,column=0,pady=5,padx=10,sticky="w")

        member_fnametxt = Entry(manage_frame,font=("montserrat",15,"bold"),textvariable=firstname)
        member_fnametxt.grid(row=3,column=1,pady=5,padx=10,sticky="w")

        member_lnamelbl = Label(manage_frame,text="LastName",font=("montserrat",15,"bold"),bg="#303F9F",fg="white")
        member_lnamelbl.grid(row=4,column=0,pady=5,padx=10,sticky="w")

        member_lnametxt = Entry(manage_frame,font=("montserrat",15,"bold"),textvariable=lastname)
        member_lnametxt.grid(row=4,column=1,pady=5,padx=10,sticky="w")

        member_mobilelbl = Label(manage_frame,text="Mobile",font=("montserrat",15,"bold"),bg="#303F9F",fg="white")
        member_mobilelbl.grid(row=5,column=0,pady=5,padx=10,sticky="w")

        member_mobiletxt = Entry(manage_frame,font=("montserrat",15,"bold"),textvariable=mobile_no)
        member_mobiletxt.grid(row=5,column=1,pady=5,padx=10,sticky="w")

        member_addresslbl = Label(manage_frame,text="Address",font=("montserrat",15,"bold"),bg="#303F9F",fg="white")
        member_addresslbl.grid(row=6,column=0,pady=5,padx=10,sticky="w")

        member_addresstxt = Entry(manage_frame,font=("montserrat",15,"bold"),textvariable=address)
        member_addresstxt.grid(row=6,column=1,pady=5,padx=10,sticky="w")

        member_pincodelbl = Label(manage_frame,text="Post Code",font=("montserrat",15,"bold"),bg="#303F9F",fg="white")
        member_pincodelbl.grid(row=7,column=0,pady=5,padx=10,sticky="w")

        member_pincodetxt = Entry(manage_frame,font=("montserrat",15,"bold"),textvariable=pincode)
        member_pincodetxt.grid(row=7,column=1,pady=5,padx=10,sticky="w")

        member_genderlbl = Label(manage_frame,text="Gender",font=("montserrat",15,"bold"),bg="#303F9F",fg="white")
        member_genderlbl.grid(row=8,column=0,pady=5,padx=10,sticky="w")

        member_gendercmb = ttk.Combobox(manage_frame,text=var4,state="readonly",font=("montserrat",15,"bold"),width=19)
        member_gendercmb['values'] = ("","Male","Female","Other")
        member_gendercmb.current(0)
        member_gendercmb.grid(row=8,column=1,pady=5,padx=10,sticky="w")

        member_id_prooflbl = Label(manage_frame,text="ID Proof",font=("montserrat",15,"bold"),bg="#303F9F",fg="white")
        member_id_prooflbl.grid(row=9,column=0,pady=5,padx=10,sticky="w")

        member_id_proofcmb = ttk.Combobox(manage_frame,text=var3,state="readonly",font=("montserrat",15,"bold"),width=19)
        member_id_proofcmb['values'] = ("","National ID","Passport","Student ID")
        member_id_proofcmb.current(0)
        member_id_proofcmb.grid(row=9,column=1,pady=5,padx=10,sticky="w")

        member_memtypelbl = Label(manage_frame,text="Member Type",font=("montserrat",15,"bold"),bg="#303F9F",fg="white")
        member_memtypelbl.grid(row=10,column=0,pady=5,padx=10,sticky="w")

        member_memtypecmb = ttk.Combobox(manage_frame,text=var2,state="readonly",font=("montserrat",15,"bold"),width=19)
        member_memtypecmb['values'] = ("","In-Patient","Out-Patient")
        member_memtypecmb.current(0)
        member_memtypecmb.grid(row=10,column=1,pady=5,padx=10,sticky="w")

        member_paymentlbl = Label(manage_frame,text="Payment Type",font=("montserrat",15,"bold"),bg="#303F9F",fg="white")
        member_paymentlbl.grid(row=11,column=0,pady=5,padx=10,sticky="w")

        member_paymentcmb = ttk.Combobox(manage_frame,text=var1,state="readonly",font=("montserrat",15,"bold"),width=19)
        member_paymentcmb['values'] = ("","Insurance","Cash","M-PESA","Card")
        member_paymentcmb.current(0)
        member_paymentcmb.grid(row=11,column=1,pady=5,padx=10,sticky="w")

        member_membership = Checkbutton(manage_frame,text="Membership Fees",variable=var5,onvalue=1,offvalue=0,font=("montserrat",15,"bold"),bg="#303F9F",fg="white",command=membership_fees)
        member_membership.grid(row=12,column=0,sticky="w")
        member_membershiptxt = Entry(manage_frame,font=("montserrat",15,"bold"),state=DISABLED,justify=RIGHT,textvariable=membership)
        member_membershiptxt.grid(row=12,column=1,pady=5,padx=10,sticky="w")

        detail_frame = Frame(self.root,relief=RIDGE,bg="#303F9F")
        detail_frame.place(x=500,y=100,width=800,height=600)

        detail_label = Label(detail_frame,font=("montserrat",11,"bold"),pady=10,padx=2,width=95,text="Date\t  Ref ID\t  First Name  Last Name  Mobile No  Address Pin Code  Gender  Membership")
        detail_label.grid(row=0,column=0,columnspan=4,sticky="w")
        detail_labeltxt = Text(detail_frame,width=123,height=34,font=("montserrat",8))
        detail_labeltxt.grid(row=1,column=0,columnspan=4)

        receipt_btn = Button(detail_frame,padx=15,bd=5,font=("montserrat",12,"bold"),bg="#388E3C",width=20,text="Receipt",command=receipt)
        receipt_btn.grid(row=2,column=0)

        reset_btn = Button(detail_frame,padx=15,bd=5,font=("montserrat",12,"bold"),bg="#616161",width=20,text="Reset",command=reset_btn_msg)
        reset_btn.grid(row=2,column=1)

        exit_btn = Button(detail_frame,padx=15,bd=5,font=("montserrat",12,"bold"),bg="#b71c1c",width=20,text="Exit",command=exit_btn)
        exit_btn.grid(row=2,column=2)

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
