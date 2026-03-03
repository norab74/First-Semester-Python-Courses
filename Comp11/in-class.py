##We need to source a data file, I'm using a CSV because they're super easy to work with.

##After loading in the CSV, we need to parse it, turn it into usable data, allow users to modify it, then write our file back.
    #The easiest way to do that without knowing what the data will be is to iterate accross our data
    
    #First:
        #Iterate accross the first line of our CSV to determine how many fields wide our table needs to be
#COMPLETED
    #Second:
        #Iterate accross each line to determine how many lines our table will contain
#COMPLETED        
    #Third:
        #Fill a list with the data from our CSV
#COMPLETED        
    #Fourth:
        #Using the same method used in "simpleTable.py"
        # (the demo from g4g), populate a table with the 
        #data from the list made in the third step
#COMPLETED        
    #Fifth:
        #Update the data in our list, referencing the
        #table as modified by the user. Reference
        #the docs, what is Entry()?
        # How can I use it for my needs?
#TODO        
    #Sixth:
        #Write the data back to our file, there's a few ways we can do this
        #The simplest way is to reopen our file in write mode
        #write blank data until End of File
        #Write our list to the file
            #leverage formatting tools like join() and sep()
#TODO            
            
## After defining the above functions, we build our UI
    #To keep things simple, just make a couple buttons,
    #While a menu bar isn't harder, it's significantly
    #more tedium for not much extra payoff
    #given the assignment, in a production environment
    #this should be done in a 'pretty' way
    
#UI is built, just needs to be hooked into the functions,
#Table() subclasses tk.Text() so it can do anything that tk.Text() can do, check out the docs on that for more


#What's broken:
    #Currently saving the file just saves a blank csv, evidenced by trying to load the file having only a single empty cell.
    #Why this happens:
        #I think what's happening is that because I haven't yet worked out the logic on
        # pulling data from our cells and putting that into a list, the save function 
        # just simply doesn't work the way I need it to. It's too abstract and it needs
        # a variable it can latch onto.
    #possible solutions:
        #as mentioned above in step 5, we need a list of our data similar to how we got data from our csv.
        #Pretty sure this is ideal
    
    
    
    
    
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText
from time import strftime
import os
import csv


#globals
global filename
filename = ''

#Add some events
lst =[]
   

def load():
    filename = filedialog.askopenfilename()
    with open(filename) as file:
        importedData = csv.reader(file)
        for row in importedData:
            lst.append(row)

        #contents.delete('1.0', END)
        #contents.insert(INSERT, file.read())

                
def save(contents):
    global filename

    filename=filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    
    #Get data and split it into rows
    text = contents.get("1.0", "end-1c")
    rows = [line.split("\t") for line in text.split("\n")]
    
    with open(filename, 'w', newline="", encoding='utf-8') as file:
        csvWriter = csv.writer(file)
        csvWriter.writerows(rows)
            
            
            
            
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




load()



class Table(tk.Text): #subclass tk.Text so we can access anythin that tk.Text can do, like copy and paste
    
    def __init__(self, root, master=None, **kwargs):
        super().__init__(master, **kwargs) #initalize superclass
        #Actually make the table:
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, font=('Arial',16,'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
    
    
total_rows = len(lst)
total_columns = len(lst[0])

#Start with an empty window
rootWindow = Tk()
rootWindow.title("CSV Editor")

#add a "scrolled text" box
contents = Table(rootWindow)








#contents.pack(side=BOTTOM, expand=True, fill=BOTH)


#lets use a menu instead of buttons, they're cleaner
menubar = Menu(rootWindow)
#File
fileDropdown = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = fileDropdown)
fileDropdown.add_command(label = "New File", command = newFile) #TODO
fileDropdown.add_command(label = "Open...", command = load)
fileDropdown.add_command(label = "Save", command = lambda:save(contents)) #TODO
fileDropdown.add_separator()
fileDropdown.add_command(label = "Exit", command = rootWindow.destroy)
#Edit
editDropdown = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Edit", menu = editDropdown)
editDropdown.add_command(label = 'Cut', command = cut) #TODO
editDropdown.add_command(label = 'Copy', command = copy)# TODO
editDropdown.add_command(label = 'Paste', command = paste) #TODO
editDropdown.add_command(label = 'Select All', command = selectAll) #TODO
editDropdown.add_separator()
editDropdown.add_command(label = 'Find...', command = None) #TODO
editDropdown.add_command(label = 'Find next', command = None) #TODO

#actually run the program
rootWindow.config(menu=menubar)
mainloop()