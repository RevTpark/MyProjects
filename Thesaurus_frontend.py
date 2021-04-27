import json
import difflib
from tkinter import *
from tkinter import messagebox
# from tkinter.ttk import *

data = json.load(open('data.json'))


# Validating the entry as strings and not nums
def callback(entry):
    if entry.isalpha():
        return True
    elif entry == '':
        return True
    else:
        return False


def output_set(li):
    list1.delete('1.0', END)
    for c, item in enumerate(li):
        list1.insert(INSERT, str(c+1) + '] ' + item + '\n')


def translate(w):
    w = w.lower()
    if w in data:
        return output_set(data[w])

    elif w.title() in data:
        return output_set(data[w.title()])

    elif w.upper() in data:
        return output_set(data[w.upper()])

    elif len(difflib.get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        temp = difflib.get_close_matches(w, data.keys(), cutoff=0.8)[0]
        msg_box = messagebox.askquestion('Similar word found', f'Did you mean {temp} instead?')
        if msg_box == 'yes':
            return output_set(data[temp])
        else:
            list1.delete('1.0', END)
            list1.insert(INSERT, "The word mentioned does not exists in database...")
    else:
        list1.delete("1.0", END)
        list1.insert(INSERT, "Oops.. The word entered does not exists. Please double check it.")


def exit_():
    msg_box = messagebox.askokcancel("Exit Thesaurus", "Are you sure you want to EXIT?")
    if msg_box:
        window.destroy()


window = Tk()
window.title('Thesaurus')
window.config(bg="light grey")

l1 = Label(text="Your personal Thesaurus", foreground='blue', font=('timesroman', '15', 'bold'),
           bg='light grey')
l1.grid(row=0, column=0, columnspan=5)

word = StringVar()
e1 = Entry(window, textvariable=word, bg='powder blue', font=('timesroman', '11'), bd=3, width=30)
e1.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

b1 = Button(window, text="Search", width=9, fg='dark blue',
            command=lambda: translate(word.get()))
b1.grid(row=1, column=4)

list1 = Text(window, width=55, height=20, font=('opensans', '10', 'bold'))
list1.grid(row=2, column=0, rowspan=5, columnspan=5)

b2 = Button(window, text='Exit', fg='red', command=exit_, width=15)
b2.grid(row=7, column=4, columnspan=5)

reg = window.register(callback)
e1.config(validate="key", validatecommand=(reg, "%P"))

window.mainloop()
