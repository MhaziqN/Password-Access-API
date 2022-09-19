from tkinter import *
import random

root = Tk()

root.title("Testing")
root.geometry("400x400")


##function###
def phrase_Generator():
    name = str(entry1.get())
    rand = ['Hello', 'Hi', 'Holla']

    # Random Greeting
    return rand[random.randint(0, 2)], name


# display method config
def Display():
    greeting = phrase_Generator()

    # Text insert config
    greeting_display = Text(master=root, height=10, width=30)
    greeting_display.grid(column=1, row=4)

    # Greeting declare wih output
    greeting_display.insert(END, greeting)


##LABEL##
label1 = Label(text="Hello World")
label1.grid(column=1, row=0, pady=10)
label1.config(font=('Time New Roman', 15))

label2 = Label(text='What is your name ? ')
label2.grid(column=0, row=1, pady=5)

entry1 = Entry()
entry1.grid(column=0, row=2, pady=5)

OkButton1 = Button(text="OK", bg='grey', command=Display)
OkButton1.grid(column=0, row=3, pady=5)

root.mainloop()
