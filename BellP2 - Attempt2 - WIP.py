#BellP2
#Programmer: Nora Bell
#Email: nbell8@cnm.edu
#Purpose: Provide a user access to cleanly presented datapoints regarding US states from a list

'''
This code is highly modularized, each individual snippet is designed to function independently of the rest, so long as variable names and inputs are
tweaked to match the circumstances. This is part of an attempt by the programmer to build a library of modularized components that can be cut and pasted
to suit her needs in a given moment. This theme of modularizing code that objectively does not benefit from it will continue as the programmer does not believe
in single use objects, code included. All code can and should be recycled. Some of this code even is recycled from earlier assignments, such as "consoleClear()".

This code has been produced with the assistance of a selfhosted GPT-oss model trained on 20 Billion parameters with a system prompt designed to produce outputs
conducive to learning for a programmer in training, rather than generating ready to use code.
'''
#--------Begin initDatabase()-----
def initDatabase() -> list[list]:
    #init db
    dbMaster = []
    #Populate dbMaster with four rows of 50 empty values
    for i in range(4):
        dbMaster.append([None]*50)
    #return dbMaster variable to the main program
    return dbMaster
#--------End initDatabase---------


#--------Begin generateFactLists()
def generateFactLists() -> list[str]:
    state_names = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
                "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
                "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
                "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
                "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee",
                "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    state_capitals = ["Montgomery", "Juneau", "Phoenix", "Little Rock", "Sacramento", "Denver", "Hartford", "Dover",
                    "Tallahassee", "Atlanta", "Honolulu", "Boise", "Springfield", "Indianapolis", "Des Moines",
                    "Topeka", "Frankfort", "Baton Rouge", "Augusta", "Annapolis", "Boston", "Lansing", "Saint Paul",
                    "Jackson", "Jefferson City", "Helena", "Lincoln", "Carson City", "Concord", "Trenton",
                    "Santa Fe", "Albany", "Raleigh", "Bismarck", "Columbus", "Oklahoma City", "Salem",
                    "Harrisburg", "Providence", "Columbia", "Pierre", "Nashville", "Austin", "Salt Lake City",
                    "Montpelier", "Richmond", "Olympia", "Charleston", "Madison", "Cheyenne"]
    state_join_order = [22, 49, 48, 25, 31, 38, 5, 1, 27, 4,
                        50, 43, 21, 19, 29, 34, 15, 18, 23, 7,
                        6, 26, 32, 20, 24, 41, 27, 26, 
                        9, 3,  27, 11, 12, 39, 17,
                        46, 33, 2, 13, 8, 40, 16,
                        28, 45, 14, 10, 42, 35, 30, 44]
    state_congressional_districts = [7, 1, 9, 4, 52, 8, 5, 1, 28, 14,
                                     2, 2, 17, 9, 4, 4, 6, 6, 2, 8, 
                                     9, 13, 8, 4, 8, 2, 3, 4,
                                     2, 12, 3, 26, 14, 1, 15,
                                     5, 6, 17, 2, 7, 1, 9,
                                     38, 4, 1, 11, 10, 2, 8, 1]
    return state_names, state_capitals, state_join_order, state_congressional_districts
#--------End generateFactLists()--



#--------Begin populateDatabase()-
def populateDatabase(dbMaster: list[list], row:int, values: list[str]) -> None:
    #here we import dbMaster, a list of lists
    #we also import the variables "row" and "values", and integer and list of strings
    if len(values) != 50:
        raise ValueError('''Working database corrupt, please restart the program
                         
                         Explaination: values!=50, if values!=50 then dbMaster will
                         misalign and report incorrect data back to the user'''
        )
    #Replace the entire addressed row with the values from our fact lists
    dbMaster[row] = values
#--------End populateDatabase()---

#--------Begin UI()---------------
def UI(dbMaster, state_names):
    while True:
        #Clear the console
        consoleClear()
        #Greet the user
        print('Welcome to the Mini US State info Repository:')
        print('Please enter a US state')
        print('You may also type "quit" to exit')
        #Request input
        userSelection=input(":")
        #Convert input to lowercase to compare with list more effectively
        userSelection=str.lower(userSelection)
        #convert list to lowercase to compare with user input more effectively
        state_names = [i.lower() for i in state_names]
            #notice this list (state_names) is not the list we interact with to pull the actual state name below, this is because
            #it is more convenient from a coding perspective to create a new list in memory to interact with than to interact with the hardcoded list.

        #check membership of userSelection in list state_names, if successful continue, else handle invalid input 
        if userSelection in state_names:
            #self explainatory, making new variable to interact with below by applying the index method to our list
            indexOfUserSelection = state_names.index(userSelection)
            
            
            #Ok so this block is a doozy:
            #first we use the "print(f)" function instead of the "print()" function, this is becasue we will be injecting some variables
            #in the first line of our text block, we use {dbMaster[0][indexOfUserSelection]}
            #the {} allows insertion of variables into a print statement
            #dbMaster[0] refers to the first "row" of our list (it is actually index zero of our list, which itself is a list)
            #[0][indexOfUserSelection] refers to the exact X*Y position of the item we are calling, where x=index+1 and Y=indexOfUserSelection+1
            #This analogy falls short of course because our database is not actually a 4x50 grid of data, it is just most easily imagined and interacted with
            #as though it were.
            #we continue calling the same snippet within our print statement with small tweaks to pull different datapoints from our set.
            input(f''' 
                    You have selected: {dbMaster[0][indexOfUserSelection]}

                    {dbMaster[0][indexOfUserSelection]} was the {dbMaster[2][indexOfUserSelection]}th state to join the union.
                    The state capital of {dbMaster[0][indexOfUserSelection]} is {dbMaster[1][indexOfUserSelection]} and it has
                    {dbMaster[3][indexOfUserSelection]} congressional districts.

                    Please press "enter" to return:
                    ''')
        #add support for gracefully exiting the program without calling EOF    
        elif userSelection == 'quit':
            print('Goodbye')
            break
        #handle invalid inputs
        else:
            print('You have made an invalid selection, please try again')
#--------End UI()-----------------

#--------Begin consoleClear()-----
def consoleClear():
        os.system('clear')
#--------End consoleClear()-------

#--------Begin Main()-------------
#While not strictly necessary, wrapping everything inside a main function can make code a bit cleaner
def main():
    dbMaster = initDatabase()
    #comment out the next line to disable this debug step
    #print(dbMaster)
    state_names, state_capitals, state_join_order, state_congressional_districts = generateFactLists()
    #comment out the next line to disable this debug step
    #print(dbMaster)
    populateDatabase(dbMaster, 0, state_names)
    populateDatabase(dbMaster, 1, state_capitals)
    populateDatabase(dbMaster, 2, state_join_order)
    populateDatabase(dbMaster, 3, state_congressional_districts)
    #comment out the next line to disable this debug step
    #print(dbMaster)
    UI(dbMaster, state_names)
#--------End main()---------------

#--------Handle Imports-----------
import os

#--------Call main()--------------
main()