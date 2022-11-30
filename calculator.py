from tkinter import *
from numpy import divide, multiply

from setuptools import Command

root = Tk()
root.geometry('300x350')

screen = Entry(root, borderwidth = 3, width= 30)
screen.grid(columnspan = 6, column = 0, row = 0)

def clear():
    screen.delete(0, 'end')

def button_click(messege):
    original_value = screen.get()
    screen.delete('0', 'end')
    screen.insert(0, original_value + str(messege))
    

clear  = Button(text = 'clear',padx = 15, pady = 15, command = clear )
clear.grid(column = 2, row = 1)

plus  = Button(text = '+', padx = 15, pady = 15, command = lambda:button_click('+'))
plus.grid(column = 5, row = 3)

minus = Button(text = '-', padx = 15, pady = 15, command = lambda:button_click('-'))
minus.grid(column = 4, row = 1)

divide  = Button(text = ':',padx = 15, pady = 15, command = lambda:button_click(':'))
divide.grid(column = 5, row = 1)

multiply  = Button(text = '*',padx = 15, pady = 15, command = lambda:button_click('*'))
multiply.grid(column = 5, row = 2)

minus = Button(text = '-',padx = 15, pady = 15, command = lambda:button_click('-'))
minus.grid(column = 5, row = 4)

brackets = Button(text = '( )',padx = 15, pady = 15, command = lambda:button_click('( )'))
brackets.grid(column = 3, row = 1)

equal = Button(text = '=',padx = 15, pady = 15, command = lambda:button_click('='))
equal.grid(column = 0, row = 5, columnspan = 2)

persent = Button(text = '%', padx = 15, pady = 15, command = lambda:button_click('%'))
persent.grid(column = 2, row = 5)

nine = Button(text = '9',padx = 15, pady = 15, command = lambda:button_click(9))
nine.grid(column = 4, row = 2)

eight  = Button(text = '8',padx = 15, pady = 15, command = lambda:button_click(8))
eight.grid(column = 2, row = 2)

seven  = Button(text = '7',padx = 15, pady = 15, command = lambda:button_click(7))
seven.grid(column = 3, row = 2)

six  = Button(text = '6',padx = 15, pady = 15, command = lambda:button_click(6))
six.grid(column = 4, row = 3)

five = Button(text = '5',padx = 15, pady = 15, command = lambda:button_click('5'))
five.grid(column = 3, row = 3)

four  = Button(text = '4',padx = 15, pady = 15, command = lambda:button_click(4))
four.grid(column = 2, row = 3)

three  = Button(text = '3',padx = 15, pady = 15, command = lambda:button_click(3))
three.grid(column = 4, row = 4)

two  = Button(text = '2',padx = 15, pady = 15, command = lambda:button_click('2'))
two.grid(column = 3, row = 4)

one  = Button(text = '1',padx = 15, pady = 15, command = lambda:button_click('1'))
one.grid(column = 2, row = 4)

zero = Button(text = '0',padx = 15, pady = 15, command = lambda:button_click('0'))
zero.grid(column = 1, row = 5)

root.title('caluculator')

root.mainloop()