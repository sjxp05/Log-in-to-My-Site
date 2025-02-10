from tkinter import *
from tkinter import ttk

tk = Tk()
tk.geometry("200x100")

lst = []
for i in range(1, 13):
    lst.append(str(i))

lst2 = []
for i in range(1, 32):
    lst2.append(str(i))

monValue = StringVar()
monBox = ttk.Combobox(
    font=("맑은 고딕", 12), textvariable=monValue, values=lst, width=3
)
monBox.place(x=30, y=0)

dateValue = StringVar()
dateBox = ttk.Combobox(
    font=("맑은 고딕", 12), textvariable=dateValue, values=lst2, width=3
)
dateBox.place(x=120, y=0)

tk.mainloop()
