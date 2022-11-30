from tkinter import *

root = Tk()

def say_hello():
    greating = Label(root, text = "Hello", fg = '#010059')
    greating.pack()

new_button = Button(root, text = 'Say hello', fg = '#00ff1e', command=say_hello)
new_button.pack()

root.mainloop()