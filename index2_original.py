import tkinter as tk
from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk
import time
    

root = tk.Tk()
root.geometry('1200x680+0+0')
root.resizable(0, 0)
root.config(bg="white")

#========================================VARIABLES========================================
USERNAME = StringVar()
PASSWORD = StringVar()
PRODUCT_NAME = StringVar()
PRODUCT_PRICE = IntVar()
PRODUCT_QTY = IntVar()
SEARCH = StringVar()
 #=====Sales Variables+========
cust_name = StringVar()
phone = StringVar()
bill = StringVar()
products = StringVar()
category = StringVar()
quantity = StringVar()
#========================================METHODS==========================================

def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `employee` (employee_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `product` (product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, product_name TEXT, product_qty TEXT, product_price TEXT)")
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    cursor.execute("SELECT * FROM `employee` WHERE `username` = 'ad' AND `password` = 'ad'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        cursor.execute("INSERT INTO `employee` (username, password) VALUES('admin1', 'admin1')")
        conn.commit()

def Exit():
    result = tkMessageBox.askquestion('Inventory Management System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()
   
def Admin_LoginForm():
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
    TopLoginForm = Frame(loginform, width=600, height=100, bd=1, relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginForm, text="Administrator Login", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
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
    btn_login = Button(MidLoginForm, text="Login", font=('arial', 18), width=30, command=AdminLogin)
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('<Return>', AdminLogin)
    
def Emp_LoginForm():
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
    TopLoginForm = Frame(loginform, width=600, height=100, bd=1, relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginForm, text="Employee Login", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
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
    btn_login = Button(MidLoginForm, text="Login", font=('arial', 18), width=30, command=EmpLogin)
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('<Return>', EmpLogin)
    
def page2(root):
    global tree
    f2 = tk.Frame(root)
    f2.pack(expand = True, fill = BOTH)
    add_f = Frame(f2, bd=5, relief=SUNKEN, width = 600)
    add_f.pack(side = LEFT, fill = Y, padx=5, pady=2)
    
    #======================Product Add=======================
    top = Frame(add_f, bd=1, relief=SOLID)
    top.pack(anchor = W, fill = X)
    lbl_text = Label(top, text="Add New Product", font=('arial', 18))
    lbl_text.pack(side = TOP, pady=10)
    MidAddNew = Frame(add_f)
    MidAddNew.pack(side=TOP, anchor = W, pady=50)
    lbl_productname = Label(MidAddNew, text="Product Name:", font=('arial', 25), bd=10)
    lbl_productname.grid(row=0, sticky=W)
    productname = Entry(MidAddNew, textvariable=PRODUCT_NAME, font=('arial', 25), width=15)
    productname.grid(row=0, column=1)
    lbl_qty = Label(MidAddNew, text="Product Quantity:", font=('arial', 25), bd=10)
    lbl_qty.grid(row=1, sticky=W)
    productqty = Entry(MidAddNew, textvariable=PRODUCT_QTY, font=('arial', 25), width=15)
    productqty.grid(row=1, column=1)
    lbl_price = Label(MidAddNew, text="Product Price:", font=('arial', 25), bd=10)
    lbl_price.grid(row=2, sticky=W)
    productprice = Entry(MidAddNew, textvariable=PRODUCT_PRICE, font=('arial', 25), width=15)
    productprice.grid(row=2, column=1)
    btn_add = Button(MidAddNew, text="Save", font=('arial', 18), width=30, bg="#009ACD", command=AddNew)
    btn_add.grid(row=3, columnspan=2, pady=20)
    #===================== Product View======================
    view_f = Frame(f2, bd=5, relief=SUNKEN, width = 600)
    view_f.pack(side = LEFT, fill = Y, padx=5, pady=2)
    TopViewForm = Frame(view_f, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP,anchor = W, fill = X)
    LeftViewForm = Frame(view_f)
    LeftViewForm.pack(side=BOTTOM, fill=Y)
    MidViewForm = Frame(view_f)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Products", font=('arial', 18))
    lbl_text.pack(side = TOP, pady=10)
    search = Entry(MidViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(fill = BOTH, expand = TRUE, side = TOP, padx=5, pady=5)
    search.insert(0,"Enter the value to search")
    search.bind("<Button-1>", clear_search) #bind the mouse button, when clicked words disappear
    btn_search = Button(MidViewForm, text="Search", command=Search)
    btn_search.pack(fill = BOTH, expand = TRUE, side = TOP,padx=5, pady=5)
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset)
    btn_reset.pack(side=LEFT, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete)
    btn_delete.pack(side=LEFT, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("ProductID", "Product Name", "Product Qty", "Product Price"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('ProductID', text="ProductID",anchor=W)
    tree.heading('Product Name', text="Product Name",anchor=W)
    tree.heading('Product Qty', text="Product Qty",anchor=W)
    tree.heading('Product Price', text="Product Price",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()
    
   
    
def page3(root):
    global tree
    f3= tk.Frame(root)
    f3.pack(fill = BOTH)
    
    Title = Frame(f3, relief=RIDGE,width=1100, bg="powder blue", bd=8)
    Title.grid(sticky=W+E, padx=5,pady=5)
    lbl_text = Label(Title, text="View Products", font=('arial', 18), bg="powder blue")
    lbl_text.pack(pady=3)
    #========================   ==================
    top = Frame(f3, relief=RIDGE, bg="powder blue", bd=5)
    top.grid(row=1, column=0, sticky=W+E, padx=5,pady=5)
    cust_lbl = Label(top, text='Customer name:', font=('arial', 12))
    cust_lbl.grid(row=0, column=0, sticky=W,padx=10)
    cust_ent= Entry(top, textvariable = cust_name, width=20)
    cust_ent.grid(row=0, column=1, sticky=W, padx=20)
    phone_lbl = Label(top, text='Phone No:', font=('arial', 12))
    phone_lbl.grid(row=0, column=2, sticky=W,padx=10)
    phone_ent= Entry(top, textvariable = phone, width=20)
    phone_ent.grid(row=0, column=3, sticky=W, padx=20)           
    bill_lbl = Label(top, text='Bill No:', font=('arial', 12))
    bill_lbl.grid(row=0, column=4, sticky=W, padx=10)
    bill_ent= Entry(top, textvariable = bill, width=20)
    bill_ent.grid(row=0, column=5, sticky=E, padx=20)
    search_btn= Button(top, text ='Search', font=('arial', 14), width=10)
    search_btn.grid(row=0,column=6,padx=20, pady=3,sticky=E)
    #=======================Invisible  FRAME====================
    inv_f =Frame(f3)
    inv_f.grid(row=2, column=0,sticky=W) 
    #============= inputing product details===========
    entry_l = Frame(inv_f, relief=GROOVE, bg="powder blue", bd=5)
    entry_l.grid(row=0, column=0,sticky = W+N+S, padx=5,pady=5)
    products_lbl = Label(entry_l, text='Product :', font=('arial', 16), bg="powder blue")
    products_lbl.grid(padx=2, sticky=W)
    products_ent = Entry(entry_l, textvariable = 'products',width=10, font=('arial', 16))
    products_ent.grid(row=0, column=1,padx=20)
    view_btn= Button(entry_l, text= 'View', font=('arial', 10), command=Search)
    view_btn.grid(row=1, column=1,padx=10, pady=3, sticky=E)
    category_lbl = Label(entry_l, text='Category :', font=('arial', 16), bg="powder blue")
    category_lbl.grid(row=2, column=0,padx=2, pady=10, sticky=W)
    category_ent = Entry(entry_l, textvariable= 'category', width=10, font=('arial', 16))
    category_ent.grid(row=2, column=1,pady=5,padx=20)
    subegory_lbl = Label(entry_l, text='Sub Category :', font=('arial', 16), bg="powder blue")
    subegory_lbl.grid(row=3, column=0,padx=2, pady=10, sticky=W)
    subegory_ent = Entry(entry_l, textvariable= 'subegory',width=10, font=('arial', 16))
    subegory_ent.grid(row=3, column=1,pady=5,padx=20)
    quantity_lbl = Label(entry_l, text='Quantity :', font=('arial', 16), bg="powder blue")
    quantity_lbl.grid(row=4, column=0,padx=2, pady=10, sticky=W)
    quantity_ent = Entry(entry_l, textvariable= 'quantity',width=10, font=('arial', 16))
    quantity_ent.grid(row=4, column=1,pady=5,padx=20)
    #in_stock = Label(entry_l, text ='In Stock'+stock)
    cart_btn= Button(entry_l, text= 'Add to Cart', font=('arial', 16), width=10)
    cart_btn.grid(row=5, column=0, pady=10, sticky=E)
    clearp_btn= Button(entry_l, text= 'Clear', font=('arial', 16), width=10)
    clearp_btn.grid(row=5, column=1,padx=10, pady=20, sticky=E)
    
    
    #========================Calculator===================================
    scrollbarx = Scrollbar(inv_f, orient=HORIZONTAL)
    scrollbar = Scrollbar(inv_f, orient=VERTICAL)
    tree = ttk.Treeview(inv_f,height=20, columns=("ProductID", "Product Name", "Product Qty", "Product Price"), selectmode="extended", yscrollcommand=scrollbar.set, xscrollcommand=scrollbarx.set)
    scrollbar.config(command=tree.yview)
    scrollbar.grid(row=0,column=4, sticky=N+S+E)
    scrollbarx.config(command=tree.xview)
    scrollbarx.grid(row=1,column=3, sticky=W+E+S)
    tree.heading('ProductID', text="ProductID",anchor=W)
    tree.heading('Product Name', text="Product Name",anchor=W)
    tree.heading('Product Qty', text="Product Qty",anchor=W)
    tree.heading('Product Price', text="Product Price",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.grid(row=0,column=2)
    ##=============End of invisible Frame============
    
    """view = Frame(f3, relief=SOLID, bg="powder blue", bd=10)
    view.grid(row=1, column=2, )"""
    scrollbar_x = Scrollbar(inv_f, orient=HORIZONTAL)
    scrollbary = Scrollbar(inv_f, orient=VERTICAL)
    tree2 = ttk.Treeview(inv_f,height=20, columns=("ProductID", "Product Name", "Product Qty", "Product Price"), selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbar_x.set)
    scrollbary.config(command=tree2.yview)
    scrollbary.grid(row=0,column=4, sticky=N+S+E)
    scrollbar_x.config(command=tree2.xview)
    scrollbar_x.grid(row=1,column=3, sticky=W+E+S)
    tree2.heading('ProductID', text="ProductID",anchor=W)
    tree2.heading('Product Name', text="Product Name",anchor=W)
    tree2.heading('Product Qty', text="Product Qty",anchor=W)
    tree2.heading('Product Price', text="Product Price",anchor=W)
    tree2.column('#0', stretch=NO, minwidth=0, width=0)
    tree2.column('#1', stretch=NO, minwidth=0, width=0)
    tree2.column('#2', stretch=NO, minwidth=0, width=150)
    tree2.column('#3', stretch=NO, minwidth=0, width=90)
    tree2.column('#4', stretch=NO, minwidth=0, width=90)
    tree2.grid(row=0,column=3)

    
    #=========================Buttons==================================
    btns_l = Frame(f3, relief=FLAT, bg="powder blue", bd=10)
    btns_l.grid(row=3, column=0, columnspan=3, padx=50,pady=5)
    gbill_btn= Button(btns_l, text= 'Generate Bill', font=('arial', 16), width=10)
    gbill_btn.grid(row=0, column=1,padx=10, pady=5, sticky=E)
    total_btn= Button(btns_l, text= 'Total', font=('arial', 16), width=10)
    total_btn.grid(row=0, column=2,padx=10, pady=5, sticky=E)
    clear_btn= Button(btns_l, text= 'Clear', font=('arial', 16), width=10)
    clear_btn.grid(row=0, column=3,padx=10, pady=5, sticky=E)
    exit_btn= Button(btns_l, text= 'Exit', font=('arial', 16), width=10)
    exit_btn.grid(row=0, column=4,padx=10, pady=5, sticky=E)
    
   



def AddNew():
    Database()
    cursor.execute("INSERT INTO `product` (product_name, product_qty, product_price) VALUES(?, ?, ?)", (str(PRODUCT_NAME.get()), int(PRODUCT_QTY.get()), int(PRODUCT_PRICE.get())))
    conn.commit()
    PRODUCT_NAME.set("")
    PRODUCT_PRICE.set("")
    PRODUCT_QTY.set("")
    cursor.close()
    conn.close()

def DisplayData():
    Database()
    cursor.execute("SELECT * FROM `product`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Search():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `product` WHERE `product_name` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
            
        cursor.close()
        conn.close()
def clear_search(Event):
    #search.delete(0, Entry.END)
    SEARCH.set("")
    
def Reset():
    tree.delete(*tree.get_children())
    DisplayData()
    SEARCH.set("")

def Delete():
    if not tree.selection():
       print("ERROR")
    else:
        result = tkMessageBox.askquestion('Inventory Management System', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `product` WHERE `product_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
    



def Logout():
    result = tkMessageBox.askquestion('Inventory Management System', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes': 
        admin_id = ""
        employee_id = ""
        changepage()

def AdminLogin(event=None):
    global admin_id, chk
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
     
    else:
        
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")
            chk = 1
            changepage()
    
            AdminHome()
            #time.sleep(.3)
        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
        #cursor.close()
        conn.close() 
def EmpLogin(event=None):
    global employee_id, chk
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
     
    else:
        
        cursor.execute("SELECT * FROM `employee` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `employee` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            employee_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")
            chk = 2
            changepage()
            EmpHome()
           
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
def remove_menu():
    root.config(menu="")
    root.title("")
def menu1(root):
    root.title("Inventory Management System")
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Account", command=Admin_LoginForm)
    filemenu.add_command(label="Exit", command=Exit)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)
def menu2(root):
    root.title("Inventory Management System/Administrator")
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Logout", command=Logout)
    filemenu.add_command(label="Exit", command=Exit)
    menubar.add_cascade(label="Account", menu=filemenu)
    root.config(menu=menubar)
def menu3(root):
    root.title("Inventory Management System/Sales")
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Search", command=Logout)
    filemenu.add_command(label="Print", command=Logout)
    filemenu.add_command(label="Exit", command=Exit)
    menubar.add_cascade(label="File", menu=filemenu)
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


    btn_admin = tk.Button(login_dis, text="Admin Login", command=Admin_LoginForm, font=('arial', 20) )
    btn_admin.pack(side=TOP, padx=10, pady=10)
    btn_empl = tk.Button(login_dis, text="Employee Login", command=Emp_LoginForm, font=('arial', 20))
    btn_empl.pack(side=TOP, padx=10, pady=10)

def changepage():
    global pagenum, root
    for widget in root.winfo_children():
        widget.destroy()
        remove_menu()
    if pagenum == 1 and chk == 1:
        page2(root)
        menu2(root)
        pagenum = 2
    
    elif pagenum == 1 and chk == 2:
        page3(root)
        menu3(root)
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
