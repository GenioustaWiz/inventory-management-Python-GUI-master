import tkinter as tk
from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk
import time
#import sales

root = tk.Tk()
import sales
import admin
root.geometry('1200x680+0+0')
root.resizable(0, 0)
root.config(bg="white")

#========================================VARIABLES========================================
USERNAME = StringVar()
PASSWORD = StringVar()
#===========Add Users======
rank = StringVar()
user_name = StringVar()
login_name = StringVar()
u_id = IntVar()
user_pass = StringVar()
type_id = StringVar()
emp_date = StringVar()

u_id.set("")
#========================================METHODS==========================================

def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `usr` (usr_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, userrank TEXT, username TEXT, loginname TEXT, userid TEXT, idtype TEXT, userpass TEXT, empltdate TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `employee` (employee_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `product` (product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, product_name TEXT, product_qty TEXT, product_price TEXT)")
    """cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    cursor.execute("SELECT * FROM `employee` WHERE `username` = 'ad' AND `password` = 'ad'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        cursor.execute("INSERT INTO `employee` (username, password) VALUES('admin1', 'admin1')")
        conn.commit()"""
        
        

def ShowAddNew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Inventory Management System/Add new user")
    width = 600
    height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    AddNewForm()

def AddNewForm():
    TopAddNew = Frame(addnewform, width=600, height=100, bd=4, relief=GROOVE)
    TopAddNew.pack(side=TOP, pady=5,padx=5)
    lbl_text = Label(TopAddNew, text="Add new User", font=('arial', 20), width=600)
    lbl_text.pack(fill=X)
    MidAddNew = Frame(addnewform, width=600, bd=4, relief=GROOVE)
    MidAddNew.pack(side=TOP, pady=10,padx=5)
    lblN= Label(MidAddNew,text="Rank:", font=('arial', 25), bd=10)
    lblN.grid(row=0, column=0,sticky=W)
    cboN= ttk.Combobox(MidAddNew, font=('arial', 23),textvariable=rank,state='readonly',width=15)
    cboN['value']=('','Admin','Emlpoyee')
    cboN.current(0)
    cboN.grid(row=0,column=1)

    lbl_username = Label(MidAddNew, text="User Name:", font=('arial', 25), bd=10)
    lbl_username.grid(row=1,column=0, sticky=W)
    userName = Entry(MidAddNew, textvariable=user_name, font=('arial', 25), width=15)
    userName.grid(row=1, column=1)
    lbl_screenname = Label(MidAddNew, text="Login Name:", font=('arial', 25), bd=10)
    lbl_screenname.grid(row=2,column=0, sticky=W)
    screenname = Entry(MidAddNew, textvariable=login_name, font=('arial', 25), width=15)
    screenname.grid(row=2, column=1)
    lbl_id = Label(MidAddNew, text="User Id:", font=('arial', 25), bd=10)
    lbl_id.grid(row=3, sticky=W)
    userId = Entry(MidAddNew, textvariable=u_id, font=('arial', 25), width=15)
    userId.grid(row=3, column=1)
    lbl_idT = Label(MidAddNew, text="Type of ID:", font=('arial', 25), bd=10)
    lbl_idT.grid(row=4, sticky=W)
    Id_type = Entry(MidAddNew, textvariable=type_id, font=('arial', 25), width=15)
    Id_type.grid(row=4, column=1)
    lbl_qty = Label(MidAddNew, text="User Password:", font=('arial', 25), bd=10)
    lbl_qty.grid(row=5, sticky=W)
    productqty = Entry(MidAddNew, textvariable=user_pass, font=('arial', 25), width=15)
    productqty.grid(row=5, column=1)
    
    lbl_price = Label(MidAddNew, text="Employment Date:", font=('arial', 25), bd=10)
    lbl_price.grid(row=6, sticky=W)
    productprice = Entry(MidAddNew, textvariable=emp_date, font=('arial', 25), width=15)
    productprice.grid(row=6, column=1)
    btn_add = Button(MidAddNew, text="Save", font=('arial', 14), width=30, bg="#009ACD", command = AddNew)
    btn_add.grid(row=7, columnspan=2, pady=20)

def AddNew():
    Database()
    cursor.execute("INSERT INTO `usr` (userrank, username,loginname, userid, idtype, userpass, empltdate) VALUES(?, ?, ?, ?, ?, ?, ?)", (rank.get(),user_name.get(),login_name.get(), u_id.get(), type_id.get(), user_pass.get(), emp_date.get()))
    conn.commit()
    rank .set("")
    user_name.set("")
    login_name.set("")
    u_id.set("")
    user_pass.set("")
    type_id.set("")
    emp_date.set("")
    cursor.close()
    conn.close()
    
def Exit():
    result = tkMessageBox.askquestion('Inventory Management System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()
        
def Admin_Reg_Chk(): #Checks whether their is another admin registered before registering a new one.
    #if admin available in the database it refuses to register another one.
    
    Database()
    cursor.execute("SELECT userrank FROM usr")
    fetch = cursor.fetchall()
    print(fetch)
    
    if fetch != []:
        cursor.close() #close to avoid endless loop.
        conn.close()
        #print("Am Sorry their is already another admin registered")
        tkMessageBox.showwarning("Warning", "Cannot to open Signup screen, because Admin Info already Exists")
        tkMessageBox.showinfo("Information", "Please proceed to Login screen")
        
    else:
        print("Thanks")
        Signup()
    
    cursor.close()
    conn.close()
 
def Signup():
    global signupform
     
    signupform = Toplevel()
    signupform.title("Inventory Management System/Signup")
    width = 600
    height = 450
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    signupform.resizable(0, 0)
    signupform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    TopsignForm = Frame(signupform, width=600, height=100, bd=1, relief=SOLID)
    TopsignForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopsignForm, text="Administrator Signup", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidsignForm = Frame(signupform, width=600)
    MidsignForm.pack(side=TOP, pady=10)
    
    lblN= Label(MidsignForm,text="Rank:", font=('arial', 14), bd=5)
    lblN.grid(row=0, column=0,sticky=W, pady=5)
    cboN= ttk.Combobox(MidsignForm, font=('arial', 13),textvariable=rank,state='readonly',width=15)
    cboN['value']=('click me','Admin')
    cboN.current(0)
    cboN.grid(row=0,column=1)
    lbl_username = Label(MidsignForm, text="User Name:", font=('arial', 14), bd=5)
    lbl_username.grid(row=1,column=0, sticky=W, pady=5)
    userName = Entry(MidsignForm, textvariable=user_name, font=('arial', 14), width=15)
    userName.grid(row=1, column=1)
    lbl_screenname = Label(MidsignForm, text="Login Name:", font=('arial', 14), bd=5)
    lbl_screenname.grid(row=2,column=0, sticky=W, pady=5)
    screenname = Entry(MidsignForm, textvariable=login_name, font=('arial', 14), width=15)
    screenname.grid(row=2, column=1)
    lbl_id = Label(MidsignForm, text="User Id:", font=('arial', 14), bd=5)
    lbl_id.grid(row=3, sticky=W, pady=5)
    userId = Entry(MidsignForm, textvariable=u_id, font=('arial', 14), width=15)
    userId.grid(row=3, column=1)
    lbl_idT = Label(MidsignForm, text="Type of ID:", font=('arial', 14), bd=5)
    lbl_idT.grid(row=4, sticky=W, pady=5)
    Id_type = Entry(MidsignForm, textvariable=type_id, font=('arial', 14), width=15)
    Id_type.grid(row=4, column=1)
    lbl_pass = Label(MidsignForm, text="User Password:", font=('arial', 14), bd=5)
    lbl_pass.grid(row=5, sticky=W, pady=5)
    password = Entry(MidsignForm, textvariable=user_pass, font=('arial', 14), width=15)
    password.grid(row=5, column=1)
    
    lbl_date = Label(MidsignForm, text="Employment Date:", font=('arial', 14), bd=5)
    lbl_date.grid(row=6, sticky=W, pady=5)
    emp_dat = Entry(MidsignForm, textvariable=emp_date, font=('arial', 14), width=15)
    emp_dat.grid(row=6, column=1)
    btn = Button(MidsignForm,text="Signup", command=auth_Signup,bd=1, bg= "red")
    btn.grid(row=7, column=1,columnspan=2, sticky=E, pady=20)
    btn.bind('<Return>', auth_Signup)
    
def auth_Signup(event=None):
    
    Database()
     
   
    if rank == "click me":
        #print("Am Sorry their is already another admin registered")
        tkMessageBox.showwarning("Warning", "Please Select Admin or Employee from Click me Button")
    elif user_name.get() == "" or login_name.get() == "" or u_id.get() == "" or user_pass.get() == "" or type_id.get() == "":
        tkMessageBox.showwarning("Warning", "Please fill every detail asked in the Signup form")
    else:
        cursor.execute("INSERT INTO `usr` (userrank, username,loginname, userid, idtype, userpass, empltdate) VALUES(?, ?, ?, ?, ?, ?, ?)", (rank.get(),user_name.get(),login_name.get(), u_id.get(), type_id.get(), user_pass.get(), emp_date.get()))
        conn.commit()
        rank .set("")
        user_name.set("")
        login_name.set("")
        u_id.set("")
        user_pass.set("")
        type_id.set("")
        emp_date.set("")
        signup_destroy()
    cursor.close()
    conn.close()
    
def signup_destroy():
    signupform.destroy()

def LoginForm():
    global lbl_result
    global loginform
    loginform = Toplevel()
    loginform.title("Inventory Management System/Account Login")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    
    TopLoginForm = Frame(loginform, width=600)
    TopLoginForm.pack(fill=X,side=TOP, pady=10,padx=5)
    cboN= ttk.Combobox(TopLoginForm, font=('arial', 23),textvariable=rank,state='readonly',width=15)
    cboN['value']=('click me','Admin','Emlpoyee')
    cboN.current(0)
    cboN.pack(anchor=CENTER)
    MidLoginForm = Frame(loginform, width=600)
    MidLoginForm.pack(side=TOP, pady=50)
    lbl_username = Label(MidLoginForm, text="Username:", font=('arial', 25), bd=18)
    lbl_username.grid(row=0)
    lbl_password = Label(MidLoginForm, text="Password:", font=('arial', 25), bd=18)
    lbl_password.grid(row=1)
    lbl_result = Label(MidLoginForm, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)
    username = Entry(MidLoginForm, textvariable=USERNAME, font=('arial', 25), width=15)
    username.grid(row=0, column=1)
    password = Entry(MidLoginForm, textvariable=PASSWORD, font=('arial', 25), width=15, show="*")
    password.grid(row=1, column=1)
    btn_login = Button(MidLoginForm, text="Login", font=('arial', 18), width=30, command=Login)
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('<Return>', Login)
    

def Logout():
    
    result = tkMessageBox.askquestion('Inventory Management System', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes': 
        admin_id = ""
        employee_id = ""
        changepage()

def Login(event=None):
    
    global admin_id, chk
    Database()
    if rank.get() == "click me":
        #print("Am Sorry their is already another admin registered")
        tkMessageBox.showwarning("Warning", "Please Select Admin or Employee from Click me Button")
    
    
    elif USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
     
    else:
        
        cursor.execute("SELECT * FROM `usr` WHERE `userrank` = ? AND `loginname` = ? AND `userpass` = ?", (rank.get(), USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `usr` WHERE `userrank` = ? AND `loginname` = ? AND `userpass` = ?", (rank.get(), USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            usr_id = data[0]
            if rank.get() == "Admin":
                chk = 1
                changepage()
                AdminHome()
                rank.set("")
                login_name.set("")
                user_pass.set("")
                lbl_result.config(text="")
            elif rank == "Employee":
                chk = 2
                changepage()
                EmpHome()
                rank.set("")
                login_name.set("")
                user_pass.set("")
                lbl_result.config(text="")
                
        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
        cursor.close()
        conn.close() 


def AdminHome():
    chk = 0
    loginform.destroy()
    
def EmpHome():
    chk = 0
    loginform.destroy()
   

#========================================MENUBAR WIDGETS==================================
"""def remove_menu():
    root.config(menu="")
    root.title("")"""
def menu1(root):
    root.title("Inventory Management System")
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Signup", command=Admin_Reg_Chk)
    filemenu.add_command(label="Exit", command=Exit)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)
def menu2(root):
    root.title("Inventory Management System/Administrator")
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu2 = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Logout", command=Logout)
    filemenu.add_command(label="Exit", command=Exit)
    filemenu2.add_command(label="Add User", command=ShowAddNew)
    menubar.add_cascade(label="Account", menu=filemenu)
    menubar.add_cascade(label="File", menu=filemenu2)
    root.config(menu=menubar)

def page1(root):
    f1 = tk.Frame(root)
    f1.pack(expand = True, fill = BOTH)
    
    #========================================FRAME============================================
    Title = tk.Frame(f1, bd=1, relief=SOLID)
    Title.pack(pady=10)

    login_dis = tk.Frame(f1, bd=1, relief=SOLID)
    login_dis.pack(pady=10)

    #========================================LABEL WIDGET=====================================
    lbl_display = tk.Label(Title, text="Welcome to IRS", font=('arial', 45))
    lbl_display.pack()

    lbl2_display = tk.Label(Title, text="Am a Retail & Inventory Management System, here to make your Business Life Easy", font=('arial', 12))
    lbl2_display.pack()

    btn_admin = tk.Button(login_dis, text="Login", command=LoginForm, font=('arial', 25) )
    btn_admin.pack(side=TOP, padx=10, pady=10)
    

def changepage():
    global pagenum, root
    
    for widget in root.winfo_children():
        widget.destroy()
        
    if pagenum == 1 and chk == 1:
        cursor.close() #hav to call this to close the database before its opened somewhere else
        conn.close() 
        menu2(root)
        admin.page2(root)
        pagenum = 2
    
    elif pagenum == 1 and chk == 2:
        cursor.close() #hav to call this to close the database before its opened somewhere else
        conn.close() 
        menu2(root)
        sales.page3(root)
        pagenum = 3
    else:
        page1(root)
        menu1(root)
        pagenum = 1
pagenum = 1
chk = 0

#========================================INITIALIZATION===================================
if __name__ == '__main__':
    menu1(root)
    page1(root)
    root.mainloop()
