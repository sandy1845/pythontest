from tkinter import *

root = calc ()

input = Entry(root, width(50))
input.grid = (row=0, column=0, columnspan=3, padx=15, pady=15) 

def click():
    return

def add():
    return

def sub():
    return

def multi():
    return

def div():
    return

def clear():
    return

Button_1 = Button(root, text="1", padx=50, pady=25, command=click)
Button_2 = Button(root, text="2", padx=50, pady=25, command=click)
Button_3 = Button(root, text="3", padx=50, pady=25, command=click)
Button_4 = Button(root, text="4", padx=50, pady=25, command=click)
Button_5 = Button(root, text="5", padx=50, pady=25, command=click)
Button_6 = Button(root, text="6", padx=50, pady=25, command=click)
Button_7 = Button(root, text="7", padx=50, pady=25, command=click) 
Button_8 = Button(root, text="8", padx=50, pady=25, command=click)
Button_9 = Button(root, text="9", padx=50, pady=25, command=click)
Button_0 = Button(root, text="0", padx=50, pady=25, command=click)

Button_7.grid=(row(1), column(0))
Button_8.grid=(row(1), column(1))
Button_9.grid=(row(1), column(2))

Button_6.grid=(row(2), column(0))
Button_5.grid=(row(2), column(1))
Button_4.grid=(row(2), column(2))

Button_3.grid=(row(1), column(0))
Button_2.grid=(row(1), column(1))
Button_1.grid=(row(1), colu
root.mainloop