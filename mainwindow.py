import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import Treeview

from classobjects import Laptop

root = Tk()
orders = []
ordersname = []
#orders.append(delllappy)


def updatetable(orders):
    trv.delete(*trv.get_children())
    for i in orders:
        trv.insert('', 'end', values=(i.name, i.quantity, i.price, (i.quantity*i.price)))


def adddelltotable():
    delllappyy = Laptop("Dell Laptop", 1000)
    for item in orders:
        if item.name == delllappyy.name:
            item.quantity += 1
            updatetable(orders)

    dellNames = [p for p in ordersname if p == "Dell Laptop"]
    if "Dell Laptop" not in dellNames:
        orders.append(delllappyy)
        ordersname.append("Dell Laptop")
        updatetable(orders)


def addasustotable():
    asuslappyy = Laptop("Asus Laptop", 800)
    for item in orders:
        if item.name == asuslappyy.name:
            item.quantity += 1
            updatetable(orders)

    asusNames = [p for p in ordersname if p == "Asus Laptop"]
    if "Asus Laptop" not in asusNames:
        orders.append(asuslappyy)
        ordersname.append("Asus Laptop")
        updatetable(orders)


wrapper1 = LabelFrame(root, text="Items")
wrapper2 = LabelFrame(root, text="Orders")
wrapper3 = LabelFrame(root, text="Totals")

wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="no", padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

asuslaptopBTN = Button(wrapper1, text="Asus Laptop", command=addasustotable)
asuslaptopBTN.pack()
delllaptopBTN = Button(wrapper1, text="Dell Laptop", command=adddelltotable)
delllaptopBTN.pack()

trv = Treeview(wrapper2, columns=(1, 2, 3, 4), show="headings", height="10")
trv.pack()
trv.heading(1, text="Product")
trv.heading(2, text="Quantity")
trv.heading(3, text="Price")
trv.heading(4, text="Subtotal per Product")


root.title("POS System")
root.geometry("800x700")
root.mainloop()
