#BellP1
#Programmer: Bell, Nora
#EMail: nbell8@cnm.edu
#Purpose: Provide a tool to calculate the volume and surface area of a square pyramid.


#!/usr/bin/env python3


#This script is a calculator to handle square pyramids.
#It will calculate the volume and surface area based on user input.
def mainLoop():
    #Import Libraries
    import math
    import os
    from time import sleep
    
    #Define greeting function to ensure a positive user experience.
    def greeting():
        print('Hello and welcome to my Square Pyramid calculator')
        sleep(1)
        input("Please press Enter/Return to continue")
        consoleClear()

    #Gather facts re:pyramid from user
    def gatherData():
        L=float(input('Please enter the Base Length of your pyramid: '))
        consoleClear()
        H=float(input('Please enter the Height of your pyramid: '))
        consoleClear()
        #return variables back to mainLoop
        # functionating the program improves memory safety, but also requires the use of explicit memory management
        #"return" will handle said memory management for us in this case
        return(L,H)
    
    #Calculate the slant height of the given pyramid
    def slant(L,H):
        #Pythagoras was right
        S=math.sqrt((H**2)+(L/2)**2)
        #return S for availability in mainLoop()
        return S
    

    #Calculate the surface area of the given pyramid, ignoring the base side
    def surfaceArea(S,L):
        #Use the formula for Surface Area of a triangle with the dimensions supplied in gatherData()
        face=(S*L)/2
        #Multiply the results of the above by 4 to handle all sides (sans base)
        surfaceArea=face*4
        #return the variable surfaceArea to mainLoop()
        return surfaceArea
    
    

    #Calculate the volume of the given pyramid
    def volume(L,H):
        #Use the formula for volume of a square pyramid with the dimensions supplied in gatherData()
        #to reduce the code needed to handle this operation, we will define L^2 explicitly
        Lsquared=math.pow(L,2)
        volume=(Lsquared*H)/3
        return volume
    
    #Report results back to the User
    def report(surfaceArea,volume):
        print("The Area of the pyramid is ", surfaceArea, "units squared")
        print("The Volume of the pyramid is ", volume, "units cubed")
        #prompt user to trigger loop or exit with EOF
        print("Press Enter to Calculate another pyramid")
        input("Press Ctrl-D (Ctrl-Z+Enter on Windows) to exit the calculator")
        consoleClear()
        mainLoop()
    #Clear the console to clean things up and ensure output is presented neatly
    def consoleClear():
        os.system('clear')


    #Define order of mainLoop()
    greeting()
    L, H = gatherData()
    S=slant(L, H)
    surfaceArea=surfaceArea(S, L)
    volume=volume(L, H)
    report(surfaceArea, volume)

#Call the main loop to execute the program
mainLoop()