import tkinter as tk
from tkinter import ttk
from tkinter import *


root = Tk()

wrapper1 = LabelFrame(root, text="Items")
wrapper2 = LabelFrame(root, text="Orders")
wrapper3 = LabelFrame(root, text="Totals")

wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)


root.title("POS System")
root.geometry("800x700")
root.mainloop()