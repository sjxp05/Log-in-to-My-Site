from tkinter import *

root = Tk()

id1 = ""
pw1 = ""


def idcheck():
    global id1, pw1

    id1 = thisId.get()
    pw1 = thisPw.get()  # 잘 됨!!

    # 입력한거 삭제 기능: 잘됨
    thisId.delete(0, END)
    thisPw.delete(0, END)

    print(id1)
    print(pw1)


thisId = Entry(
    font=("맑은 고딕", 15),
    fg="black",
)
thisId.pack()

thisPw = Entry(
    font=("맑은 고딕", 15),
    fg="black",
    show="*",
)
thisPw.pack()

bt1 = Button(root, text="Log in", command=idcheck)
bt1.pack()

root.mainloop()
