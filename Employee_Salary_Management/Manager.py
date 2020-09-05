# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 14:23:27 2020

@author: jaity banerjee
"""

from tkinter import *
from tkinter import messagebox
import os
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Manager Login ")
        self.root.geometry("550x450")
        self.root.configure(bg="#006666")
        root.resizable(False,False)
        Frame_Login=Frame(self.root,bg="#FF9966")
        Frame_Login.place(x=21,y=21,height=410,width=500)            
        
        title=Label(Frame_Login,text="Login Portal",font=('times',25,"bold","italic"),fg="Black",bg="#FF9966").place(x=80,y=30)
        desc=Label(Frame_Login,text="Manager Login Area",font=('calligrapher',11),fg="red",bg="#FF9966").place(x=80,y=70)
        lbl_user=Label(Frame_Login,text="User Name",font=('calligrapher',12,"bold"),fg="Black",bg="#FF9966").place(x=80,y=110)
        self.txt_user=Entry(Frame_Login,font=("times new roman",15),bg="LightGrey")
        self.txt_user.place(x=80,y=150,width=350,height=35)
        
        lbl_pass=Label(Frame_Login,text="Password",font=('calligrapher',12,"bold"),fg="Black",bg="#FF9966").place(x=80,y=210)
        self.txt_pass=Entry(Frame_Login,font=("times new roman",15),bg="LightGrey")
        self.txt_pass.place(x=80,y=250,width=350,height=35)
        
        btn=Button(Frame_Login,text="Login Here",font=('times',15,"bold"),width=15,fg="Black",bg="#006600",command=self.loginFunc).place(x=80,y=320)
        
                   
                   
    def loginFunc(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_pass.get()!="1234":
            messagebox.showerror("Error","Invalid Password",parent=self.root)
        elif self.txt_user.get()!="Jaity":
            messagebox.showerror("Error","Invalid Username",parent=self.root)
        else:
            root.destroy()
            os.system("python Employee_salary.py")
            
            
root=Tk()
obj=Login(root)
root.mainloop()
        