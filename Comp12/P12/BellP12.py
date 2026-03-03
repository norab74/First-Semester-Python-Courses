# BellP12
# Programmer: Nora Bell
# Email: nbell8@cnm.edu
# Purpose: To demonstrate proficiency SQLite3

import tkinter as tk
#from tkinter import *
# #Pylance is telling me this is bad fashion (so I'm commenting it out), and lazy imports haven't been implemented
#yet in python 3.11 (which means too much memory is used for stuff I'm not actively using).
# Python 3.14 (which I have as well) DOES have lazy imports, and I've tried it in personal apps.
# It also has multithreading, which python 3.13 (the one supported in class) does *not* support, so I'm sticking with
# best practices for 3.11 for now and importing each module manually.
from tkinter import ttk, messagebox, Toplevel, Label, Button, Entry, mainloop
from Geopoint import GeoPoint
import sqlite3

# Create tk windows
root = tk.Tk() #adding a root window so that #welcomeWindow doesn't have to be, this way we can destroy it later
root.withdraw() #hide the root window because I don't want it around

mainWindow = Toplevel()
#mainWindow.attributes('-type', 'dialog')
mainWindow.configure(bg='cornsilk3')
resultsWindow = Toplevel()
#resultsWindow.attributes('-type', 'dialog')
resultsWindow.configure(bg='cornsilk3')

# Title our windows
mainWindow.title("GeoPoint Comparer - BellP11")
resultsWindow.title("Comparison Complete!")

# Set Window Geometries
mainWindow.geometry("625x400")
resultsWindow.geometry("400x100")

# Add text to our windows
#Label(welcomeWindow, text="Please load the file containing your location data", fg="darkolivegreen3", bg='cornsilk4').grid(row=0, column=0, padx=5, pady=5)
mainWindowLatitudeLabel = Label(mainWindow, text="Latitude:", fg="darkolivegreen3", bg='cornsilk4')
mainWindowLongitudeLabel = Label(mainWindow, text="Longitude:", fg="darkolivegreen3", bg='cornsilk4')
mainWindowCalculateDistanceLabel = Label(mainWindow, text="Calculate", fg="darkolivegreen3", bg='cornsilk4')
resultsWindowLabel = Label(resultsWindow, text="", fg="darkolivegreen3", bg='cornsilk4')

# Create buttons
#Button(welcomeWindow, text="Exit", command=root.destroy).grid(row=2, column=0, padx=1, pady=10)
mainWindowCloseButton = Button(mainWindow, text="Close", fg="darkolivegreen3", bg='cornsilk4', command=root.destroy).grid(row=5,column=0)
resultsWindowCloseDialogButton = Button(resultsWindow, text="Close", fg="darkolivegreen3", bg='cornsilk4', command=resultsWindow.destroy)

# Create spreadsheet-like display
spreadsheet = ttk.Treeview(mainWindow, columns=("City", "Latitude", "Longitude"), show="headings")
spreadsheet.heading("City", text="City")
spreadsheet.heading("Latitude", text="Latitude")
spreadsheet.heading("Longitude", text="Longitude")
spreadsheet.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Create Text Entry widgets
entryText = tk.StringVar(value="Enter path or click 'Select'")
#welcomeWindowFileSelectorTextEntry = Entry(welcomeWindow, textvariable=entryText, width=21)
#welcomeWindowFileSelectorTextEntry.grid(row=1, column=0, padx=10)
mainWindowLatitudeTextEntry = Entry(mainWindow)
mainWindowLongitudeTextEntry = Entry(mainWindow)
mainWindowLatitudeTextEntry.grid(row=0, column=1)
mainWindowLongitudeTextEntry.grid(row=1, column=1)
mainWindowLatitudeLabel.grid(row=0, column=0)
mainWindowLongitudeLabel.grid(row=1, column=0)
mainWindowCalculateDistanceLabel.grid(row=2, column=0)

# Store GeoPoints
geo_points = []

# Load file and populate spreadsheet
def loadFile():     #I should have renamed this in the refactor, but I didn't want to. It pulls from a db now.
    """
    Loads in data from a database and formats it for later use, reports back an error in the console if it fails for some reason.
    
    """    
    try:
        conn = sqlite3.connect('Points.db')
        cursor = conn.cursor()
        cursor.execute("SELECT point_descriptor, point_latitude, point_longitude FROM Points")
        rows = cursor.fetchall()
        conn.close()
        #^^Do that sql stuff, ya'know, queries. 
        geo_points.clear()
        spreadsheet.delete(*spreadsheet.get_children())

        for desc, lat, lon in rows:
            spreadsheet.insert("", "end", values=(desc, lat, lon))
            point = GeoPoint(float(lat), float(lon), desc)
            geo_points.append(point)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load file: {e}")

# Calculate closest point
def calculateClosest():
    try:
        user_lat = float(mainWindowLatitudeTextEntry.get())
        user_lon = float(mainWindowLongitudeTextEntry.get())
        user_point = GeoPoint(user_lat, user_lon, "User Location")

        distances = []
        for point in geo_points:
            deltaLat = point.getPoint()[0] - user_point.getPoint()[0] #type:ignore
            deltaLon = point.getPoint()[1] - user_point.getPoint()[1] #type:ignore
            lat1_2 = [point.getPoint()[0], user_point.getPoint()[0]] #type:ignore
            dist = GeoPoint.distance(deltaLat, lat1_2, deltaLon)
            distances.append(dist)

        if distances:
            indexofDistance = distances.index(min(distances))
            closest = geo_points[indexofDistance].getDescription()
            resultsWindowLabel.config(text=f"The closest location to you is {closest}")
            resultsWindowLabel.grid(row=0, column=0, padx=10, pady=10)
            resultsWindowCloseDialogButton.grid(row=1, column=0, padx=10, pady=10)
            resultsWindow.deiconify()
        else:
            messagebox.showinfo("Result", "No distances were calculated.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric latitude and longitude.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Buttons

mainWindowCalculateDistanceButton = Button(mainWindow, text="Calculate", fg="darkolivegreen3", bg='cornsilk4', command=calculateClosest)
mainWindowCalculateDistanceButton.grid(row=2, column=1, padx=10, pady=10)

# Hide windows until needed
resultsWindow.withdraw()
loadFile() #loads the DB, named such due to laziness in refactor. In production code I'd be cleaner.
mainloop()