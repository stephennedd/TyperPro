import random
import time
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()

GREY = "#81827D"

# Open file article.txt and seperate the sentences using ('.') as split.
# Then write a randomly chosen sentence into sentence.txt.
for i in range(1000):
    with open("files/article.txt", 'r') as f:
        sentences = f.read().split(".")
    with open("files/sentence.txt", 'w') as f:
        f.write(random.choice(sentences) + ".")
# Read the sentence that was written into sentences.txt and print it.
with open("files/sentence.txt", 'r') as q:
    sentence = str(q.read().strip())

# Create a time stamp of the time it printed the sentence.
start = time.time()

root.title("TyperPro")
root.geometry("1000x500")
root.config(bg= GREY)
root.iconbitmap(bitmap="images/icon.ico")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.pack()

img = Image.open("images/typerlogo.png")
img = img.resize((350,225), Image.ANTIALIAS)
photoImg = ImageTk.PhotoImage(img)
Logo = Label(root, image= photoImg, borderwidth= 0, )
Logo.pack()

SentenceToType = Label(root, text= sentence, fg='blue', bg=GREY, width= 900)
SentenceToType.pack(pady= 10)

Explain = Label(root, text= "Type the above sentence below.",bg= GREY, fg = 'black', font='Ariel')
Explain.pack(pady =25)

word = StringVar()
Entry1 = Entry(root, fg='black',bd= 2, width= 60, textvariable= word, relief=GROOVE, takefocus= TRUE)
Entry1.pack()


def SentenceChecker():
    Right = Label(root, text= "Great!", fg= 'green', bg = GREY)
    Wrong = Label(root, text= "You made a mistake.", fg= 'red', bg = GREY)
    content = word.get()
    if content == sentence:
        now = time.time()
        end = round((now - start), 2)
        Time = Label(root, text= str(end) + " seconds", bg= GREY)
        Right.pack()
        Time.pack()
    else:
        now = time.time()
        end = round((now - start), 2)
        Time2 = Label(root, text=str(end) + " seconds", bg=GREY)
        Wrong.pack()
        Time2.pack()


EnterButton = Button(root, text="Finished", width=10, relief=RAISED, command=SentenceChecker)
EnterButton.pack(pady= 10)

# root.bind('<Return>', SentenceChecker())
root.mainloop()