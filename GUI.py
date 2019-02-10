from tkinter import *
from tkinter import ttk

root = Tk()
root.title("TyperPro")
root.geometry("500x500")
root.iconbitmap(bitmap="icon.ico")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.pack()

words = StringVar()

Label = Label(root, textvariable= )

E1 = Entry(root, fg='black',font='Ariel', bd= 5, width = 44, textvariable= words)
E1.pack(pady = 200)
root.mainloop()