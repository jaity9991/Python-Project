# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 20:12:00 2020

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
root.configure(bg="skyBlue")
root.geometry("900x400")
root.title("Employee_Salary_Update")

Label(root, text="Salary Update",fg="Black",bg="skyblue",font=('Sans serif',25,"bold")).grid(row=0,column=3)
Label(root, text="EmployeeID",fg="Black",bg="skyblue",font=('times',10,"bold")).grid(row=1,column=0)
e1 = Entry(root,fg="black",bg="lightpink")
e1.grid(row=1, column=1,ipadx=70,ipady=5,pady=10)




Label(root, text="Salary",fg="Black",bg="skyblue",font=('times',10,"bold")).grid(row=3,column=0)
e9 = Entry(root,fg="black",bg="lightpink")
e9.grid(row=3, column=1,ipadx=70,ipady=5,pady=10)

Label(root, text="Overtime",fg="Black",bg="skyblue",font=('times',10,"bold")).grid(row=4,column=0)
e10 = Entry(root,fg="black",bg="lightpink")
e10.grid(row = 4, column = 1,ipadx=70,ipady=5,pady=10)


Label(root, text="Date_Of_Salary",fg="Black",bg="skyblue",font=('times',10,"bold")).grid(row=5,column=0)
e11 = Entry(root,fg="black",bg="lightpink")
e11.grid(row = 5, column=1,ipadx=70,ipady=5,pady=10);




def Showall():
    class A(Frame):
        def __init__(self, parent):
            Frame.__init__(self, parent)
            self.CreateUI()
            self.LoadTable()
            self.grid(sticky=(N, S, W, E))
            parent.grid_rowconfigure(0, weight=1)
            parent.grid_columnconfigure(0, weight=1)
        def CreateUI(self):
            tv= Treeview(self)
            tv.place(x=30, y=200)
            tv['columns']=('EmployeeID','First_Name', 'Last_Name','Address', 'Adhar_Number', 'Password', 'Gender','Qualification','Skills','Experience')
            tv.heading('#0',text='EmployeeID',anchor='center')
            tv.column('#0',anchor='center')
            tv.heading('#1', text='First_Name', anchor='center')
            tv.column('#1', anchor='center')
            tv.heading('#2', text='Last_Name', anchor='center')
            tv.column('#2', anchor='center')
            tv.heading('#3', text='Address', anchor='center')
            tv.column('#3', anchor='center')
            tv.heading('#4', text='Adhar_Number', anchor='center')
            tv.column('#4', anchor='center')
            tv.heading('#5', text='Password', anchor='center')
            tv.column('#5', anchor='center')
            tv.heading('#6',text='Gender', anchor='center')
            tv.column('#6', anchor='center')
            tv.heading('#7', text='Qualification', anchor='center')
            tv.column('#7', anchor='center')
            tv.heading('#8', text='Skills', anchor='center')
            tv.column('#8', anchor='center')
            tv.heading('#9', text='Experience', anchor='center')
            tv.column('#9', anchor='center')
            tv.grid(sticky=(N,S,W,E))
            self.treeview = tv
            self.grid_rowconfigure(0,weight=1)
            self.grid_columnconfigure(0,weight=1)
        def LoadTable(self):
            
            EmployeeID=e1.get()
            dbEmployeeID=""
            Select="Select * from student where EmployeeID='%s'"%(EmployeeID)
            mycursor.execute(Select)
            result=mycursor.fetchall()
            EmployeeID=""
            First_Name=""
            Last_Name=""
            Address=""
            Adhar_Number=""
            Password=""
            Gender=""
            Qualification=""
            Skills=""
            Experience=""
            
            for i in result:
                EmployeeID=i[0]
                First_Name=i[1]
                Last_Name=i[2]
                Address=i[3]
                Adhar_Number=i[4]
                Password=i[5]
                Gender=i[6]
                Qualification=i[7]
                Skills=i[8]
                Experience=i[9]
                self.treeview.insert("",'end',text=EmployeeID,values=(First_Name,Last_Name,Address,Adhar_Number,Password,Gender,Qualification,Skills,Experience))
    
    root=Tk()
    root.title("Overview Page")
    A(root)
    
def Reg():
    EmployeeID=e1.get()
    
    Salary=e9.get()
    Overtime=e10.get()
    Date_of_Salary=e11.get()
    
    Update="Update student set Salary='%s', Overtime='%s', Date_of_Salary='%s' where EmployeeID='%s' " %(Salary,Overtime,Date_of_Salary,EmployeeID)
        
    
    mycursor.execute(Update)
    mydb.commit()
    messagebox.showinfo("Info","Record Registered")
    e1.delete(0, END)
    e9.delete(0, END)
    e10.delete(0, END)
    e11.delete(0, END)
            
              
btn1=Button(root,text = "Show",fg="Black",bg="Darkviolet",font=('times',10,"bold"),command=Showall)
btn1.grid(row=1,column=2,padx=40)

btn2=Button(root,text = "Register",fg="Black",bg="Yellow",font=('times',10,"bold"),command=Reg)
btn2.grid(row=5,column=2,padx=40)

root.mainloop()