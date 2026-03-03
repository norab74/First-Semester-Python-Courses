from tkinter import *



#Lets make a window
top = Tk()
top.title("This is my first GUI in tKinter")
top.geometry('400x300') ##This line does not work on tiling WMs unless you've floating windows enabled or force it, like below.
top.attributes('-type', 'dialog') #This line forces the window to float so even on tiling WMs like i3 it still floats
top.configure(bg='coral2')

#Lets define a behavior for a button:
def clicked():
    print("Yo dude, I got clicked")
def anotherOne():
    third = Toplevel()
    third.geometry('600x200')
    third.attributes('-type', 'dialog')
    third.configure(bg='brown')
    Label(third, text="Oh this is an interesting color for a window").pack()
second = Toplevel()
def DareClicked():
    second.attributes('-type', 'dialog')
    second.configure(bg='lightGreen')
    Label(second, text="I've been spawned by a button").pack()
    thirdButton = Button(second, text="Oh Woah, another button", command=MakeMoreButtons, bg='yellow').pack()
    
def MakeMoreButtons():
    for i in range(10):
        Button(second, text=i).pack()

#Lets make a button
testButton = Button(text="Click Here", command=clicked, bg='violet').pack(side=LEFT, expand=True)
secondButton = Button(text="Dare you to click me", command=DareClicked, bg='cyan').pack(side=RIGHT, expand=True)
#testButton.pack()
#testButton['text'] = "Click Here!" #Put some text on it
#testButton['command'] = clicked

#lets add some text
topLabel = Label(top,text="Hello tKinter!", fg='green').pack()


mainloop() #much like pygame, everything must be handled in a loop. If we specify logic within mainloop by defining it manually, we may make our UI more dynamic.
