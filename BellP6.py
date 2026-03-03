#BellP6
#Programmer: Nora Bell
#Email: nbell8@cnm.edu
#Purpose: To demonstrate competency in functions
import math
from os import system
from time import sleep
def consoleClear(): #handy little helper to keep our outputs clear
    system('clear')
def header(): #welcome the user, explain the purpose of the app
    consoleClear()
    print("Welcome to the ATCF Distance Calculator") #ATCF is "As the crow flies", an out of use english phrase meaning "directly, with no creedence to obstacle"
    print("Using this script one can calculate the distance in Kilometers between two points on Earth")
    print("Distance reports will not be perfect because the formula used assumes the Earth is a ")
    print("perfect sphere, when it is in fact an 'Oblate Spheroid'.")
    sleep(3)
    print('''
        ░▒▓██████▓▒░                      ░▒▓████████▓▒░ 
     ░▒▓█▓▒░   ░▒▓█▓▒░                  ░▒▓█▓▒░    ░▒▓█▓▒░ 
    ░▒▓█▓▒░     ░▒▓█▓▒░              ░▒▓█▓▒░          ░▒▓█▓▒░ 
   ░▒▓█▓▒░       ░▒▓█▓▒░            ░▒▓█▓▒░            ░▒▓█▓▒░ 
    ░▒▓█▓▒░     ░▒▓█▓▒░              ░▒▓█▓▒░         ░▒▓█▓▒░ 
     ░▒▓█▓▒░   ░▒▓█▓▒░                  ░▒▓█▓▒░    ░▒▓█▓▒░ 
        ░▒▓██████▓▒░                      ░▒▓████████▓▒░ 
          Sphere                          Oblate Spheroid
       Perfectly Round               	  Slightly Bulged 
                                           at the Middle                     
          
          ''')
    sleep(2)
    print("For most situations, especially relatively small distances, this difference shouldn't matter.")
    sleep(3)
    consoleClear()
def get_location(): #gather inputs, return them as a tuple
    place2 = ""
    if loc1 != []: #simple logic to determine if this is the first or second time get_location() has been called once or twice on this time around.
        place2 = "second "
    lat = float(input(f"Enter your {place2 }latitude in Decimal Degrees:  ").strip())
    lon = float(input(f"Enter your {place2 }Longitude in Decimal Degrees:  ").strip())
    place2 = ""
    return lat,lon
def distance(loc1,loc2):
    #Convert to radians, all the resources I saw online said to do this manually, but why? the radians method is built into 'math'
    lat1 = math.radians(loc1[0])
    lat2 = math.radians(loc2[0])
    lon1 = math.radians(loc1[1])
    lon2 = math.radians(loc2[1])

    #Calculate Deltas, I'd use the Delta symbol here but idk if windows can handle unicode characters like that in its terminal like *nix can
    deltaLat = lat2 - lat1
    deltaLon = lon2 - lon1

    #Do the Math, Apply the Haversine formula to calculate the distance between our points in KM
    a = math.sin(deltaLat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(deltaLon / 2)**2
    radiusKM = 6371
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radiusKM*c #This still feels illegal, but I'm doing it anyway becasue it looks like it's pretty much the standard.
    #If I can be totally honest, I don't really understand this formula, I referenced a lot of online resources (mostly from geeksforgeeks.com) 
    #to handle this section, math (especially trigonometry) isn't my strong suit, logic is.


header()
while True:
    loc1,loc2 = [],[] #Initialize loc* as lists for mutability, we're assigning tuples to them and we need them workable.
    loc1 = get_location() #returns tuple (lat,lon), assigns to loc*
    loc2 = get_location()
    dist = round(distance(loc1,loc2),2) #returns distance using loc* as params, round to 2 decimal places
    print(f"Location 1 is {dist} Kilometers away from Location 2")
    doAgain = input("Would you like to compare another two locations? (Y/n) :  ").strip().upper() #
    if doAgain != 'Y': #simple logic to either quit or repeat
        consoleClear()
        print("Sayonara!")
        exit()
    