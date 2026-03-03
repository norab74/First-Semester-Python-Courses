##Goals for this assignment:
'''    Create 3 lists to act as databases to store:
        state names
        state capitals
        number of congressional districts and order joined the Union

The program should initialize 3 lists with the above Data
The program should ask the user to enter the name of a state 
the program should parse the lists to find the index of the state the user entered and handle unacceptable inputs.
the program should then report back the the requested information about the state requested

'''

#BellP2
#Programmer: Nora Bell
#Date: 09/15/2025
#Purpose: Provide user the capability to look up information about US states
#Disclaimers : LLM generated code has been sampled, mostly for the purpose of list population. Said code has been
    #reviewed and edited by the programmer to promote factual acuracy and to restyle the code to the programmer's preferences.


#Initialize our empty lists with 50 entries each, one for each US state, initialize our empty variables at the same time
def createLists(dbList ,state_names, state_capitals, 
                state_join_order, state_congressional_districts, userState):
    empty = [] * 50
    state_names = empty
    state_capitals = empty
    state_join_order = empty
    state_congressional_districts = empty
    dbList = []
    userState = []
    return state_names, state_capitals, state_join_order, state_congressional_districts, dbList, userState

#Fill our lists with data; the indexes of each datum shall match its cooresponding state.
def populateLists(state_names, state_capitals, state_join_order,
                   state_congressional_districts, dbList):
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
                        50, 43, 21, 19, 34, 15, 16, 18, 23, 6,
                        26, 32, 20, 24, 41, 37, 9, 36, 47, 30, 12, 17,
                        29, 33, 2, 42, 13, 3, 39, 44, 11, 10, 35, 40, 45, 14, 46]
    state_congressional_districts = [7, 1, 9, 4, 53, 7, 5, 1, 27, 14,
                                    2, 2, 18, 9, 4, 6, 6, 2, 8, 9,
                                    14, 8, 4, 1, 3, 4, 2, 12, 27, 21, 13, 1,
                                    16, 5, 18, 2, 7, 1, 9, 11, 3, 10, 8, 1, 8, 1]
    #add lists to database
    state_names = dbList[0]
    state_capitals = dbList[1]
    state_join_order = dbList[2]
    state_congressional_districts = dbList[3]
    return state_names, state_capitals, state_join_order, state_congressional_districts, dbList
def acceptInput(state_names, state_capitals, state_join_order,
                   state_congressional_districts, dbList):
    while true:
        userState=input("Please type the name of a US State: ")
        if lower.userState in lower.dbList[0]:
            dbListIndex = dbList.index(userState)
            dbState     = dbList.index(state_names)
            dbCapitals  = dbList.index(state_capitals)
            dbOrder     = dbList.index(state_join_order)
            dbCongDist  = dblist.index(state_congressional_districts)
            '''Ok so this one is a bit complicated, what I've done here is
            created a nested database. dbList is a database which holds 
            the positions of the other 4 databases in an index. The other 
            4 databases hold individual datapoints regarding the states, 
            aligned by index. 

                    it breaks down as print(f  '  listoflists[listofnames[indexofgivenname]]  )
            its a little bit disgusting, and super clunky to read, but it highlights the modularity
            of the functions we're working with
            '''
            print(f'''
                You have selected: {dbList[dbState[dbListIndex]]}

                {dbList[dbState[dbListIndex]]} was the {dbList[dbOrder[dbListIndex]]}th state to join the union.
                The state capital of {dbList[dbState[dbListIndex]]} is {dbList[dbCapitals[dbListIndex]]} and it has
                {dbList[dbCongDist[dbListIndex]]} congressional districts
                ''')
        else:
                print('You have entered an invalid selection, please try again')

createLists(dbList ,state_names, state_capitals, state_join_order, state_congressional_districts)

        
        




