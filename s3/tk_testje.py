from tkinter import *

def click():
    """click me action"""
    print('you clicked the button.')

buttons = []
window = Tk()
button1 = Button(window, 
                text="click me", 
                command=click)
button1.pack()
buttons.append(button1)

button2 = Button(window, 
                text="click me also", 
                command=click)
button2.pack()
buttons.append(button2)

button1.pack()
window.mainloop()
