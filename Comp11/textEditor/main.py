from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText
from time import strftime
import os


#globals
global filename
filename = ''

#Add some events
        

def load():
    filename = filedialog.askopenfilename()
    with open(filename) as file:
        contents.delete('1.0', END)
        contents.insert(INSERT, file.read())

def save():
    global filename
    if os.path.exists(filename):
        with open(filename, 'w') as file:
            file.write(contents.get('1.0', END))
    else:
        filename=filedialog.asksaveasfilename()
        with open(filename, 'w') as file:
            file.write(contents.get('1.0', END))
def newFile():
    contents.delete('1.0', END)
    filename = ''

def cut():
    contents.event_generate("<<Cut>>")
def copy():
    contents.event_generate("<<Copy>>")
def paste():
    contents.event_generate("<<Paste>>")
def selectAll():
    contents.tag_add("sel", "1.0", END)
#def find():


#def findNext():
    

#Start with an empty window
rootWindow = Tk()
rootWindow.title("Simple Editor")

#add a "scrolled text" box
contents = ScrolledText()
contents.pack(side=BOTTOM, expand=True, fill=BOTH)


#lets use a menu instead of buttons, they're cleaner
menubar = Menu(rootWindow)
#File
fileDropdown = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = fileDropdown)
fileDropdown.add_command(label = "New File", command = newFile) #TODO
fileDropdown.add_command(label = "Open...", command = load)
fileDropdown.add_command(label = "Save", command = save) #TODO
fileDropdown.add_separator()
fileDropdown.add_command(label = "Exit", command = rootWindow.destroy)
#Edit
editDropdown = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Edit", menu = editDropdown)
editDropdown.add_command(label = 'Cut', command = cut)
editDropdown.add_command(label = 'Copy', command = copy)
editDropdown.add_command(label = 'Paste', command = paste)
editDropdown.add_command(label = 'Select All', command = selectAll)
editDropdown.add_separator()
editDropdown.add_command(label = 'Find...', command = None)
editDropdown.add_command(label = 'Find next', command = None)

#actually run the program
rootWindow.config(menu=menubar)
mainloop()