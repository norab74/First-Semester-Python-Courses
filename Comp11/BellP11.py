#BellP11
#Programmer: Nora Bell
#Email: nbell8@cnm.edu
#Purpose: To demonstrate profiency in tkinter for the generation of simple user interfaces
#Imports
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from Geopoint import GeoPoint
import csv


#create tk windows
welcomeWindow = tk.Tk()
welcomeWindow.attributes('-type', 'dialog')
filePickerWindow = Toplevel()
filePickerWindow.attributes('-type', 'dialog')
mainWindow = Toplevel()
mainWindow.attributes('-type', 'dialog')
resultsWindow = Toplevel()
resultsWindow.attributes('-type', 'dialog')
#Title our windows
welcomeWindow.title("GeoPoint Comparer - BellP11")
filePickerWindow.title("Select a file")
mainWindow.title("GeoPoint Comparer - BellP11")
resultsWindow.title("Comparison Complete!")
#Set Window Geometries
welcomeWindow.geometry("400x200")
filePickerWindow.geometry("500x500")
mainWindow.geometry("800x600")
resultsWindow.geometry("300x200")
#Add text to our windows
welcomeWindowLabel = Label(welcomeWindow,
                    text = "Please load the file containing your location data",
                    fg = "darkolivegreen3",
                    bg = 'cornsilk4').grid(row=0, column=0, padx=5, pady=5)
mainWindowLatitudeLabel = Label(mainWindow,
                    text="Latitude:",
                    fg = "darkolivegreen3",
                    bg = 'cornsilk4')
mainWindowLongitudeLabel = Label(mainWindow,
                    text="Longitude:",
                    fg = "darkolivegreen3",
                    bg = 'cornsilk4')
mainWindowCalculateDistanceLabel = Label(mainWindow,
                    text="Calculate",
                    fg = "darkolivegreen3",
                    bg = 'cornsilk4')
resultsWindowLabel = Label(resultsWindow,
                    text="", #TODO
                    fg = "darkolivegreen3",
                    bg = 'cornsilk4')
#Create buttons for our windows
welcomeWindowCancelButton = Button(welcomeWindow,
                                   text = "Exit",
                                   command = exit).grid(row=2, column=0, padx=1, pady=10)

mainWindowCalculateDistanceButton = Button(mainWindow,
                                           text = "Calculate",
                                           fg = "darkolivegreen3",
                                           bg = 'cornsilk4')
resultsWindowsCloseDialogButton = Button(resultsWindow,
                                         text = "Close",
                                         fg = "darkolivegreen3",
                                         bg = 'cornsilk4',
                                         command=resultsWindow.destroy)
#Create a "spreadsheet-like" display for the data pulled in from CSV
spreadsheet = ttk.Treeview(mainWindow,
                    columns =("City",
                              "Latitude",
                              "Longitude"),
                    show = "headings")
#Define the headings for each column of our display
spreadsheet.heading("City", text="City")
spreadsheet.heading("Latitude", text="Latitude")
spreadsheet.heading("Longitude", text="Longitude")
#Fill our spreadsheet with data pulled from our csv
#TODO

#Create Text Entry widgets for each window that will need them
entryText=tk.StringVar(value="Enter path or click 'Select'")
welcomeWindowFileSelectorTextEntry = Entry(welcomeWindow, textvariable=entryText).grid(row=1, column=0, padx=10)
mainWindowLatitudeTextEntry = Entry(mainWindow)
mainWindowLongitudeTextEntry = Entry(mainWindow)
#Create a file picker
def filePicker():
    filename = filedialog.askopenfilename(initialdir= ".",
                                          title = "Select a File",
                                          filetypes = (("CSV Files",
                                                        "*.csv"),
                                                       ("Enable Unsupported Files (may cause unexpected behavior)",
                                                        "*.*")))
    if filename:
        entryText.set(filename) #Update text box
        
welcomeWindowExploreFilesButton = Button(welcomeWindow,  #we're doing this here because reasons... good ones... don't ask.
                            text= "Select",
                            command = filePicker).grid(row=1, column=1)
welcomeWindowLoadButton = Button(welcomeWindow,
                                 text="Load",
                                 fg = "darkolivegreen3",
                                 bg = "cornsilk4",
                                 #command = 
                                 ).grid(row=2, column=1, padx=10, pady=10)




mainloop()