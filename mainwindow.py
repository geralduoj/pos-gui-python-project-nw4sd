import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import Treeview
import datetime as dt
import glob

from classobjects import Laptop, Phone, Consoles, ConsoleGames, Television

splash_screen = Tk()

splash_screen.geometry("850x700")
splash_screen['background']='#64ceff'
splash_screen.overrideredirect(True)

label = Label(splash_screen, text="Centennial College\n POS System")
label.configure(foreground="white",font=("connecticut",60))
label['background']='#64ceff'
label.pack()

label.place(relx = 0.5, rely = 0.5, anchor = 'center')

def splash():
    splash_screen.destroy()

splash_screen.after(1000,splash)

root = Tk()
root.resizable(width=False, height=False)

orders = []
ordersname = []
#orders.append(delllappy)

def updatetable(orders):
    trv.delete(*trv.get_children())
    for i in orders:
        trv.insert('', 'end', values=(i.name, i.quantity, i.price, (i.quantity*i.price)))


def adddelltotable():
    delllappyy = Laptop("Dell Laptop", 1000)
    subtotal = 0
    for item in orders:
        if item.name == delllappyy.name:
            item.quantity += 1
            subtotal += item.quantity * item.price
            item.subtotal = subtotal
            updatetable(orders)

    dellNames = [p for p in ordersname if p == "Dell Laptop"]
    if "Dell Laptop" not in dellNames:
        delllappyy.subtotal = 1000
        orders.append(delllappyy)
        ordersname.append("Dell Laptop")
        updatetable(orders)


def addasustotable():
    subtotal = 0
    asuslappyy = Laptop("Asus Laptop", 800)
    for item in orders:
        if item.name == asuslappyy.name:
            item.quantity += 1
            subtotal += item.quantity * item.price
            item.subtotal = subtotal
            updatetable(orders)

    asusNames = [p for p in ordersname if p == "Asus Laptop"]
    if "Asus Laptop" not in asusNames:
        asuslappyy.subtotal = 800
        orders.append(asuslappyy)
        ordersname.append("Asus Laptop")
        updatetable(orders)


def addiphone12totable():
    subtotal = 0
    iphone12 = Phone("iPhone 12 Pro Max", 550)
    for item in orders:
        if item.name == iphone12.name:
            item.quantity += 1
            subtotal += item.quantity * item.price
            item.subtotal = subtotal
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "iPhone 12 Pro Max"]
    if "iPhone 12 Pro Max" not in itemNames:
        iphone12.subtotal = 550
        orders.append(iphone12)
        ordersname.append("iPhone 12 Pro Max")
        updatetable(orders)


def addiphone11totable():
    subtotal = 0
    iphone11 = Phone("iPhone 11 Pro", 400)
    for item in orders:
        if item.name == iphone11.name:
            item.quantity += 1
            subtotal += item.quantity * item.price
            item.subtotal = subtotal
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "iPhone 11 Pro"]
    if "iPhone 11 Pro" not in itemNames:
        iphone11.subtotal = 400
        orders.append(iphone11)
        ordersname.append("iPhone 11 Pro")
        updatetable(orders)


def addsamsunggalaxytotable():
    subtotal = 0
    samsunggalaxy = Phone("Samsung Galaxy Pro", 900)
    for item in orders:
        if item.name == samsunggalaxy.name:
            item.quantity += 1
            subtotal += item.quantity * item.price
            item.subtotal = subtotal
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "Samsung Galaxy Pro"]
    if "Samsung Galaxy Pro" not in itemNames:
        samsunggalaxy.subtotal = 900
        orders.append(samsunggalaxy)
        ordersname.append("Samsung Galaxy Pro")
        updatetable(orders)


def addps4totable():
    subtotal = 0
    ps4 = Consoles("Play Station 4", 300)
    for item in orders:
        if item.name == ps4.name:
            item.quantity += 1
            subtotal += item.quantity * item.price
            item.subtotal = subtotal
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "Play Station 4"]
    if "Play Station 4" not in itemNames:
        ps4.subtotal = 300
        orders.append(ps4)
        ordersname.append("Play Station 4")
        updatetable(orders)


def addxboxonetotable():
    subtotal = 0
    xboxone = Consoles("XBOX ONE", 1000)
    for item in orders:
        if item.name == xboxone.name:
            item.quantity += 1
            subtotal += item.quantity * item.price
            item.subtotal = subtotal
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "XBOX ONE"]
    if "XBOX ONE" not in itemNames:
        xboxone.subtotal = 1000
        orders.append(xboxone)
        ordersname.append("XBOX ONE")
        updatetable(orders)


def addps5totable():
    subtotal = 0
    ps5 = Consoles("Play Station 5", 1100)
    for item in orders:
        if item.name == ps5.name:
            item.quantity += 1
            subtotal += item.quantity * item.price
            item.subtotal = subtotal
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "Play Station 5"]
    if "Play Station 5" not in itemNames:
        ps5.subtotal = 1100
        orders.append(ps5)
        ordersname.append("Play Station 5")
        updatetable(orders)


def addxbox360totable():
    subtotal = 0
    xbox360 = Consoles("XBOX 360", 200)
    for item in orders:
        if item.name == xbox360.name:
            item.quantity += 1
            subtotal += item.quantity * item.price
            item.subtotal = subtotal
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "XBOX 360"]
    if "XBOX 360" not in itemNames:
        xbox360.subtotal = 200
        orders.append(xbox360)
        ordersname.append("XBOX 360")
        updatetable(orders)


def addlg55totable():
    subtotal = 0
    lg55 = Television("LG 55inch TV", 780)
    for item in orders:
        if item.name == lg55.name:
            item.quantity += 1
            subtotal += item.quantity * item.price
            item.subtotal = subtotal
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "LG 55inch TV"]
    if "LG 55inch TV" not in itemNames:
        lg55.subtotal = 780
        orders.append(lg55)
        ordersname.append("LG 55inch TV")
        updatetable(orders)


def addsamsung55totable():
    subtotal = 0
    samsung55 = Television("Samsung 55inch TV", 780)
    for item in orders:
        if item.name == samsung55.name:
            item.quantity += 1
            subtotal += item.quantity * item.price
            item.subtotal = subtotal
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "Samsung 55inch TV"]
    if "Samsung 55inch TV" not in itemNames:
        samsung55.subtotal = 780
        orders.append(samsung55)
        ordersname.append("Samsung 55inch TV")
        updatetable(orders)


def addsharp55totable():
    subtotal = 0
    sharp55 = Television("Sharp 40inch TV", 650)
    for item in orders:
        if item.name == sharp55.name:
            item.quantity += 1
            subtotal += item.quantity * item.price
            item.subtotal = subtotal
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "Sharp 40inch TV"]
    if "Sharp 40inch TV" not in itemNames:
        sharp55.subtotal = 650
        orders.append(sharp55)
        ordersname.append("Sharp 40inch TV")
        updatetable(orders)


def addrca55totable():
    subtotal = 0
    rca55 = Television("RCA 40inch TV", 650)
    for item in orders:
        if item.name == rca55.name:
            item.quantity += 1
            subtotal += item.quantity * item.price
            item.subtotal = subtotal
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "RCA 40inch TV"]
    if "RCA 40inch TV" not in itemNames:
        rca55.subtotal = 650
        orders.append(rca55)
        ordersname.append("RCA 40inch TV")
        updatetable(orders)


def addtcl55totable():
    subtotal = 0
    tcl55 = Television("TCL 20inch TV", 230)
    for item in orders:
        if item.name == tcl55.name:
            item.quantity += 1
            subtotal += item.quantity * item.price
            item.subtotal = subtotal
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "TCL 20inch TV"]
    if "TCL 20inch TV" not in itemNames:
        tcl55.subtotal = 230
        orders.append(tcl55)
        ordersname.append("TCL 20inch TV")
        updatetable(orders)


def addfifa20totable():
    subtotal = 0
    fifa20 = ConsoleGames("Fifa 20", 20)
    for item in orders:
        if item.name == fifa20.name:
            item.quantity += 1
            subtotal += item.quantity * item.price
            item.subtotal = subtotal
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "Fifa 20"]
    if "Fifa 20" not in itemNames:
        fifa20.subtotal = 20
        orders.append(fifa20)
        ordersname.append("Fifa 20")
        updatetable(orders)


def addfifa21totable():
    subtotal = 0
    fifa21 = ConsoleGames("Fifa 21", 90)
    for item in orders:
        if item.name == fifa21.name:
            item.quantity += 1
            subtotal += item.quantity * item.price
            item.subtotal = subtotal
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "Fifa 21"]
    if "Fifa 21" not in itemNames:
        fifa21.subtotal = 90
        orders.append(fifa21)
        ordersname.append("Fifa 21")
        updatetable(orders)


def addnba2k20totable():
    subtotal = 0
    nba2k20 = ConsoleGames("NBA 2K 20", 20)
    for item in orders:
        if item.name == nba2k20.name:
            item.quantity += 1
            subtotal += item.quantity * item.price
            item.subtotal = subtotal
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "NBA 2K 20"]
    if "NBA 2K 20" not in itemNames:
        nba2k20.subtotal = 20
        orders.append(nba2k20)
        ordersname.append("NBA 2K 20")
        updatetable(orders)


def addnba2k21totable():
    subtotal = 0
    nba2k21 = ConsoleGames("NBA 2K 21", 50)
    for item in orders:
        if item.name == nba2k21.name:
            item.quantity += 1
            subtotal += item.quantity * item.price
            item.subtotal = subtotal
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "NBA 2K 21"]
    if "NBA 2K 21" not in itemNames:
        nba2k21.subtotal = 50
        orders.append(nba2k21)
        ordersname.append("NBA 2K 21")
        updatetable(orders)


def addcodbopstotable():
    subtotal = 0
    codbops = ConsoleGames("COD Black Ops 2", 10)
    for item in orders:
        if item.name == codbops.name:
            item.quantity += 1
            subtotal += item.quantity * item.price
            item.subtotal = subtotal
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "COD Black Ops 2"]
    if "COD Black Ops 2" not in itemNames:
        codbops.subtotal = 10
        orders.append(codbops)
        ordersname.append("COD Black Ops 2")
        updatetable(orders)


def addcodmwtotable():
    subtotal = 0
    codmw = ConsoleGames("COD MW 2", 24)
    for item in orders:
        if item.name == codmw.name:
            item.quantity += 1
            subtotal += item.quantity * item.price
            item.subtotal = subtotal
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "COD MW 2"]
    if "COD MW 2" not in itemNames:
        codmw.subtotal = 24
        orders.append(codmw)
        ordersname.append("COD MW 2")
        updatetable(orders)


def addcodcoldwartotable():
    subtotal = 0
    codcoldwar = ConsoleGames("COD Cold War", 100)
    for item in orders:
        if item.name == codcoldwar.name:
            item.quantity += 1
            subtotal += item.quantity * item.price
            item.subtotal = subtotal
            updatetable(orders)

    itemNames = [p for p in ordersname if p == "COD Cold War"]
    if "COD Cold War" not in itemNames:
        codcoldwar.subtotal = 100
        orders.append(codcoldwar)
        ordersname.append("COD Cold War")
        updatetable(orders)

    

def calculateQTY():
    totalqty = 0
    for item in orders:
        totalqty += item.quantity
    totalitemsqtyLABEL.config(text=str(totalqty))

    subtotal = 0
    for item in orders:
        subtotal += item.subtotal
    totalallsubamtLABEL.config(text=str(subtotal))
    taxTotaltxtLABEL.config(text=str(round(subtotal*0.13,2)))
    grandtotalalltxtLABEL.config(text=str(round(subtotal*0.13,2)+subtotal))
    
    global receipt
    receipt = Toplevel(root)
    receipt.title("Receipt")
    receipt.geometry("800x500")
    receipt.config(bg="white")
    
    infoFrame = Frame(receipt)
    itemsFrame = Frame(receipt)
    totalsFrame = Frame(receipt)
    optionsFrame = Frame(receipt)
    
    infoFrame.pack(expand="no", padx=20, pady=10)
    itemsFrame.pack(fill="both", expand="no", padx=20, pady=10)
    totalsFrame.pack(expand="no")
    optionsFrame.pack(expand="yes", padx=20, pady=10)
    
    labelSimplePOS = Label(infoFrame,text='Simple POS',font='Times 16 bold')
    labelSimplePOS.grid(row = 0, column = 1)
    
    labelAddress = Label(infoFrame,text = "My Shop Lot,Shopping Mall, Post Code, City",font = "Times 11")
    labelAddress.grid(row=1, column = 1)
    
    labelTelephone = Label(infoFrame,text = "Tel:0105292122",font = "Times 11")
    labelTelephone.grid(row=2, column =0)
    
    labelReceiptNumber = Label(infoFrame,text = "Sale Number:5",font = "Times 11")
    labelReceiptNumber.grid(row=2,column=2)
    
    labelDate = Label(infoFrame,text=f"Date:{dt.datetime.now():%a, %b %d %Y}",font = "Times 11")
    labelDate.grid(row=3,column=0)
    
    receiptDetails = Treeview(itemsFrame, columns=(1, 2, 3, 4), show="headings", height="10")
    receiptDetails.pack()
    receiptDetails.heading(1, text="Product")
    receiptDetails.heading(2, text="Quantity")
    receiptDetails.heading(3, text="Price")
    receiptDetails.heading(4, text="Subtotal per Product")

    receiptDetails.delete(*receiptDetails.get_children())
    for i in orders:
        receiptDetails.insert('', 'end', values=(i.name, i.quantity, i.price, (i.quantity * i.price)))
    
    totalitemsReceipt = Label(totalsFrame, text="Total Items:")
    totalitemsReceipt.grid(row=0,column=1)
    totalitemsqtyReceipt = Label(totalsFrame, text=str(totalqty))
    totalitemsqtyReceipt.grid(row=0,column=2)
    
    totalallReceipt = Label(totalsFrame, text="Sub Total:")
    totalallReceipt.grid(row=0,column=3)
    totalallsubamtReceipt = Label(totalsFrame, text=str(subtotal))
    totalallsubamtReceipt.grid(row=0,column=4)
    
    taxTotalReceipt = Label(totalsFrame, text="HST (13%):")
    taxTotalReceipt.grid(row=1,column=1)
    taxTotaltxtReceipt = Label(totalsFrame, text=str(round(subtotal*0.13,2)))
    taxTotaltxtReceipt.grid(row=1,column=2)
    
    grandtotalallReceipt = Label(totalsFrame, text="Grand Total:")
    grandtotalallReceipt.grid(row=1,column=3)
    grandtotalalltxtReceipt = Label(totalsFrame, text=str(round(subtotal*0.13,2)+subtotal))
    grandtotalalltxtReceipt.grid(row=1,column=4)
    
    labelThankYou = Label(optionsFrame,text='Thank you for your business!',font='Times 16 bold')
    labelThankYou.grid(row = 0, column = 1)
    
    emailBTN = Button(optionsFrame, fg='black', bg='green', text="EMAIL", width=30,height=2)
    emailBTN.grid(row=1,column=0)
    
    printBTN = Button(optionsFrame, fg='black', bg='yellow', text="Print",width=30,height=2)
    printBTN.grid(row=1,column=2)


def clearcart():
    totalqty = 0
    for item in orders:
        totalqty = 0

    totalitemsqtyLABEL.config(text=str(totalqty))

    subtotal = 0
    for item in orders:
        subtotal = 0

        totalallsubamtLABEL.config(text=(subtotal))
        taxTotaltxtLABEL.config(text=subtotal)
        grandtotalalltxtLABEL.config(text=(subtotal)+subtotal)
        #Clear cart items - will do later - monica


wrapper1 = LabelFrame(root, text="Items")
wrapper2 = LabelFrame(root, text="Orders")
wrapper3 = LabelFrame(root, text="Totals")

wrapper1.pack(fill="both", expand="no", padx=20, pady=10)
wrapper2.pack(fill="both", expand="no", padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

asuslaptopBTN = Button(wrapper1, width=15, height=5, text="Asus Laptop\n$800", fg='white', bg='#FF5733', command=addasustotable)
asuslaptopBTN.grid(row=1,column=0)
delllaptopBTN = Button(wrapper1, width=10, height=5, fg='white', bg='#FF5733', text="Dell Laptop\n$1000", command=adddelltotable)
delllaptopBTN.grid(row=1,column=1)
iphone12BTN = Button(wrapper1, width=15, height=5, fg='white', bg='#FF5733', text="iPhone 12 Pro Max\n$550", command=addiphone12totable)
iphone12BTN.grid(row=1,column=2)
samsungGalaxyBTN = Button(wrapper1, width=19, height=5, fg='white', bg='#FF5733', text="Samsung Galaxy Pro\n$900", command=addsamsunggalaxytotable)
samsungGalaxyBTN.grid(row=1,column=3)
iphone12BTN = Button(wrapper1, width=15, height=5, fg='white', bg='#FF5733', text="iPhone 11 Pro\n$400", command=addiphone11totable)
iphone12BTN.grid(row=1,column=4)
ps4BTN = Button(wrapper1, width=15, height=5, fg='white', bg='#FF5733', text="Play Station 4\n$300", command=addps4totable)
ps4BTN.grid(row=1,column=5)
xboxoneBTN = Button(wrapper1, width=13, height=5, fg='white', bg='#FF5733', text="XBOX ONE\n$1000", command=addxboxonetotable)
xboxoneBTN.grid(row=1,column=6)
ps5BTN = Button(wrapper1, width=15, height=5, fg='white', bg='#FF5733', text="Play Station 5\n$1100", command=addps5totable)
ps5BTN.grid(row=2,column=0)
xbox360BTN = Button(wrapper1, width=10, height=5, fg='white', bg='#FF5733', text="XBOX 360\n$200", command=addxbox360totable)
xbox360BTN.grid(row=2,column=1)
lgtvBTN = Button(wrapper1, width=15, height=5, fg='white', bg='#FF5733', text="LG 55inch TV\n$780", command=addlg55totable)
lgtvBTN.grid(row=2,column=2)
samsungtvBTN = Button(wrapper1, width=19, height=5, fg='white', bg='#FF5733', text="Samsung 55inch TV\n$780", command=addsamsung55totable)
samsungtvBTN.grid(row=2,column=3)
sharptvBTN = Button(wrapper1, width=15, height=5, fg='white', bg='#FF5733', text="Sharp 40inch TV\nn$650", command=addsharp55totable)
sharptvBTN.grid(row=2,column=4)
rcatvBTN = Button(wrapper1, width=15, height=5, fg='white', bg='#FF5733', text="RCA 40inch TV\n$650", command=addrca55totable)
rcatvBTN.grid(row=2,column=5)
tcltvBTN = Button(wrapper1, width=13, height=5, fg='white', bg='#FF5733', text="TCL 20inch TV\n$230", command=addtcl55totable)
tcltvBTN.grid(row=2,column=6)
fifa20tvBTN = Button(wrapper1, width=15, height=5, fg='white', bg='#FF5733', text="Fifa 20\n$20", command=addfifa20totable)
fifa20tvBTN.grid(row=3,column=0)
fifa21tvBTN = Button(wrapper1, width=10, height=5, fg='white', bg='#FF5733', text="Fifa 21\n$90", command=addfifa21totable)
fifa21tvBTN.grid(row=3,column=1)
nba2k20tvBTN = Button(wrapper1, width=15, height=5, fg='white', bg='#FF5733', text="NBA 2K 20\n$20", command=addnba2k20totable)
nba2k20tvBTN.grid(row=3,column=2)
nba2k21tvBTN = Button(wrapper1, width=19, height=5, fg='white', bg='#FF5733', text="NBA 2K 21\n$50", command=addnba2k21totable)
nba2k21tvBTN.grid(row=3,column=3)
codbkops2tvBTN = Button(wrapper1, width=15, height=5, fg='white', bg='#FF5733', text="COD Black Ops 2\n$10", command=addcodbopstotable)
codbkops2tvBTN.grid(row=3,column=4)
codmw2tvBTN = Button(wrapper1, width=15, height=5, fg='white', bg='#FF5733', text="COD MW 2\n$24", command=addcodmwtotable)
codmw2tvBTN.grid(row=3,column=5)
codcoldwartvBTN = Button(wrapper1, width=13, height=5, fg='white', bg='#FF5733', text="COD Cold War\n$100", command=addcodcoldwartotable)
codcoldwartvBTN.grid(row=3,column=6)

totalitemsLABEL = Label(wrapper3, text="Total Items:")
totalitemsLABEL.grid(row=1,column=1)
totalitemsqtyLABEL = Label(wrapper3, text="0")
totalitemsqtyLABEL.grid(row=1,column=2)

totalallLABEL = Label(wrapper3, text="Sub Total:")
totalallLABEL.grid(row=2,column=1)
totalallsubamtLABEL = Label(wrapper3, text="0")
totalallsubamtLABEL.grid(row=2,column=2)

taxTotalLABEL = Label(wrapper3, text="HST (13%):")
taxTotalLABEL.grid(row=3,column=1)
taxTotaltxtLABEL = Label(wrapper3, text="0")
taxTotaltxtLABEL.grid(row=3,column=2)

grandtotalallLABEL = Label(wrapper3, text="Grand Total:")
grandtotalallLABEL.grid(row=4,column=1)
grandtotalalltxtLABEL = Label(wrapper3, text="0")
grandtotalalltxtLABEL.grid(row=4,column=2)

generateReceiptBTN = Button(wrapper3, fg='white', bg='#17B14D', text="Generate Receipt", command=calculateQTY)
generateReceiptBTN.grid(row=4,column=5)

clearcartBTN = Button(wrapper3, fg='white', bg='#17B14D', text="Clear Cart", command=clearcart)
clearcartBTN.grid(row=4, column=6, padx=20,pady=10)

trv = Treeview(wrapper2, columns=(1, 2, 3, 4), show="headings", height="10")
trv.pack()
trv.heading(1, text="Product")
trv.heading(2, text="Quantity")
trv.heading(3, text="Price")
trv.heading(4, text="Subtotal per Product")

root.title("POS System")
root.geometry("850x700")
root.mainloop()
