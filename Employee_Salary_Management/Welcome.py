# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 14:23:27 2020

@author: jaity banerjee
"""

from tkinter import *
from tkinter import messagebox
import os

def callNxt():
    root.destroy()
    os.system('python employee_reg.py')
    
def callNew():
    root.destroy()
    os.system('python Manager.py')
    
    
class Welcome:
    def __init__(self,root):
        self.root=root
        self.root.title("Welcome to Portal")
        self.root.geometry("900x600+100+40")
        self.root.configure(bg="#FF6666")
        
        Frame_Welcome=Frame(self.root,bg="#66CCCC")
        Frame_Welcome.place(x=450,y=140,height=400,width=500)            
        
        title=Label(Frame_Welcome,text="Login Portal",font=('times',25,"bold"),fg="Black",bg="#66CCCC").place(x=30,y=30)
        desc=Label(Frame_Welcome,text="Existing Login Area",font=('calligrapher',12,"italic"),fg="red",bg="#66CCCC",pady=15).place(x=30,y=70)
        lbl_user=Label(Frame_Welcome,text="User ID",font=('calligrapher',12,"bold"),fg="Black",bg="#66CCCC").place(x=30,y=110)
        self.txt_user=Entry(Frame_Welcome,font=("times new roman",15),bg="orange")
        self.txt_user.place(x=30,y=150,width=350,height=35)
        
        lbl_pass=Label(Frame_Welcome,text="Password",font=('calligrapher',12,"bold"),fg="Black",bg="#66CCCC").place(x=30,y=210)
        self.txt_pass=Entry(Frame_Welcome,font=("times new roman",15),bg="Orange")
        self.txt_pass.place(x=30,y=250,width=350,height=35)
        
        btn=Button(Frame_Welcome,text="Login Here",font=('times',15,"bold"),width=10,fg="Black",bg="purple",command=self.WelcomeFunc).place(x=30,y=320)
        btn=Button(Frame_Welcome,text="New User",font=('times',15,"bold"),width=10,fg="Black",bg="blue",command=callNxt).place(x=180,y=320)
        btn=Button(Frame_Welcome,text="Manager",font=('times',15,"bold"),width=10,fg="Black",bg="brown",command=callNew).place(x=330,y=320)
                   
                   
    def WelcomeFunc(self):
        EmployeeID_Page=self.txt_user.get()
        Password_Page=self.txt_pass.get()
        select="select EmployeeID,Password from student where EmployeeID='%s' "%(EmployeeID_Page)
        mycursor.execute(select)
        result=mycursor.fetchall()
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif EmployeeID_Page!=str(result[0][0]):
            messagebox.showerror("Error","Invalid Password",parent=self.root)
        elif Password_Page!=str(result[0][1]):
            messagebox.showerror("Error","Invalid UserID",parent=self.root)
        else:
            root.destroy()
            os.system("python Employee_Page.py")
            
            
root=Tk()
obj=Welcome(root)
root.mainloop()
        
