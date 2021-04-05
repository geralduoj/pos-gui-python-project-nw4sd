import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import Treeview

from classobjects import Laptop
from classobjects import Phone

root = Tk()
orders = []


def updatetable(orders):
    trv.delete(*trv.get_children())
    for i in orders:
        trv.insert('', 'end', values=(i.name, i.quantity, i.price))


def adddelltotable():
    delllappy = Laptop("Dell", 1000)
    orders.append(delllappy)
    updatetable(orders)


def addasustotable():
    asuslappy = Laptop("Asus", 800)
    orders.append(asuslappy)
    updatetable(orders)


wrapper1 = LabelFrame(root, text="Items")
wrapper2 = LabelFrame(root, text="Orders")
wrapper3 = LabelFrame(root, text="Totals")

wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="no", padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

asuslaptopBTN = Button(wrapper1, text="Asus", command=addasustotable)
asuslaptopBTN.pack()
delllaptopBTN = Button(wrapper1, text="Dell", command=adddelltotable)
delllaptopBTN.pack()

trv = Treeview(wrapper2, columns=(1,2,3), show="headings", height="10")
trv.pack()
trv.heading(1, text="Product")
trv.heading(2, text="Quantity")
trv.heading(3, text="Price")

for i in orders:
    trv.insert('', 'end', values=(i.name, i.quantity, i.price))

root.title("POS System")
root.geometry("800x700")
root.mainloop()
