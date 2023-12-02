from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title("Python Guides")
ws.geometry("300x250")


def about():
    messagebox.showinfo('PythonGuides', 'Python Guides aims at providing best practical tutorials')


menubar = Menu(ws, foreground='black', activebackground='white', activeforeground='black')
file = Menu(menubar, tearoff=1, foreground='black')
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save as")
file.add_separator()
file.add_command(label="Exit", command=ws.quit)
menubar.add_cascade(label="File", menu=file)

edit = Menu(menubar, tearoff=0)



ws.config(menu=menubar)
ws.mainloop()
