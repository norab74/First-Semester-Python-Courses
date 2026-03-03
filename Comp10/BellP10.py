#BellP10
#Programmer: Nora Bell
#Email: nbell8@cnm.edu
#Purpose: Add file handling to existing application instead of using hardcoded info
    
from PySide6.QtWidgets import QApplication #needed to run Qt applications
from ui import CourseApp #this is where the magic happens
import sys #needed to execute/control applications outside the python interpreter environment

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = CourseApp()
    window.show()
    sys.exit(application.exec())
    

