#BellP1
#Programmer: Bell, Nora
#EMail: nbell8@cnm.edu
#Purpose: Provide a tool to calculate the volume and surface area of a square pyramid.
import math
height = float(input("Height of Pyramid: "))
base = float(input("Base width of Pyramid: "))
#calculate slant based on Height and Width
slant = float(math.sqrt((height**2)+(base**2)/2))
#Calculate a single side based on Width and Slant
faceArea = ((base*slant)/2)
#Calculate Surface Area of Pyramid (ignoring base)
surfaceArea = faceArea*4
#Calculate Volume based on Width and Height
volume = (base**2)*height/3
#Print results to the user
print (slant)
print("The Surface Area is ", surfaceArea, "units squared and the Volume is " ,volume, "units cubed.")
#Wait for user confirmation that answer has been read before exiting
input("Press Enter or Ctrl+D (Ctrl+Z on Windows) to exit")
