import tkinter as tk
from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk
import bcrypt 

#===========Add Users======
rank = StringVar()
user_name = StringVar()
login_name = StringVar()
u_id = IntVar()
user_pass = StringVar()
user_passv = StringVar()
pass_x = StringVar()
type_id = StringVar()
emp_date = StringVar()
SEARCH = StringVar()

u_id.set("")
def connection():
    global conn, cursor
    conn = sqlite3.connect("irs.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `usr` (usr_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, userrank TEXT, username TEXT, loginname TEXT, userid TEXT, idtype TEXT, userpass TEXT, empltdate TEXT)")
    
  


def page4(root):
    global tree, ent_pass, ent_pass1
    
    f4= Frame(root, bg="green")
    f4.pack(fill = BOTH)
    leftframe = Frame(f4, bd=1, bg="light green", relief=GROOVE)
    leftframe.pack(anchor=W,fill = BOTH, side=LEFT, pady=5,padx=5)
    rightframe = Frame(f4, bd=1, bg="light green", relief=GROOVE)
    rightframe.pack(anchor=E,fill = BOTH, side=RIGHT, pady=5,padx=5)
    
    topframe = Frame(leftframe,  height=100, bd=4, relief=GROOVE)
    topframe.pack(anchor=NW,fill=X, side=TOP, pady=5,padx=5) 
    lbl_text = Label(topframe, text="Add new User", font=('arial', 20))
    lbl_text.pack(anchor=CENTER)
    MidAddNew = Frame(leftframe, bd=4, relief=GROOVE)
    MidAddNew.pack(anchor=NW,side=TOP,ipadx= 5, pady=(10,5),padx=5) #Tips #if i say side= LEFT the next frame after this one will be placed on the right
    lblN= Label(MidAddNew,text="Rank:", font=('arial', 14), bd=2)
    lblN.grid(row=0, column=0,sticky=W,pady=15)
    cboN= ttk.Combobox(MidAddNew, font=('arial', 13),textvariable=rank,state='readonly',width=15)
    cboN['value']=('','Admin','Employee')
    cboN.current(0)
    cboN.grid(row=0,column=1)

    lbl_username = Label(MidAddNew, text="User Name:", font=('arial', 14), bd=2)
    lbl_username.grid(row=1,column=0, sticky=W, pady=15)
    userName = Entry(MidAddNew, textvariable=user_name, font=('arial', 14), width=15)
    userName.grid(row=1, column=1)
    lbl_screenname = Label(MidAddNew, text="Login Name:", font=('arial', 14), bd=2)
    lbl_screenname.grid(row=2,column=0, sticky=W, pady=15)
    screenname = Entry(MidAddNew, textvariable=login_name, font=('arial', 14), width=15)
    screenname.grid(row=2, column=1)
    lbl_id = Label(MidAddNew, text="User Id:", font=('arial', 14), bd=2)
    lbl_id.grid(row=3, sticky=W, pady=15)
    userId = Entry(MidAddNew, textvariable=u_id, font=('arial', 14), width=15)
    userId.grid(row=3, column=1)
    lbl_idT = Label(MidAddNew, text="Type of ID:", font=('arial', 14), bd=2)
    lbl_idT.grid(row=4, sticky=W, pady=15)
    Id_type = Entry(MidAddNew, textvariable=type_id, font=('arial', 14), width=15)
    Id_type.grid(row=4, column=1)
    lbl_pass = Label(MidAddNew, text="Password:", font=('arial', 14), bd=2)
    lbl_pass.grid(row=5, sticky=W, pady=15) 
    ent_pass = Entry(MidAddNew, textvariable=user_pass, font=('arial', 14), width=15, show="*")
    ent_pass.grid(row=5, column=1)
    ent_pass.bind("<Button-1>", clear_p)#shld clr quantity entry and
    ent_pass = Label(MidAddNew, textvariable=pass_x, font=('arial', 7))
    ent_pass.grid(row=5, column=2)
    
    lbl_passv = Label(MidAddNew, text="Verify Password:", font=('arial', 14), bd=2)
    lbl_passv.grid(row=6, sticky=W, pady=15)
    ent_passv = Entry(MidAddNew, textvariable=user_passv, font=('arial', 14), width=15, show="*")
    ent_passv.grid(row=6, column=1)
    ent_passv.bind("<Button-1>", clear_pv)
    user_passv.trace('w', my_tracer)
    ent_pass1 = Label(MidAddNew, textvariable=pass_x, font=('arial', 7))
    ent_pass1.grid(row=6, column=2)
    lbl_emdate = Label(MidAddNew, text="Employment Date:", font=('arial', 14), bd=2)
    lbl_emdate.grid(row=7, sticky=W, pady=15)
    ent_emdate = Entry(MidAddNew, textvariable=emp_date, font=('arial', 14), width=15)
    ent_emdate.grid(row=7, column=1)
    
    btn_fram = Frame(leftframe, bd=4, bg="light green", relief=GROOVE)
    btn_fram.pack(fill=X, pady=5,padx=5)
    btn_add = Button(btn_fram, text="Save User", font=('arial', 14), bg="#009ACD", command = AddNew)
    btn_add.pack(pady=(10,5), padx=5, fill=X)
    btn_add = Button(btn_fram, text="Update User", font=('arial', 14), bg="#009ACD", command = update_data)
    btn_add.pack(fill=X, padx=5)
    
    #========================Calculator===================================
    topframe = Frame(rightframe,  height=100, bd=4, relief=GROOVE)
    topframe.pack(fill=X, side=TOP, pady=(5,3),padx=5) 
    lbl_text = Label(topframe, text="Users Display Screen", font=('arial', 20))
    lbl_text.pack(anchor=CENTER)
    treeframe = Frame(rightframe, bd=4, relief=GROOVE)
    treeframe.pack(side=TOP, pady=5,padx=5) 
    scrollbarx = Scrollbar(treeframe, orient=HORIZONTAL)
    scrollbar = Scrollbar(treeframe, orient=VERTICAL)
    tree = ttk.Treeview(treeframe,height=24, columns=("UserID","Rank", "User Name", "Login Name", "ID", "ID Type", "Password", "Employment Date"), selectmode="extended", yscrollcommand=scrollbar.set, xscrollcommand=scrollbarx.set)
    scrollbar.config(command=tree.yview)
    scrollbar.grid(row=0,column=2, sticky=N+S+E)
    scrollbarx.config(command=tree.xview)
    scrollbarx.grid(row=1,columnspan=2, sticky=W+E+S)
    tree.heading('UserID', text="UserID",anchor=W)
    tree.heading('Rank', text="Rank",anchor=W)
    tree.heading('User Name', text="User Name",anchor=W)
    tree.heading('Login Name', text="Login Name",anchor=W)
    tree.heading('ID', text="ID",anchor=W)
    tree.heading('ID Type', text="ID Type",anchor=W)
    tree.heading('Password', text="Password",anchor=W)
    tree.heading('Employment Date', text="Employment Date",anchor=W)
         
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=80)
    tree.column('#3', stretch=NO, minwidth=0, width=150)
    tree.column('#4', stretch=NO, minwidth=0, width=80)
    tree.column('#5', stretch=NO, minwidth=0, width=80)
    tree.column('#6', stretch=NO, minwidth=0, width=100)
    tree.column('#7', stretch=NO, minwidth=0, width=80)
    tree.column('#8', stretch=NO, minwidth=0, width=130)
    
    tree.grid(row=0,column=1)
    tree.bind('<<TreeviewSelect>>', select_item)
    DisplayData()
    #==========Search\Buttons================
    btn_frame = Frame(rightframe, bg="light green", relief=GROOVE)
    btn_frame.pack(fill=X)
    search = Entry(btn_frame, textvariable=SEARCH, width=30, font=('arial', 14))
    search.grid(row=0,column=0,pady=5,padx=(10,5))
    search.insert(0,"Enter 'login name' to search")
    search.bind("<Button-1>", clear_search) #bind the mouse button, when clicked words disappear
    btn_search = Button(btn_frame, text="Search", font=('arial', 14), bg="light blue", command=Search)
    btn_search.grid(row=0,column=1,pady=5,padx=(5,15))
    btn_add = Button(btn_frame, text="Delete", font=('arial', 14), bg="green", command = delete_data)
    btn_add.grid(row=0, column=2, pady=2, padx=20)
    btn_add = Button(btn_frame, text="Clear", font=('arial', 14), bg="green", command = clear)
    btn_add.grid(row=0, column=3, pady=2, padx=20)

def clear_p(Event):
    user_pass.set("")
    pass_x.set("")
def clear_pv(Event):
    user_passv.set("")
    pass_x.set("")
    
def my_tracer(a,b,c): #Trace send 3arguments to my_tracer
    #print(a, b, c)
    global new, act
    
    if user_pass != 0:
        
        pass__ = user_pass.get()
        pass_v = user_passv.get()
        if pass__ == pass_v:
            pass_x.set("y")
            ent_pass.configure(fg="green")
            ent_pass1.configure(fg="green")
        elif pass__ != pass_v:
            pass_x.set("x")
            ent_pass.configure(fg="red")
            ent_pass1.configure(fg="red")
        elif pass_v == "":
            pass_x.set("")

def Search():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        connection()
        cursor.execute("SELECT * FROM `product` WHERE `loginname` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
            
        cursor.close()
        conn.close()
def clear_search(Event):
    #search.delete(0, Entry.END)
    SEARCH.set("")
        
def DisplayData():
    connection()
    cursor.execute("SELECT * FROM `usr`")
    fetch = cursor.fetchall()
    for data in fetch:
        print(data)
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    
def AddNew():
    ret=verifier()
    if ret==0:
        password = user_pass.get().encode("utf-8")

        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        print(password)
        print(hashed)
        connection()
        cursor.execute("INSERT INTO `usr` (userrank, username,loginname, userid, idtype, userpass, empltdate) VALUES(?, ?, ?, ?, ?, ?, ?)", (rank.get(),user_name.get(),login_name.get(), u_id.get(), type_id.get(), hashed, emp_date.get()))
        conn.commit()
        rank.set("")
        user_name.set("")
        login_name.set("")
        u_id.set("")
        user_pass.set("")
        type_id.set("")
        emp_date.set("")
        cursor.close()
        conn.close()    
        clear()
        tree.delete(*tree.get_children())
        DisplayData()  
    else:
        tkMessageBox.showwarning("Warning", "Cannot to open Signup screen, because Admin Info already Exists")
       
    
###===============for inserting selected items from Treeview to an entry Box===============          
def select_item(event):
    print(tree.selection()) #Used for deburging
    item = tree.selection()
    for i in item:
        try:
            global selected_item, data_
            data_ = tree.item(i, 'values')
            
            print(data_) #Used for deburging
            """products_ent.delete(0, END)
            products_ent.insert(END, selected_item[1])
            #in_stock.delete(0, END)
            stock.set(int(selected_item[2]))
            """
            #user_id = data_[0]
            rank.set(data_[1])
            user_name.set(data_[2])
            login_name.set(data_[3])
            u_id.set(data_[4])
            type_id.set(data_[5])
            user_pass.set(data_[6])
            emp_date.set(data_[7])
            print (data_[6])
            
        except IndexError:
            pass
        
def verifier():
    if user_name.get() == "" or login_name.get() == "" or u_id.get() == "" or user_pass.get() == "" or user_passv.get() == "" or type_id.get() == "":
        tkMessageBox.showwarning("Warning", "Please fill every detail asked in the Signup form")
        return 1
    else:
        return 0

def delete_data():
        global data_
        w = data_[2]
        print (w)
        
        result = tkMessageBox.askquestion('User Management', 'Are you sure you want to delete ' + w + '?', icon="warning")
        if result == 'yes': 
            connection()
            cursor.execute("DELETE FROM usr WHERE usr_id=?",(data_[0],))
            conn.commit()
            cursor.close()
            conn.close()
            tree.delete(*tree.get_children())
            clear()
            DisplayData()
            print("SUCCESSFULLY DELETED THE USER")

def update_data():
    ret=verifier()
    if ret==0:
        password = user_pass.get().encode("utf-8")
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        print(password)
        print(hashed)
        print("....")
        print(data_[0])
        connection()
        cursor.execute("UPDATE usr SET userrank=?, username=?,loginname=?, userid=?, idtype=?, userpass=?, empltdate=? WHERE usr_id=?", (rank.get(),user_name.get(),login_name.get(), u_id.get(), type_id.get(), hashed, emp_date.get(), data_[0]))
        conn.commit()
        cursor.close()
        conn.close()
        tree.delete(*tree.get_children())
        DisplayData()
        clear()
        
        print("UPDATED SUCCESSFULLY")

def clear():
    rank.set("")
    user_name.set("")
    login_name.set("")
    u_id.set("")
    user_pass.set("")
    user_passv.set("")
    type_id.set("")
    emp_date.set("")
    pass_x.set("")
    data_ = [] 