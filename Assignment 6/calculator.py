from tkinter import *

window = Tk()

window.geometry("500x500")

def click(num):
    result = entry_box.get()
    entry_box.delete(0, END)
    entry_box.insert(0, str(result) + str(num))


entry_box = Entry(window, width=81, borderwidth=5)
entry_box.place(x=0, y=0)

b = Button(window,text="1",width=10, command = lambda:click(1))
b.place(x=0,y=30)

b = Button(window,text="2",width=10, command = lambda:click(2))
b.place(x=80,y=30)

b = Button(window,text="3",width=10, command = lambda:click(3))
b.place(x=160,y=30)

b = Button(window,text="4",width=10, command = lambda:click(4))
b.place(x=0,y=60)

b = Button(window,text="5",width=10, command = lambda:click(5))
b.place(x=80,y=60)

b = Button(window,text="6",width=10, command = lambda:click(6))
b.place(x=160,y=60)

b = Button(window,text="7",width=10, command = lambda:click(7))
b.place(x=0,y=90)

b = Button(window,text="8",width=10, command = lambda:click(8))
b.place(x=80,y=90)

b = Button(window,text="9",width=10, command = lambda:click(9))
b.place(x=160,y=90)

b = Button(window,text="0",width=10, command = lambda:click(0))
b.place(x=80,y=120)

def add():
    n1 = entry_box.get()
    global i,math
    math="addition"
    i= int(n1)
    entry_box.delete(0, END)

b = Button(window,text="+",width=10, command =add)
b.place(x=240,y=30)

def sub():
    n1 = entry_box.get()
    global i,math
    math = "subtraction"
    i= int(n1)
    entry_box.delete(0, END)

b = Button(window,text="-",width=10, command = sub)
b.place(x=240,y=60)

def mul():
    n1 = entry_box.get()
    global i,math
    math = "multiplication"
    i= int(n1)
    entry_box.delete(0, END)

b = Button(window,text="*",width=10, command = mul)
b.place(x=240,y=90)

def div():
    n1 = entry_box.get()
    global i,math
    math = "division"
    i= int(n1)
    entry_box.delete(0, END)

b = Button(window,text="/",width=10, command = div)
b.place(x=240,y=120)

def equal():
    num2 = entry_box.get()
    n2=int(num2)
    entry_box.delete(0, END)
    if math == "addition":
        entry_box.insert(0,i+n2)
    elif math == "subtraction":
        entry_box.insert(0,i-n2)
    elif math == "multiplication":
        entry_box.insert(0,i*n2)
    elif math == "division":
        entry_box.insert(0,i/n2)

b = Button(window,text="=",width=10, command = equal)
b.place(x=160,y=120)

b = Button(window,text="Clear",width=10, command = lambda:entry_box.delete(0, END))
b.place(x=0,y=120)

mainloop()