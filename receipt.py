import tkinter as tk
from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk
Lists = []
#====================Variables==================
SEARCH = StringVar()
cust_name = StringVar()
phone = StringVar() 
bill = StringVar()
#=====================    =====================
#=========Front End=============main Frame and widgets=====================================
def page5(root, deactivate): #this makes Deactivate to b activated in
    #Main Screen and also on Receipt Screen
    global tree,txtReceipt
    
    f5= Frame(root, bg="blue")
    f5.pack(fill = BOTH)
    top_f= Frame(f5)
    top_f.pack(side=TOP,fill = X,pady=3,padx=3)
    tool_bar = Frame(top_f, relief=RAISED, bg="powder blue", bd=4)
    tool_bar.pack(side=TOP,fill = X)
    lbl_text = Label(tool_bar, text="View Receipt", font=('arial', 18), bg="powder blue")
    lbl_text.pack(pady=3)
    print(deactivate)
    
    #========================Buttons & entries==================
    top = Frame(top_f, relief=RIDGE, bg="powder blue", bd=4)
    top.pack(fill = X)
    
    cust_lbl = Label(top, text='Customer name:', font=('arial', 12), bg="powder blue")
    cust_lbl.grid(row=0, column=0, sticky=W,padx=10)
    cust_ent= Entry(top, textvariable = cust_name, width=20)
    cust_ent.grid(row=0, column=1, sticky=W, padx=20)
             
    bill_lbl = Label(top, text='Bill No:', font=('arial', 12), bg="powder blue")
    bill_lbl.grid(row=0, column=2, sticky=W, padx=10)
    bill_ent= Entry(top, textvariable = SEARCH, width=20)
    bill_ent.grid(row=0, column=3, sticky=E, padx=20)
    search_btn= Button(top, text ='Search', font=('arial', 14), width=10, bg="blue", command = Search)
    search_btn.grid(row=0,column=4,padx=20, pady=3,sticky=E)
    
    del_btn= Button(top, text ='Delete', font=('arial', 14), width=10, bg="blue", command = Delete)
    del_btn.grid(row=0,column=5,padx=20, pady=3,sticky=E)
    view_btn= Button(top, text ='View', font=('arial', 14), width=10, bg="blue", command = get1_R)
    view_btn.grid(row=0,column=6,padx=20, pady=3,sticky=E)
    print_btn= Button(top, text ='Print', font=('arial', 14), width=10, bg="blue", command = get1_R)
    print_btn.grid(row=0,column=7,padx=20, pady=3,sticky=E)
    
    #================= Display Frame ==================
    inv_f =Frame(f5, bg="light blue")
    inv_f.pack(side=TOP,fill = BOTH, pady=5,padx=3) 
    #===================    ==========================
    display_f=Frame(inv_f)
    display_f.pack(side=LEFT,anchor=W, expand= TRUE)
    scrollbarx = Scrollbar(display_f, orient=HORIZONTAL)
    scrollbary = Scrollbar(display_f, orient=VERTICAL)
    tree = ttk.Treeview(display_f, columns=("ReceiptID", "Customer Name","Phone No", "Bill No", "Product Name", "Product Quantity", "Product Price", "Product Total"), selectmode="extended",\
         height=28, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('ReceiptID', text="ReceiptID",anchor=W)
    tree.heading('Customer Name', text="Customer Name",anchor=W)
    tree.heading('Phone No', text="Phone No",anchor=W)
    tree.heading('Bill No', text="Bill No",anchor=W)
    tree.heading('Product Name', text="Product Name ",anchor=W)
    tree.heading('Product Quantity', text="Quantity",anchor=W)
    tree.heading('Product Price', text="Price",anchor=W)
    tree.heading('Product Total', text="Total",anchor=W)
    
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=140)
    tree.column('#3', stretch=NO, minwidth=0, width=110)
    tree.column('#4', stretch=NO, minwidth=0, width=65)
    tree.column('#5', stretch=NO, minwidth=0, width=100)
    tree.column('#6', stretch=NO, minwidth=0, width=60)
    tree.column('#7', stretch=NO, minwidth=0, width=60)
    tree.column('#8', stretch=NO, minwidth=0, width=60)
    tree.pack(side=LEFT, fill= BOTH)
    tree.bind('<<TreeviewSelect>>', select_item)
    DisplayReceipt()
    ###=======================Text Display================
    receipt_f=Frame(inv_f)
    receipt_f.pack(side=RIGHT, anchor=E)
    #scrollbar_x = Scrollbar(receipt_f, orient=HORIZONTAL)
    txtReceipt = Text(receipt_f, height=40,bd=2,font=('arial',8,'bold'))
    txtReceipt.pack(side=LEFT, fill= Y)
    scrollbary = Scrollbar(receipt_f, orient=VERTICAL, command=txtReceipt.yview)
    scrollbary.pack(side=LEFT, anchor=W, fill=Y)
    txtReceipt.configure(yscrollcommand=scrollbary.set)
    if deactivate == 1:
        deactivate = 0
#=================================================================================
def connection():
    global conn, cursor
    conn = sqlite3.connect("irs.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `product` (product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, product_name TEXT,product_category TEXT,Initial_stock TEXT,Stock_available TEXT, product_price TEXT, product_colour TEXT, product_size TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `receipt` (receipt_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, customer_name TEXT,phone_no TEXT,bill_no TEXT,product_name TEXT, product_quantity TEXT, product_price TEXT, product_total TEXT)")

def DisplayReceipt():
    connection()
    cursor.execute("SELECT * FROM `receipt`")
    fetch = cursor.fetchall()
    for data in fetch:
        #print(data)
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
def select_item(event):
    connection()
    print(tree.selection()) #Used for deburging
    item = tree.selection()
    for i in item:
        try:
            global selected_item
            selected_item = tree.item(i, 'values')
            
            print(selected_item) #Used for deburging
            
            
        except IndexError:
            pass

def Search():
    if SEARCH.get() != "":
        global fetch
        tree.delete(*tree.get_children())
        connection()
        cursor.execute("SELECT * FROM `receipt` WHERE `bill_no` LIKE ?", ('%'+str(SEARCH.get())+'%',))
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
    DisplayReceipt()
    SEARCH.set("")

def Delete():
    item = tree.get_children()
    for i in item:       
        print(i)#for debugging purpose
        #child = tree.item(i,"values")
        
        
    
        result = tkMessageBox.askquestion('Inventory Management System', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            contents =tree.item(i,"values")
            #contents = [contents[3]]
            print(contents)
            Reset()
            connection()
            cursor.execute("DELETE FROM receipt WHERE bill_no=?",(contents[3],))
            conn.commit()
            cursor.close()
            conn.close()
            tree.delete(*tree.get_children())
            DisplayReceipt()
            

def get1_R():
    global fetch
    if fetch:
        global Lists
        Lists = []
        BillString =""
        """connection() 
        cursor.execute("SELECT * FROM `receipt` WHERE `bill_no` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()"""
        #print(fetch[1]) #for debuging purposes only 
        clear()
        
        for a in fetch:
            listDick = {"name":a[4], "quantity":a[5], "price":a[6]}
            Lists.append(listDick)
            print(Lists)
        for fetch in fetch:
            
            BillString =""
            BillString +="\n=====================Receipt=======================\n"
            BillString +="\n{:<20}{:<17}{:<5}".format("Bill no:", str(fetch[3]), "")
            BillString +="\n{:<20}{:<17}{:<5}".format("Customer:", fetch[1], "")
            BillString +="\n{:<20}{:<17}{:<5}".format("Phone no:", str(fetch[2]), "")
            BillString +="\n==================================================="
            BillString +="\n{:<20}{:<12}{:<10}".format("Product", "Quantity", "Price")
            BillString +="\n==================================================="
            for a in Lists:
                
                BillString +="\n{:<20}{:<12}{:<10}".format(a["name"], a["quantity"], a["price"])
            #print("{:<20}{:<12}{:10}".format(a["name"], a["quantity"], a["price"]))
            BillString +="\n===================================================\n"
            BillString +="\n{:<20}{:<12}{:<10}".format("Total Cost", " ", str(fetch[7]))
        if BillString:
            #txtReceipt.delete('1.0',END)
            txtReceipt.insert(END,f"\n\n------------------------------------------------------------------------------------------------------------------------")
            txtReceipt.insert(END,f"\n------------------------------------------------------------------------------------------------------------------------\n")
            txtReceipt.insert(END, BillString)
            print(BillString)
            
    """cursor.close()
    conn.close()   """ 
def clear():
    SEARCH.set("")
