from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk

global back
#========================================VARIABLES========================================
PRODUCT_NAME = StringVar()
PRODUCT_PRICE = IntVar()
PRODUCT_QTY = IntVar()
PRODUCT_QTY2 = IntVar()
PRODUCT_SIZE = StringVar()
PRODUCT_COLOUR = StringVar()
PRODUCT_CATEGORY = StringVar()
SEARCH = StringVar()

#========================================METHODS==========================================
def connection():
    global conn, cursor
    conn = sqlite3.connect("irs.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `product` (product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, product_name TEXT,product_category TEXT,Initial_stock TEXT,Stock_available TEXT, product_price TEXT, product_colour TEXT, product_size TEXT)")

def page2(root, back):
    global tree
    print(back)
    #deactivate =0
    f2 = Frame(root, bg="green")
    f2.pack(fill = BOTH)
    add_f = Frame(f2, bd=5, relief=SUNKEN, width = 600)
    add_f.pack(anchor=W, side = LEFT, fill = Y, padx=5, pady=2)
    top = Frame(add_f, bd=1, relief=SOLID)
    top.pack(anchor = W, fill = X)
    lbl_text = Label(top, text="Add New Product", font=('arial', 18))
    lbl_text.pack(side = TOP, pady=10)
    #======================Product Add=======================
    
    MidAddNew = Frame(add_f)
    MidAddNew.pack(side=TOP, anchor = W, pady=30)
    lbl_productname = Label(MidAddNew, text="Product Name:", font=('arial', 14))
    lbl_productname.grid(row=0, sticky=W, pady=10)
    productname = Entry(MidAddNew, textvariable=PRODUCT_NAME, font=('arial', 14), width=15)
    productname.grid(row=0, column=1)
    lbl_qty = Label(MidAddNew, text="Initial Stock:", font=('arial', 14))
    lbl_qty.grid(row=1, sticky=W, pady=10)
    productqty = Entry(MidAddNew, textvariable=PRODUCT_QTY, font=('arial', 14), width=15)
    productqty.grid(row=1, column=1)
    lbl_price = Label(MidAddNew, text="Product Price:", font=('arial', 14), bd=2)
    lbl_price.grid(row=2, sticky=W, pady=10)
    productprice = Entry(MidAddNew, textvariable=PRODUCT_PRICE, font=('arial', 14), width=15)
    productprice.grid(row=2, column=1)
    lbl_colour = Label(MidAddNew, text="Product Colour:", font=('arial', 14), bd=2)
    lbl_colour.grid(row=3, sticky=W, pady=10)
    productcolour = Entry(MidAddNew, textvariable=PRODUCT_COLOUR, font=('arial', 14), width=15)
    productcolour.grid(row=3, column=1)
    lbl_size = Label(MidAddNew, text="Product Size:", font=('arial', 14), bd=2)
    lbl_size.grid(row=4, sticky=W, pady=10)
    productsize = Entry(MidAddNew, textvariable=PRODUCT_SIZE, font=('arial', 14), width=15)
    productsize.grid(row=4, column=1)
    lbl_cartgory = Label(MidAddNew, text="Category:", font=('arial', 14), bd=2)
    lbl_cartgory.grid(row=5, sticky=W, pady=10)
    productCart = Entry(MidAddNew, textvariable=PRODUCT_CATEGORY, font=('arial', 14), width=15)
    productCart.grid(row=5, column=1)
    lbl_Cstock = Label(MidAddNew, text="Current Stock:", font=('arial', 14), bd=2)
    lbl_Cstock.grid(row=6, sticky=W, pady=10)
    productCstock = Entry(MidAddNew, textvariable=PRODUCT_QTY2, font=('arial', 14), width=15)
    productCstock.grid(row=6, column=1)
    btn_add = Button(MidAddNew, text="Save Products", font=('arial', 16), width=20, bg="#009ACD", command=AddNew)
    btn_add.grid(row=7, columnspan=2, pady=5)
    btn_add = Button(MidAddNew, text="Save Products", font=('arial', 16), width=20, bg="#009ACD", command=AddNew)
    btn_update = Button(MidAddNew, text="Update Products", font=('arial', 16), width=20, bg="#009ACD", command=update_data)
    btn_update.grid(row=8, columnspan=2, pady=5)
    
    #===================== Product View======================
    view_f = Frame(f2, bd=5, relief=SUNKEN, width = 600)
    view_f.pack(anchor=E, side = RIGHT, fill = Y, padx=5, pady=2)
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
    tree = ttk.Treeview(MidViewForm, columns=("ProductID", "Product Name","Category","Initial Stock", "Stock Available", "Product Price", "Product Colour", "Product Size"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('ProductID', text="ProductID",anchor=W)
    tree.heading('Product Name', text="Product Name",anchor=W)
    tree.heading('Category', text="Category",anchor=W)
    tree.heading('Initial Stock', text="Initial Stock",anchor=W)
    tree.heading('Stock Available', text="Stock Available",anchor=W)
    tree.heading('Product Price', text="Product Price",anchor=W)
    tree.heading('Product Colour', text="Product Colour",anchor=W)
    tree.heading('Product Size', text="Product Size",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=110)
    tree.column('#4', stretch=NO, minwidth=0, width=70)
    tree.column('#5', stretch=NO, minwidth=0, width=90)
    tree.column('#6', stretch=NO, minwidth=0, width=100)
    tree.column('#7', stretch=NO, minwidth=0, width=120)
    tree.column('#8', stretch=NO, minwidth=0, width=120)
    tree.pack()
    tree.bind('<<TreeviewSelect>>', select_item)
    DisplayData()
   
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
            PRODUCT_NAME.set(data_[1])
            PRODUCT_CATEGORY.set(data_[2])
            PRODUCT_QTY2.set(data_[4])
            PRODUCT_QTY.set(data_[3])
            PRODUCT_PRICE.set(data_[5])
            PRODUCT_COLOUR.set(data_[6])
            PRODUCT_SIZE.set(data_[7])
            
            print (data_[6])
            
        except IndexError:
            pass
def clear():    
    data_ = []
    PRODUCT_NAME.set("")
    PRODUCT_PRICE.set("")
    PRODUCT_QTY.set("")
    PRODUCT_COLOUR.set("")
    PRODUCT_SIZE.set("")
    PRODUCT_CATEGORY.set("")
    PRODUCT_QTY2.set("")
    
def verifier():
    if PRODUCT_NAME.get() == "" or PRODUCT_PRICE.get() == "" or PRODUCT_QTY.get() == "" or PRODUCT_QTY2.get() == "":
        tkMessageBox.showwarning("Warning", "Please fill Make sure Product Name, initial stock, product price and current stock are filled correctly")
        return 1
    else:
        return 0
def AddNew():
    ret=verifier()
    if ret==0:
        connection()
        cursor.execute("INSERT INTO `product` (product_name, product_category, Initial_stock, Stock_available, product_price, product_colour, product_size) VALUES(?, ?, ?, ?, ?, ?, ?)", (str(PRODUCT_NAME.get()), str(PRODUCT_CATEGORY.get()), int(PRODUCT_QTY.get()), str(PRODUCT_QTY2.get()), int(PRODUCT_PRICE.get()), str(PRODUCT_COLOUR.get()), str(PRODUCT_SIZE.get())))
        conn.commit()
        cursor.close()
        conn.close()
        tree.delete(*tree.get_children())
        DisplayData()
        clear()
    
def update_data():
    ret=verifier()
    if ret==0:
        print("....")
        print(data_[0])
        connection()
        cursor.execute("UPDATE product SET product_name=?, product_category=?, Initial_stock=?, Stock_available=?, product_price=?, product_colour=?, product_size=? WHERE product_id=?", (str(PRODUCT_NAME.get()), str(PRODUCT_CATEGORY.get()), int(PRODUCT_QTY.get()), str(PRODUCT_QTY2.get()), int(PRODUCT_PRICE.get()), str(PRODUCT_COLOUR.get()), str(PRODUCT_SIZE.get()), data_[0]))
        conn.commit()
        cursor.close()
        conn.close()
        tree.delete(*tree.get_children())
        DisplayData()
        clear()

def DisplayData():
    connection()
    cursor.execute("SELECT * FROM `product`")
    fetch = cursor.fetchall()
    for data in fetch:
        print(data)
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Search():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        connection()
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
    clear()

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
            clear()
    
