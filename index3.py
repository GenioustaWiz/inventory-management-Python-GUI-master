import tkinter as tk
from tkinter import *
import tkinter.messagebox as tkMessageBox

import sqlite3
import tkinter.ttk as ttk
import time
import bcrypt 
import _cffi_backend
from datetime import datetime, date
#import sales
deactivate=5
back=5
act_ = 0

root = tk.Tk()
#import sales
import sales1
import products
import users
import receipt
root.geometry('1200x680+0+0')
#root.resizable(0, 0)
root.config(bg="black")

def sale(): #helps in changing from sales to sales1 and vice varsa wen trying differnet widgets
    root.title("Inventory Management System/Administrator:  Sales Management")
    sale = sales1.page3(root, back)
def product():
    global back
    root.title("Inventory Management System/Administrator:  Product Management")
    product = products.page2(root, back)
    #back = 0
    
Date1 =StringVar()
Time1 =StringVar()
def T_update():
    Date1.set(time.strftime("%d/%m/%y"))
    Time1.set(time.strftime("%H:%M:%S"))
#================Check for Expiry = === ====== = = =
def program_expired():
    connection()
    """cursor.execute("DELETE FROM expiry WHERE date_time")
    conn.commit()"""
    cursor.execute("SELECT * FROM `expiry`")
    Date = cursor.fetchone()
    print(Date)
    #Date = Date[1]
    now = datetime.now()
    #print(now.strftime("%A"))
    now1 = now.day #Only Chooses day from date. and saves it
    print(now)
    if Date == None:
        global act_
        print ("Date == None")
        now2 = str(now1)
        cursor.execute("INSERT INTO `expiry` (date_time) VALUES(?)",(now2,)) #((now2,))the comma is required for a single element hence it will return error
        conn.commit()
        act_ = 1
        expiry_.set("1 month remaining to expiry date")  
        
    elif Date[1]:
        date_ = int(Date[1])
        check_ = (now1 - date_)
        month_ = 31
        
        remaining_days = str( month_ - check_)
        print(remaining_days)
        if check_ >= month_: #expiry date is set afta 31 days
            global alert
            alert = 1   
            expiry_.set("0 days remaining. Product has expired")  
            #tkMessageBox.showerror('Error', 'Sorry Your Product has Expired. Please contact the Author for more information..')
            #sys.exit()
        elif check_ <= month_:
            expiry_.set("Remaining " + remaining_days + "days to expiry")
    
       

    conn.close()
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
expiry_ = StringVar()

u_id.set("")


#========================================METHODS==========================================
def connection():
    global conn, cursor
    conn = sqlite3.connect("irs.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `usr` (usr_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, userrank TEXT, username TEXT, loginname TEXT, userid TEXT, idtype TEXT, userpass TEXT, empltdate TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `product` (product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, product_name TEXT,product_category TEXT,Initial_stock TEXT,Stock_available TEXT, product_price TEXT, product_colour TEXT, product_size TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `receipt` (receipt_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, customer_name TEXT,phone_no TEXT,bill_no TEXT,product_name TEXT, product_quantity TEXT, product_price TEXT, product_total TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `expiry` (exp_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date_time)")
    
def ShowAddNew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Inventory Management System/Add Admin user")
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
    cboN['value']=('','Admin','Employee')
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
    global app_date
    connection()
    cursor.execute("INSERT INTO `usr` (userrank, username,loginname, userid, idtype, userpass, empltdate) VALUES(?, ?, ?, ?, ?, ?, ?)", (rank.get(),user_name.get(),login_name.get(), u_id.get(), type_id.get(), user_pass.get(), emp_date.get()))
    now = datetime.now()
    cursor.execute("insert into expiry values(?)",(now))
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
    
def Exit():
    result = tkMessageBox.askquestion('Inventory Management System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()
        
def Admin_Reg_Chk(): #Checks whether their is another admin registered before registering a new one.
    #if admin available in the database it refuses to register another one.
    
    connection()
    cursor.execute("SELECT userrank FROM usr")
    fetch = cursor.fetchall()
    print(fetch)
    cursor.close() #close to avoid endless loop.
    conn.close()
    if fetch != []:
        
        #print("Am Sorry their is already another admin registered")
        tkMessageBox.showwarning("Warning", "Cannot to open Signup screen, because Admin Info already Exists")
        tkMessageBox.showinfo("Information", "Please proceed to Login screen")
        
    else:
        print("Thanks")
        Signup()
    
    
 
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
    password = Entry(MidsignForm, textvariable=user_pass, font=('arial', 14), width=15, show="*")
    password.grid(row=5, column=1)
    
    lbl_date = Label(MidsignForm, text="Employment Date:", font=('arial', 14), bd=5)
    lbl_date.grid(row=6, sticky=W, pady=5)
    emp_dat = Entry(MidsignForm, textvariable=emp_date, font=('arial', 14), width=15)
    emp_dat.grid(row=6, column=1)
    btn = Button(MidsignForm,text="Signup", command=auth_Signup,bd=1, bg= "red")
    btn.grid(row=7, column=1,columnspan=2, sticky=E, pady=20)
    btn.bind('<Return>', auth_Signup)
    
def auth_Signup(event=None):
    password = user_pass.get().encode("utf-8")

    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    print(password)
    print(hashed)
    
    connection()
     
   
    if rank == "click me":
        #print("Am Sorry their is already another admin registered")
        tkMessageBox.showwarning("Warning", "Please Select Admin or Employee from Click me Button")
    elif user_name.get() == "" or login_name.get() == "" or u_id.get() == "" or user_pass.get() == "" or type_id.get() == "":
        tkMessageBox.showwarning("Warning", "Please fill every detail asked in the Signup form")
    else:
        cursor.execute("INSERT INTO `usr` (userrank, username,loginname, userid, idtype, userpass, empltdate) VALUES(?, ?, ?, ?, ?, ?, ?)", (rank.get(),user_name.get(),login_name.get(), u_id.get(), type_id.get(), hashed, emp_date.get()))
        conn.commit()
        rank.set("")
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
    if alert == 1:
        tkMessageBox.showwarning("Warning", 'Sorry Your Product has Expired. You have no Prodcut Access Rights. Please contact the Author for more information..')
    else:
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
        cboN['value']=('click me','Admin','Employee')
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
        global chk,back,admin_id,employee_id
        
        admin_id = ""
        employee_id = ""
        chk=0
        back_()
        changepage()

def Login(event=None):
    
    global usr_id,chk,r,back
    connection()
    
    if rank.get() == "click me":
        #print("Am Sorry their is already another admin registered")
        tkMessageBox.showwarning("Warning", "Please Select Admin or Employee from Click me Button")
    
    
    elif USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    
    else:
        password = PASSWORD.get().encode("utf-8")
        cursor.execute("SELECT * FROM `usr` WHERE `userrank` = ? AND `loginname` = ?", (rank.get(), USERNAME.get()))
        passv = cursor.fetchone()
        hashed = passv[6]
        print(password)
        print(hashed)
        if bcrypt.checkpw(password, hashed):
            cursor.execute("SELECT * FROM `usr` WHERE `userrank` = ? AND `loginname` = ? AND `userpass` = ?", (rank.get(), USERNAME.get(), PASSWORD.get()))
            #data = cursor.fetchone()
            #usr_id = data[0]
            if rank.get() == "Admin":
                chk = 1
                back = 0
                changepage()
                AdminHome()
                rank.set("")
                USERNAME.set("")
                PASSWORD.set("")
                lbl_result.config(text="")
            elif rank.get() == "Employee":
                chk = 2
                back = 1
                changepage()
                EmpHome()
                rank.set("")
                USERNAME.set("")
                PASSWORD.set("")
                lbl_result.config(text="")
                
        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
        cursor.close()
        conn.close() 

def Users():
    global chk,r_edit
    chk = 1
    r_edit = 4
    changepage()
    
    
def AdminHome():
    chk = 0
    loginform.destroy()
    
def EmpHome():
    chk = 0
    loginform.destroy()

def back_():
    global back
    back = 5
def back__():
    global back
    back = 1

def pag2():
    #====Helps go back to Products Screen
    global pagenum,chk,r_edit
    r_edit = 4
    pagenum = 1
    chk = 1
    changepage()
def pag3():
    #====Helps go back to Sales Screen
    global pagenum,chk,r_edit
    r_edit = 4
    pagenum = 1
    chk = 2
    back__()
    changepage()

def Receipt():
    global r_u, deactivate, s_r, r_edit,chk
    
    print(back)
    if  back==1:#for employee
        #====Helps go back to receipt Screen with user only privilleges
        s_r =0
        r_edit = 2
        deactivate = 1
        
        changepage()
    elif back==0:#for admin
        s_r =1
        r_edit = 1
        deactivate = 0
        chk = 0
        back_()
        changepage()
   
    
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
    #root.title("Inventory Management System/Administrator")
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu2 = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Logout", command=Logout)
    filemenu.add_command(label="Exit", command=Exit)
    filemenu2.add_command(label="Users Screen", command=Users)
    filemenu2.add_command(label="Products Screen", command=pag2)
    filemenu2.add_command(label="Sales Screen", command=pag3)
    filemenu2.add_command(label="Receipt Screen", command=Receipt)
    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Screens", menu=filemenu2)
    root.config(menu=menubar)
def menu3(root):
    root.title("Inventory Management System/Sales")
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu1 = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Logout", command=Logout)
    filemenu.add_command(label="Exit", command=Exit)
    filemenu1.add_command(label="Check Receipts", command= Receipt)
    filemenu1.add_command(label="Go to Sales", command= pag3)
    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Access", menu=filemenu1)
    root.config(menu=menubar)

def update_t():
    global t_str,show_t
    T_update()
    D= Date1.get()
    T= Time1.get()
    t_str = "D: "+D+" T: "+T
    
    
    #Use config to update Label
    #print(str(t_str))
    
    root.after(1000,update_t)
    
def page1(root):
    f1 = tk.Frame(root, bg="green")
    f1.pack(expand = True, pady=5, padx=5, fill = BOTH)
    
    #========================================FRAME============================================
    Title = tk.Frame(f1, relief=RAISED)
    Title.pack(pady=10, padx=5, fill=X)

    login_dis = tk.Frame(f1, relief=GROOVE)
    login_dis.pack(pady=30)
    
    expiry_dis = tk.Frame(f1, relief=SUNKEN,bg="light green")
    expiry_dis.pack(pady=(200,0))
    
    c_dis = tk.Frame(f1, relief=SUNKEN)
    c_dis.pack(pady=(50,0),side=BOTTOM, anchor=SE)
    
    #========================================LABEL WIDGET=====================================
    lbl_display = tk.Label(Title, text="Welcome to IRS", font=('arial', 45))
    lbl_display.pack()

    lbl2_display = tk.Label(Title, text="It's a Simple yet Efficient Retail & Inventory Management System, it's Designed with to help your Business Grow.",fg="gray", font=('arial', 15))
    lbl2_display.pack()

    btn_admin = tk.Button(login_dis, text="Login", command=LoginForm,bg="light green", font=('arial', 25), width=40)
    btn_admin.pack(padx=1, pady=1)
    
    lbl3_expiry = tk.Label(expiry_dis, textvariable=expiry_, font=('arial', 20), fg="red", bg="green")
    lbl3_expiry.pack( padx=3, pady=3)
    lbl3_expiry = tk.Label(c_dis, text="Designed By G*Lab", font=('arial', 20), fg="red", bg="green")
    lbl3_expiry.pack()
    
    if act_ == 1:
        tkMessageBox.showinfo("Welcome", "Your 30 days Trails has began today, You can buy the full product by contacting the Developer. Thank You")
        

def changepage():
    global pagenum,enter_page4,chk, root, r_edit
    #print(pagenum)
    #print(chk)
    #print(enter_page4)
    for widget in root.winfo_children():
        widget.destroy()
        
    if pagenum == 1 and chk == 1:
        menu2(root)
        product()
        pagenum = 2
    
    elif pagenum == 1 and chk == 2:
        menu3(root)
        sale()
        pagenum = 3
        
    elif enter_page4 ==0 and chk == 1:
        # print("Hi3")
        menu2(root)
        root.title("Inventory Management System/Administrator: User Management")
        users.page4(root)
        chk= 0
        #print(chk)
        pagenum = 4
        
    elif r_edit == 1:
        # print("Hi3")
        menu2(root)
        root.title("Inventory Management System/Receipt Management(ADMIN)")
        receipt.page5(root,deactivate)
        
        
    elif r_edit == 2:
        # print("Hi3")
        menu3(root)
        root.title("Inventory Management System/Receipt Management(Employee)")
        receipt.page5(root,deactivate)
        
        
            
    else:
        page1(root)
        menu1(root)
        pagenum = 1
pagenum = 1
enter_page4 = 0
chk = 0
r_edit = 0
alert = 0
program_expired()
#========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.after(1000,update_t)
    menu1(root)
    page1(root)
    root.mainloop()
