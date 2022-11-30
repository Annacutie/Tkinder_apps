from cProfile import label
from tkinter import *

#from hello import say_hello

root = Tk()

#text = Entry(root)
'''
def say_hello():
    greating = Label(root, text = "Hello", fg = '#010059')
    greating.pack()
'''
def greating():
    #text.get()
    label = Label(root, text = f'Hello {text.get()}')
    label.grid(row=2 ,column=1)

text = Entry(root)
say_hello = Button(root, text = 'Hello', command = greating)
text.grid(row=0 ,column=0, columnspan=2)
say_hello.grid(row=1, column=0, columnspan=2)

root.title('Welcome')
root.mainloop()