#---------Opening Demo---------------------------------------------------
def openDemo():
    #1 Write a list that contains the numbers 1-5
    list1 = [1,2,3,4,5]


    #2 Access the third element in a list containing 10,20,30,40,50
    list2 = [10,20,30,40,50]
    prob2Ans = list2[2]


    #3 Using slicing, access the last three items in a tuple
    tup = (1,2,3,4,5,6)
    prob3Ans = tup[-3:]
    print(prob3Ans)


    #4 Using slicing, reverse a string
    string = "This is a string"
    rString = string[::-1]
    print(rString)


    #5 Check if an element exists in a list using in
    trueOrFalse = 20 in list2
    print(trueOrFalse)
    trueOrFalse = 90 in list2
    print(trueOrFalse)

#openDemo()     #comment this line out to disable this part of the script


#--------End Opening Demo------------------------------------------------

'''
=========================================================================
Dictionaries - A datatype that stores data in a key:value pair
=========================================================================
    Dictionaries are particularly useful in building databases, as each cell 
        contains multiple datapoints that can be co-referenced.
    Today we will learn to build and manipulate dictionaries.
'''

#------------Example------------
def dictExample1():   #This is an example of using dictionaries to store and pull data
    dictionaryOne = {'Amy':27, 'Bob':32, 'Charlie':84, 'Eduardo':33}
    print(dictionaryOne)
    print('You may also pull a single item')
    print('  print(dictionaryOne["Charlie"]) will return Charlie\'s age')
    print(dictionaryOne['Charlie'])
    print('To print just the names, we can use "print(dictionaryOne.keys()")')
    print(dictionaryOne.keys())
#Just a note - If we were making a phone book using numbers which contain mathematical operating symbols,
#  we must use strings to contain our numbers, not ints or floats

#dictExample1()   #comment this out to disable this section of code


def pListExample1():    #This is the same as above, but with parallel lists
                        #Notice this does in two lines what the above code could do in 1
    names = ['Amy', 'Bob', 'Charlie', 'Eduardo']
    ages  = [  27 ,   32 ,       84 ,       33]
    nameInd = names.index('Charlie')
    print(ages[nameInd])


#pListExample1()   #comment this out to disable this section of code



##############################
#Basic Dictionary Operations:
def dictBasics():
    dictionary = {'key':'val'}
    print(dictionary)
    print(len(dictionary)   )       #returns the number of items in dictionary
    dictionary['key']          #returns the value associated with `key`
    del dictionary['key']      #Deletes items associated with `key`
    print(dictionary)
    dictionary['key'] = 'val2'    #associates `key` with new value `val`
    print(dictionary)

    print('key' in dictionary )     #Checks for an item `key` in dictionary `dictionary`, Boolean return
    dictionary['key2']='newVal'     #Add a new key:value pair to the dictionary
    print(dictionary)
#dictBasics()   #Comment this line out to disable this section of code

def PhonebookDemo():
    print('Make a new Phonebook, add two people')
    PhoneBook = {'Adam':1234, 'Kevin':2345}
    #Add stuff
    print(PhoneBook)
    print('Add a few more names')
    PhoneBook['Bobert'] = 9876
    print(PhoneBook)
    PhoneBook['Cloud'] = 7777
    print(PhoneBook)
    print("Add the name trudy, with phone number 8888")
    PhoneBook['Trudy'] = 8888
    print(PhoneBook)
    print("Actually, I don't like trudy, delete her")
    del PhoneBook['Trudy']
    print(PhoneBook)
    print('Kevin got a new phone number, its 92873, update it')
    PhoneBook['Kevin'] = 928734
    print(PhoneBook)
#PhonebookDemo()    #Comment this line out to disable this section of code

'''
======================================
======================================
Alright, so here's the deal with keys. 
These lil shits can be just about anything, even nothing!
____________________________________________
You can initialize an empty dictionary with
        dict={}
    Then you can add stuff to it with
        dict[key:value]
'''

#Let's embed a dictionary entry as a string
def embeddedCallDemo():
    PhoneBook = {'Amy':123, 'Bob':234, 'Chuck':345}
    print('This string is in the pre 3.6 format')
    print("Bob's phone number is %s"%PhoneBook['Bob'])
    print('This string is in the new style, standard as of python 3.6')
    print(f"Amy's phone number is {PhoneBook['Amy']}")

#embeddedCallDemo()

'''
=====================================
        Dictionary Methods
=====================================
append()
extend()
get()
keys() - gives all the keys in a list, takes no arguments
value()
items()
update()
pop()
popitem() - removes the last added value from the dictionary
clear()
copy()
'''


def methodsDemo():
    person = {'name':'Alice', 'age':25, 'email':'alice@email.com'}
    key_person=list(person.keys())
    print(','.join(key_person))
    pair=person.popitem()
    print(pair)
    person.popitem()

    print(person)
methodsDemo()