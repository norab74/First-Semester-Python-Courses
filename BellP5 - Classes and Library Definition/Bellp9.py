#BellP9
#Programmer: Nora Bell
#Email: nbell8@cnm.edu
#Purpose: To demonstrate capability to make a User interface. Here I have used Qt6 via PySide6. I have used this to learn more effectively how
    #to make tools for my own use case which blend seamlessly with my own desktop environment (lxQt via i3wm), rather than the built-in tool
    #tkinter as suggested by the program spec.
    
from PySide6.QtWidgets import QApplication #needed to run Qt applications
from ui import CourseApp #this is where the magic happens
import sys #needed to execute/control applications outside the python interpreter environment

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = CourseApp()
    window.show()
    sys.exit(application.exec())
    

