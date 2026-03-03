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
lst = [(1, 'Amy', 'Avocado', 19),
       (2, 'Brian', 'Brownies', 20),
       (3,"Charlie","Carrots",23),
       (4,"Eduard","Eggplants",22),
       (5,"Francois","Figs",12)]

#Find the total number of rows and colums
total_rows = len(lst)
total_columns = len(lst[0])





#Create the root window
root = Tk()
t = Table(root)
root.attributes('-type', 'dialog')
root.mainloop()