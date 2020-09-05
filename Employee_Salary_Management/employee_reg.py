# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 20:52:58 2020

@author: jaity banerjee
"""

from tkinter.ttk import *
from tkinter import *
import mysql.connector
from tkinter import messagebox
import os 

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="employee"
)
mycursor=mydb.cursor()
root = Tk()
v=StringVar()


root.configure(bg="skyBlue")
root.geometry("900x400")

root.title("Employee Details")

Label(root, text="Registration Form",fg="Black",bg="skyblue",font=('times',15,"bold")).grid(row=0,column=2)

Label(root, text="EmployeeID",fg="Black",bg="skyblue",font=('times',10,"bold")).grid(row=1,column=0)
e1 = Entry(root,fg="black",bg="lightpink")
e1.grid(row=1, column=1,ipadx=70,ipady=5,pady=10)

Label(root, text="First_Name",fg="Black",bg="skyblue",font=('times',10,"bold")).grid(row=2,column=0)
e2 = Entry(root,fg="black",bg="lightpink")
e2.grid(row=2, column=1,ipadx=70,ipady=5,pady=10)

Label(root, text="Last_Name",fg="Black",bg="skyblue",font=('times',10,"bold")).grid(row=3,column=0)
e3 = Entry(root,fg="black",bg="lightpink")
e3.grid(row = 3, column = 1,ipadx=70,ipady=5,pady=10)

Label(root, text="Address",fg="Black",bg="skyblue",font=('times',10,"bold")).grid(row=4,column=0)
e4 = Entry(root,fg="black",bg="lightpink")
e4.grid(row = 4, column=1,ipadx=70,ipady=5,pady=10);

Label(root, text="Adhar_Number",fg="Black",bg="skyblue",font=('times',10,"bold")).grid(row=5,column=0)
e5 = Entry(root,fg="black",bg="lightpink")
e5.grid(row = 5, column=1,ipadx=70,ipady=5,pady=10);

Label(root, text="Password",fg="Black",bg="skyblue",font=('times',10,"bold")).grid(row=6,column=0)
e6 = Entry(root,fg="black",bg="lightpink")
e6.grid(row = 6, column=1,ipadx=70,ipady=5,pady=10);

Label(root, text="Gender",fg="Black",bg="skyblue",font=('times',10,"bold"),pady=10).grid(row=7,column=0)
rd = Radiobutton(root, text = "MALE",variable=v,fg="Black",bg="skyblue",value="Male",font=('times',10,"bold"))
rd.grid(row=7,column=1,pady=10)
rd2 = Radiobutton(root, text = "FEMALE",variable=v,fg="Black",bg="skyblue",value="Female",font=('times',10,"bold"))
rd2.grid(row=7,column=2,pady=10)

Label(root, text="Qualification",fg="Black",bg="skyblue",font=('times',10,"bold")).grid(row=8,column=0)
e7 = Entry(root,fg="black",bg="lightpink")
e7.grid(row=8, column=1,ipadx=70,ipady=5,pady=10)

Label(root, text="Skills",fg="Black",bg="skyblue",font=('times',10,"bold")).grid(row=9,column=0)
e8 = Entry(root,fg="black",bg="lightpink")
e8.grid(row=9, column=1,ipadx=70,ipady=5,pady=10)

Label(root, text="Experience",fg="Black",bg="skyblue",font=('times',10,"bold"),pady=10).grid(row=10,column=0)
mline = Text(root,height=6,width=50,fg="black",bg="lightpink")
mline.grid(row=10,column=1,pady=30,padx=50)


def Submit():
    EmployeeID=e1.get()
    dbEmployeeID=""
    Select="select EmployeeID from student where EmployeeID='%s'" %(EmployeeID)
    mycursor.execute(Select)
    result=mycursor.fetchall()
    for i in result:
        dbEmployeeID=i[0]
    if(EmployeeID == dbEmployeeID):
        messagebox.askokcancel("Information","Record Already exists")
    else:
        Insert="Insert into student(EmployeeID,First_Name,Last_Name,Address,Adhar_Number,Password,Gender,Qualification,Skills,Experience) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        First_Name=e2.get()
        Last_Name=e3.get()
        Address=e4.get()
        Adhar_Number=e5.get()
        Password=e6.get()
        Gender=v.get()
        Qualification=e7.get()
        Skills=e8.get()
        Experience=mline.get(1.0,END)
        if(EmployeeID !="" and First_Name !="" and Last_Name !="" and Address !="" and Adhar_Number !="" and Password !="",Gender !="",Qualification !="",Skills !="",Experience !=""):
            Value=(EmployeeID,First_Name,Last_Name,Address,Adhar_Number,Password,Gender,Qualification,Skills,Experience)
            mycursor.execute(Insert,Value)
            mydb.commit()
            messagebox.askokcancel("Information","Record inserted")
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)
            v.set(0)
            e7.delete(0, END)
            e8.delete(0, END)
            mline.delete('1.0',END)
        else:
            if (First_Name == "" and Last_Name == "" and Address == "" and Adhar_Number == "" and Password == "" and Gender == "" and Qualification == "" and Skills == "" and Experience == ""):
             messagebox.askokcancel("Information","New Entery Fill All Details")
            else:
             messagebox.askokcancel("Information", "Some fields left blank")
              
                      
             
def callNextScreen():
    root.destroy()
    os.system("python Company.py")
    
def Clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    v.set(0)
    e7.delete(0, END)
    e8.delete(0, END)
    mline.delete('1.0',END)


btn1 = Button(root, text = "Submit",fg="Black",bg="green",font=('times',10,"bold"),command=Submit)
btn1.grid(row=20,column=0)
btn2 = Button(root, text = "Clear",fg="Black",bg="orange",font=('times',10,"bold"),command=Clear)
btn2.grid(row=20,column=1)
btn3 = Button(root, text = "Login",fg="Black",bg="violet",font=('times',10,"bold"),command=callNextScreen)
btn3.grid(row=20,column=2)
btn4 = Button(root, text = "Cancel",fg="Black",bg="Red",command=root.destroy,font=('times',10,"bold"))
btn4.grid(row=20,column=4,padx=40)


root.mainloop()
