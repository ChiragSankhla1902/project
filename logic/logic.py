import os.path
from  tkinter import *
import csv
import glob
import pandas as pd

#-------------------------------------database----------------------------------------------------------------
# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',database='mysql',user='root',password='password')
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)
# mydb.commit()
# mycursor.execute("SELECT * FROM customers")
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)
#---------------------------------------------------------------------------------------------------------------
#----------------------Saving path,name and data to file---------------
save_path = (r"C:\Users\Chirag\Documents\Python Scripts\ex")
E:\project
name_of_file = input("What is the name of the file: ")
completeName = os.path.join(save_path, name_of_file+".csv")
data=pd.read_csv(completeName,index_col="Name")
a=input("Enter Name")
# b=input("Enter Branch")
# c=input("Enter Year")
# d=input("Enter CGPA")

# data.drop(a, inplace = True)
# fields = ['Name', 'Branch', 'Year', 'CGPA']
# rows = [[str(a),str(b),str(c),str(d)]]
# print(rows)
# print(rows[0][0])
# with open(completeName, 'r',newline="") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
        # if(row[0]==a):
        #     with open(completeName,'a',newline="")as csvfile:
        #         csvwriter=csv.writer(csvfile)
        #         csvwriter.writerow(rows)
# with open(completeName, 'a+',newline="") as csvfile:
#     csvwriter = csv.writer(csvfile)
#     # if(row[])
# #     csvwriter.writerow(fields)
#     csvwriter.writerows(rows)


#--------------------------------selecting particular column-----------------------------------------
# data=pd.read_csv(r"C:\Users\Chirag\Documents\Python Scripts\ex\First1.csv", usecols = ['Name','CGPA'])
#---------------------------------------selecting displaying on particular condition--------------------
# data=pd.read_csv(r"C:\Users\Chirag\Documents\Python Scripts\ex\First1.csv")
# data=data[data["CGPA"]<="9.0"]
# print(data)

#-----------------------------printing data of all the file present in a given folder--------------
# def openfile(str):
#     save_path = (r"C:\Users\Chirag\Documents\Python Scripts\ex")
#     complete=os.path.join(save_path,str)
#     data=pd.read_csv(complete)
#     print(data)
#
# for files in os.listdir(r"C:\Users\Chirag\Documents\Python Scripts\ex"):
#     openfile(files)

# root=Tk()
# Agency=StringVar()
# Medicine=StringVar()
# Agency_label=Label(root,text="Agency",font=("Arial",20),bg="#605DE2",fg="White")
# Agency_label.grid(row=1,column=0,pady=10,padx=10,sticky="w")
# #------entry-------
# Agency_name=Entry(root,textvariable=Agency,font=("Arial",15),bg="White",fg="Black",relief="flat",bd=0)
# Agency_name.grid(row=1,column=1,pady=12,padx=10)
# # Agency_name.bind("<FocusIn>",on_enter2)
# # Agency_name.bind("<FocusOut>",on_leave2)
# #--------medicine-------------
# Medicine_label=Label(root,text="Medicine",font=("Airal",20),bg="#605DE2",fg="White")
# Medicine_label.grid(row=2,column=0,pady=10,padx=10,sticky="w")
# #-------entry-------------------
# Medicine_name=Entry(root,font=("Dubai",15),bg="White",textvariable=Medicine,fg="Black",relief="flat",bd=0)
# Medicine_name.grid(row=2,column=1,pady=12,padx=10)
# # Medicine_name.bind("<FocusIn>",on_enter6)
# # Medicine_name.bind("<FocusOut>",on_leave6)
# root.mainloop()


