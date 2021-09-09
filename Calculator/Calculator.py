from tkinter import *
from PIL import ImageTk

# Backend

def callback(entry):
    if entry.isdigit():
        return True
    elif entry == '':
        return True
    else:
        return False


def click(num):
    global oper
    oper = oper + str(num)
    text.set(oper)


def clear():
    global oper
    oper = ''
    text.set("")


def equals():
    try:
        global oper
        ans = str(eval(oper))
        oper = ""
        text.set(ans)
    except ZeroDivisionError:
        text.set("ZERO DIVISION ERROR")
    except SyntaxError:
        text.set("INVALID SYNTAX")


# FrontEnd

window = Tk()

window.wm_title("Calculator")
icon = ImageTk.PhotoImage(file='../Calc_icon.png')
window.iconphoto(False, icon)
window.maxsize(300, 340)

oper = ''
text = StringVar()
e1 = Entry(window, width=22, textvariable=text, justify='right', font=('arial', 15, 'bold'),
           bd=30, bg='grey')
e1.grid(row=0, column=0, rowspan=1, columnspan=4, ipady=10)

# Row 1 ---------------------------------
b1 = Button(window, text="9", command=lambda: click(9), padx=25, pady=10,
            font=('arial', 15, 'bold'))
b1.grid(row=2, column=0)

b2 = Button(window, text="8", command=lambda: click(8), padx=25, pady=10,
            font=('arial', 15, 'bold'))
b2.grid(row=2, column=1)

b3 = Button(window, text="7", command=lambda: click(7), padx=25, pady=10,
            font=('arial', 15, 'bold'))
b3.grid(row=2, column=2)

# Row 2 ---------------------------------
b4 = Button(window, text="6", command=lambda: click(6), padx=25, pady=10,
            font=('arial', 15, 'bold'))
b4.grid(row=3, column=0)

b5 = Button(window, text="5", command=lambda: click(5), padx=25, pady=10,
            font=('arial', 15, 'bold'))
b5.grid(row=3, column=1)

b6 = Button(window, text="4", command=lambda: click(4), padx=25, pady=10,
            font=('arial', 15, 'bold'))
b6.grid(row=3, column=2)

# Row 3 ---------------------------------
b7 = Button(window, text="3", command=lambda: click(3), padx=25, pady=10,
            font=('arial', 15, 'bold'))
b7.grid(row=4, column=0)

b8 = Button(window, text="2", command=lambda: click(2), padx=25, pady=10,
            font=('arial', 15, 'bold'))
b8.grid(row=4, column=1)

b9 = Button(window, text="1", command=lambda: click(1), padx=25, pady=10,
            font=('arial', 15, 'bold'))
b9.grid(row=4, column=2)

# Row 1 ---------------------------------
b10 = Button(window, text="C", command=clear, padx=25, pady=10,
             font=('arial', 15, 'bold'))
b10.grid(row=5, column=0)

b11 = Button(window, text="0", command=lambda: click(0), padx=25, pady=10,
             font=('arial', 15, 'bold'))
b11.grid(row=5, column=1)

b12 = Button(window, text="=", command=equals, padx=25, pady=10,
             font=('arial', 15, 'bold'))
b12.grid(row=5, column=2)

# Column -----------------------------------
b13 = Button(window, text="+", command=lambda: click('+'), padx=25, pady=10,
             font=('arial', 15, 'bold'))
b13.grid(row=2, column=3)

b14 = Button(window, text="-", command=lambda: click('-'), padx=27, pady=10,
             font=('arial', 15, 'bold'))
b14.grid(row=3, column=3)

b14 = Button(window, text="*", command=lambda: click('*'), padx=27, pady=10,
             font=('arial', 15, 'bold'))
b14.grid(row=4, column=3)

b15 = Button(window, text="/", command=lambda: click('/'), padx=27, pady=10,
             font=('arial', 15, 'bold'))
b15.grid(row=5, column=3)

reg = window.register(callback)
e1.config(validate='key', validatecommand=(reg, '%P'))

window.mainloop()
