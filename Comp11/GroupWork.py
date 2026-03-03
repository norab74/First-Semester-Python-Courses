#Find or create a data source csv file
import csv

lst = []

def loadFile(filename=''):
    with open(filename, 'r') as importedFile:
    #save it as a dictionary...kinda
        datafile = csv.DictReader(importedFile)
        n = 0
        for row in datafile: #move data into our lists for easier addressing
            lst.append(row[n])
            n+=n

#display the data as a table

#Creating basic tables using Tkinter.
from tkinter import *
#Tkinter does not provide a table widget, we must create our own.
class Table:
    def __init__(self, root):
        
        #Actually make the table:
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, bg="darkolivegreen4", fg='cornsilk2', font=('Arial',16,'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
#Create the data which will populate our table
loadFile("Python Fundamentals/Comp11/P11/ExpandedPoints.csv")

#Find the total number of rows and colums
total_rows = len(lst)
total_columns = len(lst[0])




#Create the root window
root = Tk()
t = Table(root)
root.attributes('-type', 'dialog')
root.mainloop()
#provide the ability to add and remove items


