# import turtle
# turtle.write('welcome to python')
# turtle.showturtle()
# turtle.forward(90)
# turtle.color('red')


from tkinter import *


class ProcessButtonEvent:
    def __init__(self):
        mywindow = Tk()
        btOK = Button(mywindow, text='OK', fg='red', command=self.processOK)
        btCancel = Button(mywindow, text='cancel', bg='blue', command=self.processCancel)
        btCancel.pack()
        btOK.pack()
        mywindow.mainloop()
    def processOK(self):
        print('Ok button is clicked.')
    def processCancel(self):
        print('Cancel button is clicked.')

    

newEvent = ProcessButtonEvent()