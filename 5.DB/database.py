import pymysql
from tkinter import *
root=Tk()
root.title("Database")
root.geometry('{}x{}'.format(1920, 1080))
db=pymysql.connect(host="Localhost",user="",password="")
cursor=db.cursor()
try:
    cursor.execute("CREATE DATABASE College_database_management")
except :
    print("Database already exists")

finally:
    db.select_db("College_database_management")
    try:
        cursor.execute("CREATE TABLE Student(s_id INT PRIMARY KEY,s_name VARCHAR(200) NOT NULL,s_address VARCHAR(250) NOT NULL,birth_date DATE,gender VARCHAR(10))")
        cursor.execute("CREATE TABLE Course(c_id INT PRIMARY KEY,c_name VARCHAR(200) NOT NULL,c_code INT)")
        cursor.execute("CREATE TABLE Faculty(f_id INT PRIMARY KEY,f_name VARCHAR(200) NOT NULL,age INT,gender VARCHAR(10) NOT NULL,experience VARCHAR(25) NOT NULL,salary NUMERIC NOT NULL)")
        cursor.execute("CREATE TABLE Research_project(p_id INT PRIMARY KEY,p_name VARCHAR(200) NOT NULL,duration Varchar(25))")
        cursor.execute("CREATE TABLE Department(d_id INT PRIMARY KEY,d_name VARCHAR(200) NOT NULL)")
    except :
        print("Table already exists")
    finally:
        print("OK")

#GUI
#global var


def ins_value():
    s1=e1.get()
    s2=e2.get()
    s3=e3.get()
    s4=e4.get()
    s5=e5.get()
    


    db.select_db("College_database_management")

    query="INSERT INTO Student(s_id,s_name,s_address,birth_date,gender) VALUES(%s,%s,%s,%s,%s)"
    insert=(s1,s2,s3,s4,s5)
    cursor.execute(query,insert)
    db.commit()

def c_ins():
    c1=e6.get()
    c2=e7.get()
    c3=e8.get()
    db.select_db("College_database_management")

    query="INSERT INTO Course(c_id,c_name,c_code) VALUES(%s,%s,%s)"

    insert=(c1,c2,c3)
    cursor.execute(query,insert)
    db.commit()

def f_ins():
    f1=e9.get()
    f2=e10.get()
    f3=e11.get()
    f4=e12.get()
    f5=e13.get()
    f6=e14.get()
    db.select_db("College_database_management")

    query="INSERT INTO Faculty(f_id,f_name,age,gender,experience,salary) VALUES(%s,%s,%s,%s,%s,%s)"


    insert=(f1,f2,f3,f4,f5,f6)
    cursor.execute(query,insert)
    db.commit()

def p_ins():
    p1=e15.get()
    p2=e16.get()
    p3=e17.get()
    db.select_db("College_database_management")

    query="INSERT INTO Research_project(p_id,p_name,duration) VALUES(%s,%s,%s)"

    insert=(p1,p2,p3)
    cursor.execute(query,insert)
    db.commit()

def dept_ins():
    d1=e18.get()
    d2=e19.get()
    
    db.select_db("College_database_management")

    query="INSERT INTO Department(d_id,d_name,duration) VALUES(%s,%s)"

    insert=(d1,d2)
    cursor.execute(query,insert)
    db.commit()



#widgets
#student
l1=Label(root,text="Student Id:-").grid(row=0)
l2=Label(root,text="Student Name:-").grid(row=1)
l3=Label(root, text="Student Address:-").grid(row=2)
l4=Label(root,text="Birth Date:-").grid(row=3)
l5=Label(root,text="Gender:-").grid(row=4)

#course
l6=Label(root,text="Course Id:-").grid(row=0,column=2)
l7=Label(root,text="Course Name:-").grid(row=1,column=2)
l8=Label(root, text="Course Code:-").grid(row=2,column=2)

#faculty
l9=Label(root, text="Faculty Id:-").grid(row=0,column=4)
l10=Label(root, text="Faculty Name:-").grid(row=1,column=4)
l11=Label(root, text="Age:-").grid(row=2,column=4)
l12=Label(root, text="Gender:-").grid(row=3,column=4)
l13=Label(root, text="Experience:-").grid(row=4,column=4)
l14=Label(root, text="Salary:-").grid(row=5,column=4)

#research proj
l15=Label(root,text="Project Id:-").grid(row=0,column=6)
l16=Label(root,text="Project Name:-").grid(row=1,column=6)
l17=Label(root,text="Duration:-").grid(row=2,column=6)

#dept 
l15=Label(root,text="Department Id:-").grid(row=0,column=8)
l16=Label(root,text="Department Name:-").grid(row=1,column=8)



#entry students
#student
e1=Entry(root)
e2=Entry(root)
e3=Entry(root)
e4=Entry(root)
e5=Entry(root)

#course
e6=Entry(root)
e7=Entry(root)
e8=Entry(root)

#faculty
e9=Entry(root)
e10=Entry(root)
e11=Entry(root)
e12=Entry(root)
e13=Entry(root)
e14=Entry(root)

#proj
e15=Entry(root)
e16=Entry(root)
e17=Entry(root)

#dept
e18=Entry(root)
e19=Entry(root)





#layout
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
e4.grid(row=3,column=1)
e5.grid(row=4,column=1)

e6.grid(row=0,column=3)
e7.grid(row=1,column=3)
e8.grid(row=2,column=3)
e9.grid(row=0,column=5)
e10.grid(row=1,column=5)
e11.grid(row=2,column=5)
e12.grid(row=3,column=5)
e13.grid(row=4,column=5)
e14.grid(row=5,column=5)

e15.grid(row=0,column=7)
e16.grid(row=1,column=7)
e17.grid(row=2,column=7)

e18.grid(row=0,column=9)
e19.grid(row=1,column=9)





#buttons
b1=Button(root,text="Submit",command=ins_value)
b2=Button(root,text="Submit",command=c_ins)
b3=Button(root,text="Submit",command=f_ins)
b4=Button(root,text="Submit",command=p_ins)
b5=Button(root,text="Submit",command=dept_ins)
b6=Button(root,text="Exit",command=root.destroy)



b1.grid(row=6,column=1)
b2.grid(row=6,column=3)
b3.grid(row=6,column=5)
b4.grid(row=6,column=7)
b5.grid(row=6,column=9)
b6.grid(row=15,column=5)

root.mainloop()

