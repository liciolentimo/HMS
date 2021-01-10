import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

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

if __name__ == "__main__":
    root = Tk()
    app = Registration(root)
    root.mainloop()