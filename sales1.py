import tkinter as tk
from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk
import random
from datetime import datetime 

global back
#define string so that label can display it
#t_str = time.strftime('%I:%M %p')

SEARCH = StringVar()
#====================list Values===============

value=""
Lists=[]
#==============display variables===========
cust_name = StringVar()
phone = StringVar() 
name_ = ""
#n = str()
phone_ = ""
bill = StringVar()
products = StringVar()
category = StringVar()
subegory = StringVar() 
quantity = IntVar()
show_t = StringVar()

stock = IntVar()
old = IntVar()
price = IntVar()
CustomerRef = StringVar()
TotalCost = 0.0
PaidTax= StringVar()
TotalCostVar=StringVar()
SubTotal=StringVar()


quantity.set("")
stock.set("")
CustomerRef.set("")

 
"""def update_t():
    global t_str,show_t
    t_str = time.strftime('%I:%M:%S %p')
    #Use config to update Label
    show_t.set(t_str)"""
    

def page3(root, back):
    global show_t,n,tree,name_,cust_ent,quantity_ent,products_ent
    global price_ent,in_stock,tree2,t_str
    back = 1
    
    
    f3= Frame(root, bg="blue")
    f3.pack(fill = BOTH)
    top_f= Frame(f3)
    top_f.pack(side=TOP,fill = X,pady=3,padx=3)
    tool_bar = Frame(top_f, relief=RAISED, bg="powder blue", bd=4)
    tool_bar.pack(side=TOP,fill = X)
    
    
    e_bar = Frame(tool_bar, relief=RAISED, bg="powder blue")
    e_bar.pack(side=RIGHT,padx=(320,0), anchor=NE)
    c_bar = Frame(tool_bar, relief=RAISED, bg="powder blue")
    c_bar.pack(side=RIGHT, anchor=W)
    
    lbl_text = Label(c_bar, text="View Products", font=('arial', 18), bg="powder blue")
    lbl_text.pack(anchor=CENTER)
    time_lbl =tk.Label(e_bar,textvariable=show_t, font =("Helvetica",15), bg="powder blue")
    time_lbl.pack(side=TOP,anchor=E)
    """btn_logout = Button(tool_bar, text = "Logout", bg="blue")
    btn_logout.pack(side= LEFT, anchor=NW)
    btn_exit = Button(tool_bar, text = "Exit", bg="red")
    btn_exit.pack(side= RIGHT, anchor=NE)"""
    #========================Buttons==================
    top = Frame(top_f, relief=RIDGE, bg="powder blue", bd=4)
    top.pack(fill = X)
    cust_lbl = Label(top, text='Customer name:', font=('arial', 12), bg="powder blue")
    cust_lbl.grid(row=0, column=0, sticky=W,padx=10)
    cust_ent= Entry(top, textvariable = cust_name, width=20)
    cust_ent.grid(row=0, column=1, sticky=W, padx=20)
    
    phone_lbl = Label(top, text='Phone No:', font=('arial', 12), bg="powder blue")
    phone_lbl.grid(row=0, column=2, sticky=W,padx=10)
    phone_ent= Entry(top, textvariable = phone, width=20)
    phone_ent.grid(row=0, column=3, sticky=W, padx=20)
             
    bill_lbl = Label(top, text='Bill No:', font=('arial', 12), bg="powder blue")
    bill_lbl.grid(row=0, column=4, sticky=W, padx=10)
    bill_ent= Entry(top, textvariable = bill, width=20)
    bill_ent.grid(row=0, column=5, sticky=E, padx=20)
    search_btn= Button(top, text ='Search', font=('arial', 14), width=10, bg="blue")
    search_btn.grid(row=0,column=6,padx=20, pady=3,sticky=E)
    #=======================Invisible  FRAME====================
    inv_f =Frame(f3, bg="light blue")
    inv_f.pack(side=TOP,fill = X, pady=5,padx=3) 
    #============= inputing product details===========
    entry_l = Frame(inv_f, relief=GROOVE, bg="powder blue", bd=1)
    entry_l.pack(side=LEFT, anchor=W,pady=3, padx=3)
    products_lbl = Label(entry_l, text='Product :', font=('arial', 16), bg="powder blue")
    products_lbl.grid(padx=2, sticky=W)
    products_ent = Entry(entry_l, textvariable = SEARCH, width=10, font=('arial', 16))
    products_ent.grid(row=0, column=1,padx=20)
    view_btn= Button(entry_l, text= 'View', command=Search, font=('arial', 10))
    view_btn.grid(row=1, column=1,padx=10, pady=3, sticky=E)
    category_lbl = Label(entry_l, text='Category :', font=('arial', 16), bg="powder blue")
    category_lbl.grid(row=2, column=0,padx=2, pady=10, sticky=W)
    category_ent = Entry(entry_l, textvariable= category, width=10, font=('arial', 16))
    category_ent.grid(row=2, column=1,pady=5,padx=20)
    subegory_lbl = Label(entry_l, text='Sub Category :', font=('arial', 16), bg="powder blue")
    subegory_lbl.grid(row=3, column=0,padx=2, pady=10, sticky=W)
    subegory_ent = Entry(entry_l, textvariable= subegory,width=10, font=('arial', 16))
    subegory_ent.grid(row=3, column=1,pady=5,padx=20)
    quantity_lbl = Label(entry_l, text='Quantity :', font=('arial', 16), bg="powder blue")
    quantity_lbl.grid(row=4, column=0,padx=2, pady=10, sticky=W)
    quantity_ent = Entry(entry_l, textvariable= quantity,width=10, font=('arial', 16))
    quantity_ent.grid(row=4, column=1,pady=5,padx=20)
    quantity_ent.bind("<Button-1>", clear_Q)#shld clr quantity entry and 
    quantity.trace('w', my_tracer)
    in_stock = Label(entry_l, textvariable= stock, bg="powder blue")
    in_stock.grid(row=5, column=0,pady=5,padx=20)
    price_lbl = Label(entry_l, text='Price :', font=('arial', 16), bg="powder blue")
    price_lbl.grid(row=6, column=0,padx=2, pady=10, sticky=W)
    price_ent = Entry(entry_l, textvariable= price,width=10, font=('arial', 16))
    price_ent.grid(row=6, column=1,pady=5,padx=20)
    cart_btn= Button(entry_l, text= 'Add to Cart', font=('arial', 16), width=10, command = add_to_cart)
    cart_btn.grid(row=7, column=0, pady=10, sticky=E)
    clearp_btn= Button(entry_l, text= 'Clear', font=('arial', 16), width=10, command = Clear_btn)
    clearp_btn.grid(row=7, column=1,padx=10, pady=20, sticky=E)
    
    
    #========================Calculator===================================
    displa_f=Frame(inv_f, bd=4)
    displa_f.pack(side=RIGHT, anchor=E)
    display_f=Frame(displa_f)
    display_f.pack(side=LEFT, expand= TRUE)
    scrollbarx = Scrollbar(display_f, orient=HORIZONTAL)
    scrollbary = Scrollbar(display_f, orient=VERTICAL)
    tree = ttk.Treeview(display_f, columns=("ProductID", "Product Name","Category", "Stock Available", "Product Price", "Product Size"), selectmode="extended",\
         height=22, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('ProductID', text="ProductID",anchor=W)
    tree.heading('Product Name', text="Product Name",anchor=W)
    tree.heading('Category', text="Category",anchor=W)
    tree.heading('Stock Available', text="Quantity",anchor=W)
    tree.heading('Product Price', text="Price",anchor=W)
    tree.heading('Product Size', text="Size",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=140)
    tree.column('#3', stretch=NO, minwidth=0, width=110)
    tree.column('#4', stretch=NO, minwidth=0, width=60)
    tree.column('#5', stretch=NO, minwidth=0, width=60)
    tree.column('#6', stretch=NO, minwidth=0, width=60)
    tree.pack(side=LEFT, fill= BOTH)
    tree.bind('<<TreeviewSelect>>', select_item)
    DisplayData()
    ##=============End of invisible Frame============
    
    receipt_f=Frame(displa_f)
    receipt_f.pack(side=RIGHT, anchor=E)
    T_f=Frame(receipt_f)
    T_f.pack(side=BOTTOM, fill=X)
    Tcost = Label(T_f, textvariable= TotalCostVar)
    Tcost.pack(anchor = CENTER)
    
    scrollbary = Scrollbar(receipt_f, orient=VERTICAL)
    tree2 = ttk.Treeview(receipt_f,height=22, columns=("ProductID", "Product Name", \
        "Purchased Stock", "Product Price","New Productqty"), selectmode="extended", yscrollcommand=scrollbary.set)
    scrollbary.config(command=tree2.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    tree2.heading('ProductID', text="ProductID",anchor=W)
    tree2.heading('Product Name', text="Product Name",anchor=W)
    tree2.heading('Purchased Stock', text="Purchased Stock",anchor=W)
    tree2.heading('Product Price', text="Product Price",anchor=W)
    tree2.heading('New Productqty', text="New Productqty",anchor=W)
    tree2.column('#0', stretch=NO, minwidth=0, width=0)
    tree2.column('#1', stretch=NO, minwidth=0, width=0)
    tree2.column('#2', stretch=NO, minwidth=0, width=150)
    tree2.column('#3', stretch=NO, minwidth=0, width=90)
    tree2.column('#4', stretch=NO, minwidth=0, width=90)
    tree2.column('#5', stretch=NO, minwidth=0, width=60)
    tree2.pack()

    
    #=========================Buttons==================================
    btns_l = Frame(f3, relief=FLAT, bg="powder blue", bd=2)
    btns_l.pack(side=BOTTOM,pady=3, padx= 3)
    gbill_btn= Button(btns_l, text= 'Generate Bill', font=('arial', 16), width=10)
    gbill_btn.grid(row=0, column=1,padx=10, pady=1, sticky=E)
    total_btn= Button(btns_l, text= 'Total', font=('arial', 16), width=10)
    total_btn.grid(row=0, column=2,padx=10, sticky=E)
    clear_btn= Button(btns_l, text= 'Clear', font=('arial', 16), width=10)
    clear_btn.grid(row=0, column=3,padx=10, sticky=E)
    print_btn= Button(btns_l, text= 'Print', font=('arial', 16), width=10,command = print_f)
    print_btn.grid(row=0, column=4,padx=10,  sticky=E)
    
   
  
def connection():
    global conn, cursor
    conn = sqlite3.connect("irs.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `product` (product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, product_name TEXT,product_category TEXT,Initial_stock TEXT,Stock_available TEXT, product_price TEXT, product_colour TEXT, product_size TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `receipt` (receipt_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, customer_name TEXT,phone_no TEXT,bill_no TEXT,product_name TEXT, product_quantity TEXT, product_price TEXT, product_total TEXT)")
    
def DisplayData():
    connection()
    cursor.execute("SELECT * FROM `product`")
    fetch = cursor.fetchall()
    for data in fetch:
        data = (data[0],data[1],data[2],data[4],data[5],data[7]) # gettting only the required data from Database
        print(data)
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
   

def Search():
    print("hi asshole")
    if SEARCH.get() != "":
        print("hi asshole")
        tree.delete(*tree.get_children())
        connection()
        cursor.execute("SELECT * FROM `product` WHERE `product_name` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            data = (data[0],data[1],data[2],data[4],data[5],data[7]) # gettting only the required data from Database
            print(data)
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
            connection()
            cursor.execute("DELETE FROM `product` WHERE `product_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
###===============for inserting selected items from Treeview to an entry Box=============== 
def check__():
    connection()
    global check_, selected_item
    #print(tree.selection()) #Used for deburging
    item = tree.selection()
    for i in item:
        global selected_item, old,stock_l
        selected_item = tree.item(i, 'values')
        check_ = int(selected_item[3])
        print(check_)
    
def select_item(event):
    check__()
    if check_ == 0:
        tkMessageBox.showwarning("Warning", "The Product Selected is Currently out of stock.")
        
    elif check_ <= 100:
        check1 = check_
        tkMessageBox.showwarning("Warning", "The Product Selected Stock is Currently below 100 parts. its available stock is currently: " + check1)
        
        print(selected_item) #Used for deburging
        products_ent.delete(0, END)
        products_ent.insert(END, selected_item[1])
        price_ent.delete(0, END)
        price_ent.insert(END, selected_item[4])
        #in_stock.delete(0, END)
        stock_l = int(selected_item[3])
        stock.set(int(selected_item[3]))
        
    else:
        print(selected_item) #Used for deburging
        products_ent.delete(0, END)
        products_ent.insert(END, selected_item[1])
        price_ent.delete(0, END)
        price_ent.insert(END, selected_item[4])
        #in_stock.delete(0, END)
        stock_l = int(selected_item[3])
        stock.set(int(selected_item[3]))
    
            

"""def stock_update():
    connection()
    if stock != 0:
        global new,new1
        old = float(stock.get())
        new1 = float(quantity.get())
        new = (old - new1)
    else:
        print("Out Of Stock")"""
def delete_Q():
    a = quantity.get()
    #print (a)
    if a == 0:
        stock.set("")
        stock.set(stock_l)
def my_tracer(a,b,c): #Trace send 3arguments to my_tracer
    #print(a, b, c)
    global new
    connection()  
    delete_Q()   
    if stock != 0:
        
        old = float(stock_l)
        new1 = float(quantity.get())
        new = old - new1
        stock.set(new)
    else:
        print("Out Of Stock")
#using StringVar 2 get & set text
  
    
"""    
def my_tracer2(a,b,c):
    
    #global name_
    if cust_ent:
        global name_
        name_ = (str(cust_name.get()))
        print(name_)
        
    if phone():
        phone_ = (str(phone.get()))
        txtReceipt.insert(END,f" Phone No: " + phone)
        
    else:
        p = phone.get()
        phone_.set(p)"""
        
def Clear_btn():
    cust_name.set("")
    phone.set("")
    bill.set("")
    products.set("")
    category.set("")
    subegory.set("") 
    quantity.set("")
    stock.set("")
    CustomerRef.set("")
    price.set("")
    #old = IntVar()
def clear_Q(Event):
    quantity.set("")
    stock.set("")
    stock.set(stock_l)
def add_to_cart():
    if SEARCH.get() != "":
        global Lists, TotalCost,TotalCostVar
        connection()
        #cost = price.get()
        #tree2.delete(*tree2.get_children())
        cursor.execute("SELECT * FROM `product` WHERE `product_name` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchone()
        qt = quantity.get()#get infor from entry label nd use it to update receipt/tree2
        #print(fetch[1]) ##for debuging purposes only 
        Item1=int(qt)
        ItemPrice =int(fetch[5]) # will help Calculate subt, total and tax
       
        PriceOfItem= ItemPrice*Item1
        SubTotalofItems=("%.2f"% PriceOfItem)
        SubTotal.set(SubTotalofItems)
        Tax=("%.2f"% ((PriceOfItem)*0.15))
        PaidTax.set(Tax)
        TTax  = ((PriceOfItem)*0.15)
        TCost = PriceOfItem+TTax
        TotalCost +=float(TCost)
        print("Tcost")
        print(TotalCost)
        
        data = (fetch[0],fetch[1],qt, TCost,int(new)) #new is suppose to update new quantity
        
        tree2.insert('', 'end', values=(data))
        TotalCostVar.set("Total Cost = {}".format(TotalCost))
        
        listDick = {"name":fetch[1], "quantity":qt, "price":TCost}
        Lists.append(listDick)
        print(Lists)
        
        """#for Adding remaining stock to Lists so later it's added to Database after customer buys
        cursor.execute("SELECT * FROM `product` WHERE `product_name` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchone()
        #print(fetch[1]) #for debuging purposes only 
        data = fetch[0] #
        print(data)
        stock_ = str(stock.get())#get infor from stock label nd use it to update LIST
        data2 =(stock_, data)
        print(data2)
        Lists.append(data2) """  
        cursor.close()
        conn.close()


def print_f():#it's capables of updating the new stock value once the print button is pressed
    global TotalCost
    TotalCostVar.set("")
    TotalCost = 0
    """print(Lists)
    item = txtReceipt.get("1.0","end-1c")
    print(item) #prints the whole receipt on the terminal
    Database()
    #updating a set of column where ID is applicable in the database
    sqlite_update = "Update product set Stock_available =? where product_id = ?" #"they supposed to 3
    cursor.executemany(sqlite_update, Lists)
    conn.commit()
    cursor.close()
    conn.close()"""
    CustomerRef.set(random.randint(1980, 9876722))
    c_bill = CustomerRef.get()
    c_name = cust_name.get()
    c_phone = phone.get()
    BillString =""
    BillString +="=====================Receipt=======================\n\n"
    BillString +="{:<20}{:<17}{:5}\n".format("Bill no:", c_bill, "")
    BillString +="{:<20}{:<17}{:5}\n".format("Customer:", c_name, "")
    BillString +="{:<20}{:<17}{:5}\n".format("Phone no:", c_phone, "")
    BillString +="===================================================\n"
    BillString +="{:<20}{:<12}{:10}\n".format("Product", "Quantity", "Price")
    BillString +="===================================================\n"
    """ print("=====================Receipt=======================")
    print("===================================================")
    print("{:<20}{:<12}{:10}".format("Product", "Quantity", "Price"))
    print("===================================================")"""
    for a in Lists:
        BillString +="{:<20}{:<12}{:10}\n".format(a["name"], a["quantity"], a["price"])
        #print("{:<20}{:<12}{:10}".format(a["name"], a["quantity"], a["price"]))
    BillString +="===================================================\n"
    BillString +="{:<20}{:<12}{:10}\n".format("Total Cost", " ", TotalCost)
    """print("===================================================") 
    print("{:<20}{:<12}{:10}".format("Total Cost", " ", TotalCost))"""  
    print(BillString)
    for a in Lists:
        connection()
        cursor.execute("INSERT INTO `receipt` (customer_name, phone_no, bill_no, product_name, product_quantity, product_price, product_total) VALUES(?, ?, ?, ?, ?, ?,?)", (c_name, c_phone, c_bill, a["name"], a["quantity"], a["price"], TotalCost))
        conn.commit()
        cust_name.set("")
        phone.set("")
        CustomerRef.set("")
        Lists = []
        BillString =""
        cursor.close()
        conn.close()
    item = tree2.get_children()
    for i in item:       
        print(i)#for debugging purpose
        child = tree2.item(i,"values")
        
        child = [child[4], child[0]]
        #print(child)#for debugging purpose
        ####===============Updating Database with new product quantity==============
        connection()
        
        sqlite_update = """Update product set Stock_available =? where product_id = ?""" #"they supposed to 3
        cursor.executemany(sqlite_update, [child])
        conn.commit()
        cursor.close()
        conn.close()
        tree2.delete(*tree.get_children())
      



