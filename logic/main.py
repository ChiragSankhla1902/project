from tkinter import *
from tkinter import ttk
import os
from tkinter import messagebox
import mysql.connector
import csv

#use root=Toplevel() if u want to open it using another program
root=Tk()
root.title("Vijay Medical Palace")
root.geometry("1500x800")
root.minsize(1000,700)


#-----------------------Heading----------------------------------
def act(e):
    rows=main_tabel.focus()
    content=main_tabel.item(rows)
    row=content["values"]
    Agency.set(row[0])
    Medicine.set(row[1])
    Billno.set(row[2])
    Exp.set(row[3])
    Batch.set(row[4])
    rate.set(row[5])
    quantity.set(row[6])
    Id.set(row[7])
    Date.set(row[-1])
def update():
    mydb = mysql.connector.connect(host="localhost", user="root", database="FIRST", password="password")
    mycursor = mydb.cursor()
    mycursor.execute("Update First8 SET Agency=%s,Medicine=%s,Batch=%s,Rate=%s,Quantity=%s,Expiry=%s,Date=%s,Billno=%s WHERE Id=%s",(Agency_name.get(),Medicine_name.get(),Batch_name.get(),rate_name.get(),quantity_name.get(),Exp_name.get(),Date_name.get(),Billno_name.get(),Id.get()))
    mydb.commit()
    show()
    reset()
    mydb.close()
def submit():
    if(Agency_name.get()!="" and Medicine_name.get()!="" and Exp_name.get()!="" and Date_name.get()!="" and Billno_name.get()!=" "):
        mydb = mysql.connector.connect(host="localhost", user="root", database="FIRST", password="password")
        mycursor = mydb.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS First8 (Id int(16) auto_increment,Agency VARCHAR(255), Medicine VARCHAR(255),Batch VARCHAR(255),Rate VARCHAR(255),Quantity VARCHAR(255),Expiry DATE,DATE DATE,Billno Varchar(255),PRIMARY KEY (Id))")

        sql = "INSERT INTO First8 (Agency,Medicine,Batch,Rate,Quantity,Expiry,DATE,Billno) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)"
        val=(Agency_name.get(),Medicine_name.get(),Batch_name.get(),rate_name.get(),quantity_name.get(),Exp_name.get(),Date_name.get(),Billno_name.get())
        mycursor.execute(sql,val)
        mydb.commit()
        #--------------------In CSV File---------------------------------------------------------
        a=Agency_name.get()
        b=Medicine_name.get()
        c=Batch_name.get()
        d=rate_name.get()
        e=quantity_name.get()
        f=Exp_name.get()
        g=Date_name.get()
        h=Billno_name.get()
        i=Id.get()
        mydb.close()
        show()
        messagebox.showinfo("Success","inserted successfully")
        reset()
        save_path = (r"E:\project")
        completeName = os.path.join(save_path,a+".csv")
        rows = [str(a),str(b),str(c),str(d),str(e),str(f),str(g),str(h),str(i)]
        with open(completeName, 'a+', newline="") as csvfile:
            csvwriter=csv.writer(csvfile)
            csvwriter.writerow(rows)
    else:
        messagebox.showerror("Error","input all the field")

def delete_entry():
    mydb = mysql.connector.connect(host="localhost", user="root", database="FIRST", password="password")
    mycursor = mydb.cursor()
    a=Id.get()
    mycursor.execute("DELETE FROM First8 WHERE Id=%d"%a)
    mydb.commit()
    mydb.close()
    show()

def searching():
    mydb = mysql.connector.connect(host="localhost", user="root", database="FIRST", password="password")
    mycursor = mydb.cursor()
    if(search_by.get()=="Batch"):
        b=search_txt.get()
        sql="SELECT Agency,Medicine,Billno,Expiry,Batch,Rate,Quantity,Id,DATE FROM First8 WHERE Batch = %s"
        name=(b,)
        mycursor.execute(sql,name)
        rows = mycursor.fetchall()
        if len(rows)!=0:
            main_tabel.delete(*main_tabel.get_children())
            for row in rows:
                main_tabel.insert("",END,values=row)
        mydb.close()

    elif(search_by.get()=="Medicine"):
        b=search_txt.get()
        sql="SELECT Agency,Medicine,Billno,Expiry,Batch,Rate,Quantity,Id,DATE FROM First8 WHERE Medicine = %s"
        name=(b,)
        mycursor.execute(sql,name)
        rows = mycursor.fetchall()
        if len(rows)!=0:
            main_tabel.delete(*main_tabel.get_children())
            for row in rows:
                main_tabel.insert("",END,values=row)
        mydb.close()

    elif(search_by.get()=="Expiry"):
        b=search_txt.get()
        sql="SELECT Agency,Medicine,Billno,Expiry,Batch,Rate,Quantity,Id,DATE FROM First8 WHERE Expiry <= %s"
        name=(b,)
        mycursor.execute(sql,name)
        rows = mycursor.fetchall()
        if len(rows)!=0:
            main_tabel.delete(*main_tabel.get_children())
            for row in rows:
                main_tabel.insert("",END,values=row)
        mydb.close()
    mydb.commit()
    reset()
    mydb.close()

def show():
    mydb = mysql.connector.connect(host="localhost", user="root", database="FIRST", password="password")
    mycursor = mydb.cursor()
    mycursor.execute("select Agency,Medicine,Billno,Expiry,Batch,Rate,Quantity,Id,DATE from First8")
    rows=mycursor.fetchall()
    if len(rows)!=0:
        main_tabel.delete(*main_tabel.get_children())
        for row in rows:
            main_tabel.insert("",END,values=row)
    mydb.close()
    reset()

#------------------------------------events function--------------------------------------------------------------
def on_enter(e):
    f1["bg"]="#3EAFD2"
    header["bg"]="#3EAFD2"
    header["fg"]="Black"
def on_enter1(e):
    Date_name["relief"]="solid"
    Date_name["bd"]="2"
def on_enter2(e):
    Agency_name["relief"]="solid"
    Agency_name["bd"]="2"
def on_enter3(e):
    Exp_name["relief"]="solid"
    Exp_name["bd"]="2"
def on_enter4(e):
    quantity_name["relief"]="solid"
    quantity_name["bd"]="2"
def on_enter5(e):
    rate_name["relief"]="solid"
    rate_name["bd"]="2"
def on_enter6(e):
    Medicine_name["relief"]="solid"
    Medicine_name["bd"]="2"
def on_enter7(e):
    Batch_name["relief"]="solid"
    Batch_name["bd"]="2"
def on_enter8(e):
    Billno_name["relief"]="solid"
    Billno_name["bd"]="2"


def up1(e):
    Date_name.focus_set()
def down1(e):
    Medicine_name.focus_set()
def up2(e):
    Agency_name.focus_set()
def down2(e):
    quantity_name.focus_set()
def up3(e):
    Medicine_name.focus_set()
def down3(e):
    Batch_name.focus_set()
def up4(e):
    quantity_name.focus_set()
def down4(e):
    rate_name.focus_set()
def up5(e):
    Batch_name.focus_set()
def down5(e):
    Exp_name.focus_set()
def up6(e):
    rate_name.focus_set()
def down6(e):
    Date_name.focus_set()
def up7(e):
    Exp_name.focus_set()
def down7(e):
    Billno_name.focus_set()
def down8(e):
    Agency_name.focus_set()
def up8(e):
    Date_name.focus_set()

def next1(e):
    Medicine_name.focus_set()
def next2(e):
    quantity_name.focus_set()
def next3(e):
    Batch_name.focus_set()
def next4(e):
    rate_name.focus_set()
def next5(e):
    Exp_name.focus_set()
def next6(e):
    Date_name.focus_set()
def next7(e):
    Billno_name.focus_set()
def next8(e):
    Agency_name.focus_set()

def on_leave(e):
    f1["bg"]="#605DE2"
    header["bg"]="#605DE2"
    header["fg"]="White"
def on_leave1(e):
    Date_name["relief"]="flat"
    Date_name["bd"]="0"
def on_leave2(e):
    Agency_name["relief"]="flat"
    Agency_name["bd"]="0"
def on_leave3(e):
    Exp_name["relief"]="flat"
    Exp_name["bd"]="0"
def on_leave4(e):
    quantity_name["relief"]="flat"
    quantity_name["bd"]="0"
def on_leave5(e):
    rate_name["relief"]="flat"
    rate_name["bd"]="0"
def on_leave6(e):
    Medicine_name["relief"]="flat"
    Medicine_name["bd"]="0"
def on_leave7(e):
    Batch_name["relief"]="flat"
    Batch_name["bd"]="0"
def on_leave8(e):
    Billno_name["relief"]="flat"
    Billno_name["bd"]="0"
#------------------------------------------------------------------------------------------------------------------








#--------------------------Button logic-----------------------------------------------------------------------------
def reset():
    Agency.set("")
    Batch.set("")
    Medicine.set("")
    rate.set("")
    Exp.set("")
    quantity.set("")
    Date.set("")
    Billno.set("")

#------------------------------------------------------------------------------------------------------------------

#-----------------------------------Variable------------------------------------------------------------------------
Agency=StringVar()
Batch=StringVar()
Medicine=StringVar()
rate=IntVar()
Date=IntVar()
Exp=IntVar()
quantity=IntVar()
search_by=StringVar()
search_txt=StringVar()
Billno=StringVar()
Id=IntVar()


#---------------------------------------------------------Main function-------------------------------------------------
f1=Frame(root,bg="#605DE2",borderwidth=2, relief=SUNKEN)
header=Label(f1,text="Entery Software",bg="#605DE2",font=("Arial",22,"bold"),pady=10,fg="White")
f1.pack(side=TOP,fill="x")
header.pack()
f1.bind("<Enter>",on_enter)
f1.bind("<Leave>",on_leave)
#--------------------------------------frame--------------------------------
f2=Frame(root,bg="#605DE2",pady=20)
f2.place(x=15,y=70,width=450,height=700)
title=Label(f2,text="Entery",font=("Arial",25),bg="#605DE2",fg="White")
title.grid(row=0,columnspan=2,pady=20)
#-------------------------------Label-------------------------------------------
Agency_label=Label(f2,text="Agency",font=("Arial",20),bg="#605DE2",fg="White")
Agency_label.grid(row=1,column=0,pady=10,padx=10,sticky="w")
#------entry-------
Agency_name=Entry(f2,textvariable=Agency,font=("Arial",15),bg="White",fg="Black",relief="flat",bd=0)
Agency_name.grid(row=1,column=1,pady=12,padx=10)
Agency_name.bind("<FocusIn>",on_enter2)
Agency_name.bind("<FocusOut>",on_leave2)
Agency_name.bind("<Return>",next1)
Agency_name.bind("<Down>",down1)
Agency_name.bind("<Up>",up1)
#--------medicine-------------
Medicine_label=Label(f2,text="Medicine",font=("Airal",20),bg="#605DE2",fg="White")
Medicine_label.grid(row=2,column=0,pady=10,padx=10,sticky="w")
#-------entry-------------------
Medicine_name=Entry(f2,font=("Dubai",15),bg="White",textvariable=Medicine,fg="Black",relief="flat",bd=0)
Medicine_name.grid(row=2,column=1,pady=12,padx=10)
Medicine_name.bind("<FocusIn>",on_enter6)
Medicine_name.bind("<FocusOut>",on_leave6)
Medicine_name.bind("<Return>",next2)
Medicine_name.bind("<Down>",down2)
Medicine_name.bind("<Up>",up2)
#--------------------------quantity--------------
quantity_label=Label(f2,text="Quantity",font=("Airal",20),bg="#605DE2",fg="White")
quantity_label.grid(row=3,column=0,pady=10,padx=10,sticky="w")
#-------entry-------------------
quantity_name=Entry(f2,font=("Dubai",15),textvariable=quantity,bg="White",fg="Black",relief="flat",bd=0)
quantity_name.grid(row=3,column=1,pady=12,padx=10)
quantity_name.bind("<FocusIn>",on_enter4)
quantity_name.bind("<FocusOut>",on_leave4)
quantity_name.bind("<Return>",next3)
quantity_name.bind("<Down>",down3)
quantity_name.bind("<Up>",up3)
#--------------------------Batch num-----------------------------
Batch_label=Label(f2,text="Batch",font=("Airal",20),bg="#605DE2",fg="White")
Batch_label.grid(row=4,column=0,pady=10,padx=10,sticky="w")
#-------entry-------------------
Batch_name=Entry(f2,font=("Dubai",15),bg="White",textvariable=Batch,fg="Black",relief="flat",bd=0)
Batch_name.grid(row=4,column=1,pady=12,padx=10)
Batch_name.bind("<FocusIn>",on_enter7)
Batch_name.bind("<FocusOut>",on_leave7)
Batch_name.bind("<Return>",next4)
Batch_name.bind("<Down>",down4)
Batch_name.bind("<Up>",up4)
#-------------------------rate---------------------------------------
rate_label=Label(f2,text="Rate",font=("Airal",20),bg="#605DE2",fg="White")
rate_label.grid(row=5,column=0,pady=10,padx=10,sticky="w")
#-------entry-------------------
rate_name=Entry(f2,font=("Dubai",15),bg="White",fg="Black",textvariable=rate,relief="flat",bd=0)
rate_name.grid(row=5,column=1,pady=12,padx=10)
rate_name.bind("<FocusIn>",on_enter5)
rate_name.bind("<FocusOut>",on_leave5)
rate_name.bind("<Return>",next5)
rate_name.bind("<Down>",down5)
rate_name.bind("<Up>",up5)
#--------------------------------Expiry---------------------------------
Exp_label=Label(f2,text="Expiry",font=("Airal",20),bg="#605DE2",fg="White")
Exp_label.grid(row=6,column=0,pady=10,padx=10,sticky="w")
#-------entry-------------------
Exp_name=Entry(f2,font=("Dubai",15),bg="White",fg="Black",relief="flat",bd=0,textvariable=Exp)
Exp_name.grid(row=6,column=1,pady=12,padx=10)
Exp_name.bind("<FocusIn>",on_enter3)
Exp_name.bind("<FocusOut>",on_leave3)
Exp_name.bind("<Return>",next6)
Exp_name.bind("<Down>",down6)
Exp_name.bind("<Up>",up6)
#--------------------------------Date------------------------------------
Date_label=Label(f2,text="Date",font=("Airal",20),bg="#605DE2",fg="White")
Date_label.grid(row=7,column=0,pady=10,padx=10,sticky="w")
#-------entry-------------------
Date_name=Entry(f2,font=("Dubai",15),bg="White",fg="Black",relief="flat",bd=0,textvariable=Date)
Date_name.grid(row=7,column=1,pady=12,padx=10)
Date_name.bind("<FocusIn>",on_enter1)
Date_name.bind("<FocusOut>",on_leave1)
Date_name.bind("<Return>",next7)
Date_name.bind("<Down>",down7)
Date_name.bind("<Up>",up7)

bill_label=Label(f2,text="Bill_num",font=("Airal",20),bg="#605DE2",fg="White")
bill_label.grid(row=8,column=0,pady=10,padx=10,sticky="w")
Billno_name=Entry(f2,font=("Dubai",15),bg="White",fg="Black",relief="flat",bd=0,textvariable=Billno)
Billno_name.grid(row=8,column=1,pady=12,padx=10)
Billno_name.bind("<FocusIn>",on_enter8)
Billno_name.bind("<FocusOut>",on_leave8)
Billno_name.bind("<Return>",next8)
Billno_name.bind("<Down>",down8)
Billno_name.bind("<Up>",up8)
#------------------------------Buttons----------
btn_frame=Frame(f2,bg="#605DE2")
btn_frame.place(x=10,y=550,width=430)
Submit=Button(btn_frame,text="Submit",width =10,command=submit)
Submit.grid(row=0,column=0,pady=10,padx=10)
Update=Button(btn_frame,text="Update",width =10,command=update)
Update.grid(row=0,column=1,pady=10,padx=10)
Reset=Button(btn_frame,text="Reset",width =10,command=reset)
Reset.grid(row=0,column=2,pady=10,padx=10)
Delete=Button(btn_frame,text="Delete", width =10,command=delete_entry)
Delete.grid(row=0,column=3,pady=10,padx=10)
Show=Button(btn_frame,text="Show", width =20,command=show)
Show.grid(row=2,columnspan=2,column=1,pady=10,padx=10)
#-----------------------------------------------Right Frame--------------------------------------------------------------
f3=Frame(root,bg="#605DE2",pady=20)
f3.place(x=500,y=70,width=1000,height=700)
search_label=Label(f3,text="Search By",font=("Airal",15),fg="White",bg="#605DE2",pady=10,padx=10)
search_label.grid(row=0,column=0)
search_name=Entry(f3,textvariable=search_by)
search_name.grid(row=0,column=1)
to_label=Label(f3,bg="#605DE2",pady=10,padx=10,font=("Airal",15),fg="White")
to_label.grid(row=0,column=2)
to_name=Entry(f3,textvariable=search_txt,font=("Dubai",15),bg="White",fg="Black",width=12)
to_name.grid(row=0,column=3,padx=10,pady=10)
search_btn=Button(f3,text="Search",width=10,command=searching)
search_btn.grid(row=0,column=4)
#-----------------frame--------------------------------------
tabel_frame=Frame(f3,bg="#605DE2",pady=20)
tabel_frame.place(x=20,y=80,width=950,height=600)
scroll_x=Scrollbar(tabel_frame,orient=HORIZONTAL)
scroll_y=Scrollbar(tabel_frame,orient=VERTICAL)
main_tabel=ttk.Treeview(tabel_frame,columns=("Agency","Medicine","Billno","Expiry","Batch","Rate","Quantity","Id","Date"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=main_tabel.xview)
scroll_y.config(command=main_tabel.yview)
main_tabel.heading("Agency",text="Agency")
main_tabel.heading("Medicine",text="Medicine")
main_tabel.heading("Billno",text="Bill_no")
main_tabel.heading("Expiry",text="Expiry")
main_tabel.heading("Batch",text="Batch")
main_tabel.heading("Rate",text="Rate")
main_tabel.heading("Quantity",text="Quantity")
main_tabel.heading("Id",text="Id")
main_tabel.heading("Date",text="Date")
main_tabel['show']='headings'
main_tabel.column("Quantity",width=100)
main_tabel.column("Rate",width=100)
main_tabel.pack(fill=BOTH,expand=1)
main_tabel.bind("<ButtonRelease-1>",act)


root.mainloop()