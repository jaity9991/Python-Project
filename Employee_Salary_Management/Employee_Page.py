# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 14:23:27 2020

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
root.configure(bg="orange")
root.geometry("780x380")
root.resizable(False,False)
root.title("Welcome Employee")

Label(root, text="(: Welcome to your Page :)",fg="Black",bg="orange",font=('times',25,"bold","italic")).grid(row=1,column=2)
Label(root, text="---------Review Your Details--------- ",fg="Royal blue",bg="orange",font=('times',15)).grid(row=2,column=2,padx=30)

Label(root, text="<<<<------Click There------>>>> ",fg="#003333",bg="Orange",font=('Times New roman',10,"bold")).grid(row=3,column=2)
Label(root, text="Your work rate is Fantastic! ",fg="black",bg="Orange",font=('times',10)).grid(row=11,column=2)
Label(root, text="You are Doing great work-Keep it Up!",fg="black",bg="Orange",font=('times',10)).grid(row=12,column=2)
Label(root, text="**Don't Settle for Average When You are Capable of Being Awsome**",fg="DarkRed",bg="Orange",font=('times',10,"italic")).grid(row=13,column=2)



    
def show():
    class B:
        def __init__(self,root):
            self.root=root
            self.root.title("REGISTRATION FORM VIEW")
            self.root.geometry("1199x600+200+60")
            self.root.configure(bg="SkyBlue")
            
            Label(root, text="Registration Form",fg="Black",bg="skyblue",font=('times',15,"bold")).grid(row=0,column=2)

            Label(root, text="EmployeeID",fg="Black",bg="skyblue",font=('times',10,"bold")).grid(row=1,column=0)
            e1 = Entry(root,fg="black",bg="lightpink")
            e1.grid(row=1, column=1,ipadx=70,ipady=5,pady=5)
            
            Label(root, text="First_Name",fg="Black",bg="skyblue",font=('times',10,"bold")).grid(row=2,column=0)
            e2 = Entry(root,fg="black",bg="lightpink")
            e2.grid(row=2, column=1,ipadx=70,ipady=5,pady=5)
            
            Label(root, text="Last_Name",fg="Black",bg="skyblue",font=('times',10,"bold")).grid(row=3,column=0)
            e3 = Entry(root,fg="black",bg="lightpink")
            e3.grid(row = 3, column = 1,ipadx=70,ipady=5,pady=5)
            
            Label(root, text="Address",fg="Black",bg="skyblue",font=('times',10,"bold")).grid(row=4,column=0)
            e4 = Entry(root,fg="black",bg="lightpink")
            e4.grid(row = 4, column=1,ipadx=70,ipady=5,pady=5);
            
            Label(root, text="Adhar_Number",fg="Black",bg="skyblue",font=('times',10,"bold")).grid(row=5,column=0)
            e5 = Entry(root,fg="black",bg="lightpink")
            e5.grid(row = 5, column=1,ipadx=70,ipady=5,pady=5);
            
            Label(root, text="Password",fg="Black",bg="skyblue",font=('times',10,"bold")).grid(row=6,column=0)
            e6 = Entry(root,fg="black",bg="lightpink")
            e6.grid(row = 6, column=1,ipadx=70,ipady=5,pady=5);
            
            Label(root, text="Gender",fg="Black",bg="skyblue",font=('times',10,"bold"),pady=10).grid(row=7,column=0)
            v =Entry(root,fg="black",bg="lightpink")
            v.grid(row=7,column=1,ipady=5,ipadx=70,pady=5)
            
            Label(root, text="Qualification",fg="Black",bg="skyblue",font=('times',10,"bold")).grid(row=8,column=0)
            e7 = Entry(root,fg="black",bg="lightpink")
            e7.grid(row=8, column=1,ipadx=70,ipady=5,pady=5)
            
            Label(root, text="Skills",fg="Black",bg="skyblue",font=('times',10,"bold")).grid(row=9,column=0)
            e8 = Entry(root,fg="black",bg="lightpink")
            e8.grid(row=9, column=1,ipadx=70,ipady=5,pady=5)
            
            Label(root, text="Experience",fg="Black",bg="skyblue",font=('times',10,"bold"),pady=10).grid(row=10,column=0)
            mline = Text(root,height=6,width=50,fg="black",bg="lightpink")
            mline.grid(row=10,column=1,padx=30)

            
            Label(root,text="Salary",fg="black",bg="skyblue",font=('times',10,"bold"),pady=10).grid(row=11,column=0)
            e10 = Entry(root,fg="black",bg="lightpink")
            e10.grid(row=11,column=1,ipadx=70,ipady=5)
            Label(root,text="Overtime",fg="black",bg="skyblue",font=('times',10,"bold"),pady=10).grid(row=12,column=0,pady=15)
            e11 = Entry(root,fg="black",bg="lightpink")
            e11.grid(row=12,column=1,ipadx=70,ipady=5)
            Label(root,text="Date_of_Salary",fg="black",bg="skyblue",font=('times',10,"bold"),pady=10).grid(row=13,column=0,pady=15)
            e12 = Entry(root,fg="black",bg="lightpink")
            e12.grid(row=13,column=1,ipadx=70,ipady=5)
            def view():
                EmployeeID=e1.get()
                dbEmployeeID=""
                Select="select EmployeeID from student where EmployeeID='%s'" %(EmployeeID)
                mycursor.execute(Select)
                result1=mycursor.fetchall()
                print(result1)
                for i in result1:
                    dbEmployeeID=i[0]
                Select1="""Select First_Name,Last_Name,Address,Adhar_Number,Password,Gender,Qualification,Skills,
                Experience,Salary,Overtime,Date_of_Salary from student where EmployeeID='%s'""" %(EmployeeID)
                mycursor.execute(Select1)
                result2=mycursor.fetchall()
                print(result2)
                First_Name=""
                Last_Name=""
                Address=""
                Adhar_Number=""
                Password=""
                Gender=""
                Qualification=""
                Skills=""
                Experience=""
                Salary=""
                Overtime=""
                Date_of_Salary=""
                if(EmployeeID == str(dbEmployeeID)):
                    for i in result2:
                        First_Name=i[0]
                        Last_Name=i[1]
                        Address=i[2]
                        Adhar_Number=i[3]
                        Password=i[4]
                        Gender=i[5]
                        Qualification=i[6]
                        Skills=i[7]
                        Experience=i[8]
                        Salary=i[9]
                        Overtime=i[10]
                        Date_of_Salary=i[11]
                    e2.insert(0, First_Name)
                    e3.insert(0, Last_Name)
                    e4.insert(0, Address)
                    e5.insert(0, Adhar_Number)
                    e6.insert(0, Password)
                    v.insert(0, Gender)
                    e7.insert(0, Qualification)
                    e8.insert(0, Skills)
                    mline.insert(1.0, Experience)
                    e10.insert(0, Salary)
                    e11.insert(0, Overtime)
                    e12.insert(0, Date_of_Salary)
                else:
                    messagebox.showerror("ERROR","No Record Exists",parent=self.root)
                    
            
            
            def update():
                EmployeeID=e1.get()
                First_Name=e2.get()
                Last_Name=e3.get()
                Address=e4.get()
                Adhar_Number=e5.get()
                Password=e6.get()
                Gender=v.get()
                Qualification=e7.get()
                Skills=e8.get()
                Experience=mline.get(1.0,END)
                Update="Update student set First_Name='%s', Last_Name='%s', Address='%s', Adhar_Number='%s', Password='%s', Gender='%s', Qualification='%s', Skills='%s', Experience='%s' where EmployeeID='%s'" %(First_Name,Last_Name,Address,Adhar_Number,Password,Gender,Qualification,Skills,Experience,EmployeeID)
                mycursor.execute(Update)
                mydb.commit()
                if(EmployeeID==""):
                    messagebox.showerror("ERROR","Fill Details",parent=self.root)
                else:
                    messagebox.showinfo("INFORMATION","Record Updated",parent=self.root)
            def delete():
                EmployeeID=e1.get()
                Delete="delete from student where EmployeeID='%s'" %(EmployeeID)
                mycursor.execute(Delete)
                mydb.commit()
                if(EmployeeID==""):
                    messagebox.showerror("ERROR","Fill Details",parent=self.root)
                else:
                    messagebox.showinfo("INFORMATION","Record Deleted",parent=self.root)
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e6.delete(0, END)
                v.delete(0,END)
                e7.delete(0, END)
                e8.delete(0, END)
                mline.delete('1.0',END)
    
                
            btn=Button(self.root,text="View",fg="Black",bg="Darkviolet",font=("Bahnschrift",14),width=10,command=view,).grid(row=5,column=2)
            btn3= Button(self.root,text = "Update",fg="White",bg="#d77337",font=("Bahnschrift",14),width=10,command=update).grid(row=7,column=2)
            btn5= Button(self.root,text = "Delete",fg="White",bg="#778899",font=("Bahnschrift",14),width=10,command=delete).grid(row=9,column=2)
            btn6= Button(self.root,text = "Cancel",fg="White",bg="#CD5C5C",font=("Bahnschrift",14),width=10,command=self.root.destroy).grid(row=10,column=2)
    root=Tk()
    ob=B(root)
    root.mainloop()

 

btn1=Button(root,text = "ShowRecord",fg="White",bg="#336656",font=("Bahnschrift",14),width=10,command=show)
btn1.grid(row=6,column=1,pady=30,padx=40)
btn4= Button(root,text="Cancel",fg="white",bg="#FF0000",font=("Bahnschrift",14),width=10,command=root.destroy)
btn4.grid(row=6,column=3,pady=30)

root.mainloop()