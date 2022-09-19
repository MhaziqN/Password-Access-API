from tkinter import *
import random

root = Tk()


def Phrase_Gen():
    name = str(Entry1.get()) # get the Entry1 input
    phrase = ['Hello', 'Hi', 'Holla']
    decline = ['Sorry, You are not allowed !!', 'Authorized Access Only']

    # pasword filter
    if name.lower() == 'haziq':
        return phrase[random.randint(0, 2)], name
    else:
        return decline[random.randint(0, 1)]


# display configuration
def Display():
    greeting = Phrase_Gen()

    greeting_display = Text(master=root, width=30, height=10)
    greeting_display.grid(column=1, row=4)
    #inser greeting dalam box display
    greeting_display.insert(END, greeting)


###LABEL####
root.title('Password Access')
root.geometry('400x400')

label1 = Label(text="Password Access API")
label1.grid(column=1, row=0, pady=10)
label1.config(font=('Time New Roman', 12))

label2 = Label(text="Name")
label2.grid(column=0, row=1, pady=10)

Entry1 = Entry()
Entry1.grid(column=1, row=1, pady=5)

OkButton1 = Button(text="Submit", command=Display)
OkButton1.grid(column=2, row=1, pady=5)

root.mainloop()


###NOTE###

#grid for row tak boleh direct strait kebawah
# susun jadi lebih menarik if column can!!