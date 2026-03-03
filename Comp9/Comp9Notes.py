'''
You forgot to Read Chapter 9, do that tonight! - 10-15-25


What is a GUI?
    Graphical User Interface
    User's are scared of command lines, so it's better to build a GUI to interact with alongside your TUI tools.
    Unlike console programs, users will interact with windows, buttons, and menus.
    Programs will wait indefinitely for the user to interact with one of these options, instead of executing linearly
    Events to monitor could be:
        Clicks
        Keystrokes
        Any form of HID (Human Interface Device) input
    
In traditional Programming:
    Programs are more like scripts, executing sequentially
In a GUI however:
    Programs will be driven by user input captured by an 'Event Loop'

Popular GUI Toolkits: I will use PyQT6
    Tkinter (builtin)
    wxPython (wrapper for wxWidgets)
    PyQt/PySide (5/6) (Qt framework bindings, similar to KDE)
    Kivy (for Touch Driven apps)
    PySimpleGUI (Wrapper for Tkinter/wx/Qt)
    GTK via PyGObject, DearPyGui, FLTK, Toga, etc.

Overview of Tkinter:
    Default GUI toolkit
    Based on Tcl/Tk; UNIX tool, does what it says and absolutely nothing more
    Uses Geometry Managers (pack,grid,place) for widget layout.
        Pack throws shit wherever it fits, left to right, top to bottom
        Grid lets you place things on a grid, like a spreadsheet
        Place allows for exact positioning of elements.
        EXAMPLE of Tkinter: (deindent 3x to run)
            import tkinter as tk
            def say_hello(): #this is bad practice for a production application. Don't print shit to the console, it's bad practice.
                print('Hello, World')
            root = tk.Tk();
            root.title('My App')
            btn = tk.Button(root, text='Click me', command=say_hello);btn.pack()
            root.mainloop()   #while "user pressed 'close'" == False




'''
