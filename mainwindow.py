import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import Treeview

from classobjects import Laptop, Phone

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


def addiphone12totable():
    iphone12 = Phone("iPhone 12 Pro Max", 550)
    for item in orders:
        if item.name == iphone12.name:
            item.quantity += 1
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "iPhone 12 Pro Max"]
    if "iPhone 12 Pro Max" not in itemNames:
        orders.append(iphone12)
        ordersname.append("iPhone 12 Pro Max")
        updatetable(orders)


def addiphone11totable():
    iphone11 = Phone("iPhone 11 Pro", 400)
    for item in orders:
        if item.name == iphone11.name:
            item.quantity += 1
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "iPhone 11 Pro"]
    if "iPhone 11 Pro" not in itemNames:
        orders.append(iphone11)
        ordersname.append("iPhone 11 Pro")
        updatetable(orders)


def addsamsunggalaxytotable():
    samsunggalaxy = Phone("Samsung Galaxy Pro", 900)
    for item in orders:
        if item.name == samsunggalaxy.name:
            item.quantity += 1
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "Samsung Galaxy Pro"]
    if "Samsung Galaxy Pro" not in itemNames:
        orders.append(samsunggalaxy)
        ordersname.append("Samsung Galaxy Pro")
        updatetable(orders)


def addps4totable():
    ps4 = Phone("Play Station 4", 300)
    for item in orders:
        if item.name == ps4.name:
            item.quantity += 1
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "Play Station 4"]
    if "Play Station 4" not in itemNames:
        orders.append(ps4)
        ordersname.append("Play Station 4")
        updatetable(orders)


def addxboxonetotable():
    xboxone = Phone("XBOX ONE", 1000)
    for item in orders:
        if item.name == xboxone.name:
            item.quantity += 1
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "XBOX ONE"]
    if "XBOX ONE" not in itemNames:
        orders.append(xboxone)
        ordersname.append("XBOX ONE")
        updatetable(orders)


def addps5totable():
    ps5 = Phone("Play Station 5", 1100)
    for item in orders:
        if item.name == ps5.name:
            item.quantity += 1
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "Play Station 5"]
    if "Play Station 5" not in itemNames:
        orders.append(ps5)
        ordersname.append("Play Station 5")
        updatetable(orders)


def addxbox360totable():
    xbox360 = Phone("XBOX 360", 200)
    for item in orders:
        if item.name == xbox360.name:
            item.quantity += 1
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "XBOX 360"]
    if "XBOX 360" not in itemNames:
        orders.append(xbox360)
        ordersname.append("XBOX 360")
        updatetable(orders)


def addlg55totable():
    lg55 = Phone("LG 55inch TV", 780)
    for item in orders:
        if item.name == lg55.name:
            item.quantity += 1
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "LG 55inch TV"]
    if "LG 55inch TV" not in itemNames:
        orders.append(lg55)
        ordersname.append("LG 55inch TV")
        updatetable(orders)


def addsamsung55totable():
    samsung55 = Phone("Samsung 55inch TV", 780)
    for item in orders:
        if item.name == samsung55.name:
            item.quantity += 1
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "Samsung 55inch TV"]
    if "Samsung 55inch TV" not in itemNames:
        orders.append(samsung55)
        ordersname.append("Samsung 55inch TV")
        updatetable(orders)


def addsharp55totable():
    sharp55 = Phone("Sharp 40inch TV", 650)
    for item in orders:
        if item.name == sharp55.name:
            item.quantity += 1
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "Sharp 40inch TV"]
    if "Sharp 40inch TV" not in itemNames:
        orders.append(sharp55)
        ordersname.append("Sharp 40inch TV")
        updatetable(orders)


def addrca55totable():
    rca55 = Phone("RCA 40inch TV", 650)
    for item in orders:
        if item.name == rca55.name:
            item.quantity += 1
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "RCA 40inch TV"]
    if "RCA 40inch TV" not in itemNames:
        orders.append(rca55)
        ordersname.append("RCA 40inch TV")
        updatetable(orders)


def addtcl55totable():
    tcl55 = Phone("TCL 20inch TV", 230)
    for item in orders:
        if item.name == tcl55.name:
            item.quantity += 1
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "TCL 20inch TV"]
    if "TCL 20inch TV" not in itemNames:
        orders.append(tcl55)
        ordersname.append("TCL 20inch TV")
        updatetable(orders)


def addfifa20totable():
    fifa20 = Phone("Fifa 20", 20)
    for item in orders:
        if item.name == fifa20.name:
            item.quantity += 1
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "Fifa 20"]
    if "Fifa 20" not in itemNames:
        orders.append(fifa20)
        ordersname.append("Fifa 20")
        updatetable(orders)


def addfifa21totable():
    fifa21 = Phone("Fifa 21", 90)
    for item in orders:
        if item.name == fifa21.name:
            item.quantity += 1
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "Fifa 21"]
    if "Fifa 21" not in itemNames:
        orders.append(fifa21)
        ordersname.append("Fifa 21")
        updatetable(orders)


def addnba2k20totable():
    nba2k20 = Phone("NBA 2K 20", 20)
    for item in orders:
        if item.name == nba2k20.name:
            item.quantity += 1
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "NBA 2K 20"]
    if "NBA 2K 20" not in itemNames:
        orders.append(nba2k20)
        ordersname.append("NBA 2K 20")
        updatetable(orders)


def addnba2k21totable():
    nba2k21 = Phone("NBA 2K 21", 50)
    for item in orders:
        if item.name == nba2k21.name:
            item.quantity += 1
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "NBA 2K 21"]
    if "NBA 2K 21" not in itemNames:
        orders.append(nba2k21)
        ordersname.append("NBA 2K 21")
        updatetable(orders)


def addcodbopstotable():
    codbops = Phone("COD Black Ops 2", 10)
    for item in orders:
        if item.name == codbops.name:
            item.quantity += 1
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "COD Black Ops 2"]
    if "COD Black Ops 2" not in itemNames:
        orders.append(codbops)
        ordersname.append("COD Black Ops 2")
        updatetable(orders)


def addcodmwtotable():
    codmw = Phone("COD MW 2", 24)
    for item in orders:
        if item.name == codmw.name:
            item.quantity += 1
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "COD MW 2"]
    if "COD MW 2" not in itemNames:
        orders.append(codmw)
        ordersname.append("COD MW 2")
        updatetable(orders)


def addcodcoldwartotable():
    codcoldwar = Phone("COD Cold War", 100)
    for item in orders:
        if item.name == codcoldwar.name:
            item.quantity += 1
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "COD Cold War"]
    if "COD Cold War" not in itemNames:
        orders.append(codcoldwar)
        ordersname.append("COD Cold War")
        updatetable(orders)


wrapper1 = LabelFrame(root, text="Items")
wrapper2 = LabelFrame(root, text="Orders")
wrapper3 = LabelFrame(root, text="Totals")

wrapper1.pack(fill="both", expand="no", padx=20, pady=10)
wrapper2.pack(fill="both", expand="no", padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

asuslaptopBTN = Button(wrapper1, width=15, height=5, text="Asus Laptop", fg='white', bg='#FF5733', command=addasustotable)
asuslaptopBTN.grid(row=1,column=0)
delllaptopBTN = Button(wrapper1, width=10, height=5, fg='white', bg='#FF5733', text="Dell Laptop", command=adddelltotable)
delllaptopBTN.grid(row=1,column=1)
iphone12BTN = Button(wrapper1, width=15, height=5, fg='white', bg='#FF5733', text="iPhone 12 Pro Max", command=addiphone12totable)
iphone12BTN.grid(row=1,column=2)
samsungGalaxyBTN = Button(wrapper1, width=19, height=5, fg='white', bg='#FF5733', text="Samsung Galaxy Pro", command=addsamsunggalaxytotable)
samsungGalaxyBTN.grid(row=1,column=3)
iphone12BTN = Button(wrapper1, width=15, height=5, fg='white', bg='#FF5733', text="iPhone 11 Pro", command=addiphone11totable)
iphone12BTN.grid(row=1,column=4)
ps4BTN = Button(wrapper1, width=15, height=5, fg='white', bg='#FF5733', text="Play Station 4", command=addps4totable)
ps4BTN.grid(row=1,column=5)
xboxoneBTN = Button(wrapper1, width=13, height=5, fg='white', bg='#FF5733', text="XBOX ONE", command=addxboxonetotable)
xboxoneBTN.grid(row=1,column=6)
ps5BTN = Button(wrapper1, width=15, height=5, fg='white', bg='#FF5733', text="Play Station 5", command=addps5totable)
ps5BTN.grid(row=2,column=0)
xbox360BTN = Button(wrapper1, width=10, height=5, fg='white', bg='#FF5733', text="XBOX 360", command=addxbox360totable)
xbox360BTN.grid(row=2,column=1)
lgtvBTN = Button(wrapper1, width=15, height=5, fg='white', bg='#FF5733', text="LG 55inch TV", command=addlg55totable)
lgtvBTN.grid(row=2,column=2)
samsungtvBTN = Button(wrapper1, width=19, height=5, fg='white', bg='#FF5733', text="Samsung 55inch TV", command=addsamsung55totable)
samsungtvBTN.grid(row=2,column=3)
sharptvBTN = Button(wrapper1, width=15, height=5, fg='white', bg='#FF5733', text="Sharp 40inch TV", command=addsharp55totable)
sharptvBTN.grid(row=2,column=4)
rcatvBTN = Button(wrapper1, width=15, height=5, fg='white', bg='#FF5733', text="RCA 40inch TV", command=addrca55totable)
rcatvBTN.grid(row=2,column=5)
tcltvBTN = Button(wrapper1, width=13, height=5, fg='white', bg='#FF5733', text="TCL 20inch TV", command=addtcl55totable)
tcltvBTN.grid(row=2,column=6)
fifa20tvBTN = Button(wrapper1, width=15, height=5, fg='white', bg='#FF5733', text="Fifa 20", command=addfifa20totable)
fifa20tvBTN.grid(row=3,column=0)
fifa21tvBTN = Button(wrapper1, width=10, height=5, fg='white', bg='#FF5733', text="Fifa 21", command=addfifa21totable)
fifa21tvBTN.grid(row=3,column=1)
nba2k20tvBTN = Button(wrapper1, width=15, height=5, fg='white', bg='#FF5733', text="NBA 2K 20", command=addnba2k20totable)
nba2k20tvBTN.grid(row=3,column=2)
nba2k21tvBTN = Button(wrapper1, width=19, height=5, fg='white', bg='#FF5733', text="NBA 2K 21", command=addnba2k21totable)
nba2k21tvBTN.grid(row=3,column=3)
codbkops2tvBTN = Button(wrapper1, width=15, height=5, fg='white', bg='#FF5733', text="COD Black Ops 2", command=addcodbopstotable)
codbkops2tvBTN.grid(row=3,column=4)
codmw2tvBTN = Button(wrapper1, width=15, height=5, fg='white', bg='#FF5733', text="COD MW 2", command=addcodmwtotable)
codmw2tvBTN.grid(row=3,column=5)
codcoldwartvBTN = Button(wrapper1, width=13, height=5, fg='white', bg='#FF5733', text="COD Cold War", command=addcodcoldwartotable)
codcoldwartvBTN.grid(row=3,column=6)

trv = Treeview(wrapper2, columns=(1, 2, 3, 4), show="headings", height="10")
trv.pack()
trv.heading(1, text="Product")
trv.heading(2, text="Quantity")
trv.heading(3, text="Price")
trv.heading(4, text="Subtotal per Product")


root.title("POS System")
root.geometry("850x700")
root.mainloop()
