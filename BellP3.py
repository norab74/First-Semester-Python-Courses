# BellP3
# Programmer: Nora Bell
# EMail: nbell8@cnm.edu
# Purpose: Provide the user with a prompt to search for various names of fruits 

#----------Outline----------
'''
a. Creates a sequence that has the names of seven fruits.
b. Asks the user for a sentence.
c. Tells the user how many fruits are in that sentence.
d. Displays a list of fruits in the sentence.
e. Finds and replaces one instance of a fruit in the sentence with “Brussel Sprouts”.
f. Displays the new sentence to the user.
'''



#----------\Outline---------





#A. Create a sequence that has the name of seven fruits


#Generate a list of fruits to interact with
#---------begin openFruitList()
def openFruitList(): 
    fruitList = ['Apple', 'Banana', 'Cherry', 'Durian', 'Elderberry', 'Fig', 'Grape']
    return fruitList
#---------end openFruitList()


#Generate a lowercase list of fruits to interact with, in case the user doesn't user capital letters
#---------begin lowercaseFruitList()
def lowercaseFruitList(fruitList):
    return [str.lower() for str in fruitList]
#---------end lowercaseFruitList)


#B. Ask the user for a sentence


#As the user for a sentence, convert to lowercase, also initialize our list for X-reffing
#---------begin askForSentence()
def askForSentence():
    sentence = input('Please type a sentence: ')
    lc_sentence = sentence.lower()
    print(f'''You said:
            {sentence}''')
    listInSentence = [] ##This should probably be handled elsewhere but idrc, it works.

    return sentence, lc_sentence, listInSentence

#---------end askForSentence()



#C. Tell the user how many fruits from our list are in their sentence
#---------begin countFruits()
def countFruits(fruitList, lc_sentence, lc_fruitList):
    fruitsInSentence = int(0) #how many fruits are in the sentence? initialize variable
    for val in lc_fruitList[:]: #initialize a for loop
        if val in lc_sentence: #check if our entries in lc_fruitlist exist in lc_sentence
            fruitsInSentence += 1 #if they do, increment by one
            print(f"There are {fruitsInSentence} fruit(s) from our list in your sentence.")
            print(f"The fruits we found are: {val}")
            return fruitsInSentence
        else:
            break
            

#---------end countFruits()


#D. Display a list of fruits in the sentence



#----------begin listFoundFruits()
def listFoundFruits(fruitList, lc_fruitList, lc_sentence, fruitsInSentence, listInSentence):
    if fruitsInSentence != 0: #check if there are fruits in the sentence
        for val in lc_fruitList[:]: #this is kinda hacky i think, there's gotta be a better way to do this
            iterFruit=val 
            if iterFruit in lc_sentence: #Check if the values in lc_fruitList are in lc_sentence, if they are print which ones.
                indexInFruitList = lc_fruitList.index(iterFruit)
                addToList = str(fruitList[indexInFruitList])
                listInSentence.append(addToList)
                print(f'''We found the following fruits in your list:
                {listInSentence}''')

            else: # otherwise pass
                pass
        
        return listInSentence
#-----------end listFoundFruits()


#E. Find and replace one instance of a fruit found in the sentence with "Brussels Sprouts"
#---------begin subVeg()

#prettify output, make our replacement, convert replacement sentence into tuple to strip extraneous output
def subVeg(listInSentence, sentence):
    for val in listInSentence:
        cutOut = val
        subSentence = sentence.replace(cutOut, "Brussels Sprout")  #For some reason, this outputs as though it were a tuple, but is a string. Ask prof about this one.
        subSentence = subSentence.replace("(","")
        subSentence = subSentence.replace(listInSentence[0].lower(), "Brussels Sprout")
        subSenTuple = tuple(subSentence.split(","))
        newSentence = subSenTuple[0]
        return newSentence
#---------end subVeg()



#F. Print the new modified sentence to the user
#---------begin printNew()
#Pretty self explanatory, just printing the new sentence with a silly intro
def printNew(newSentence):
    print(f'''
                Muahuahua, we have replaced one of your fruits with some dastardly Brussels Sprouts!
            It now reads:                   
                {newSentence}''')
    
def main():
    fruitList= openFruitList() #init fruit list
    lc_fruitList = lowercaseFruitList(fruitList) #init lowercase fruit list
    sentence = str(askForSentence()) #get input from user
    lc_sentence = sentence.lower()
    fruitsInSentence = countFruits(fruitList, lc_sentence, lc_fruitList)
    listInSentence = []
    listFoundFruits(fruitList, lc_fruitList, lc_sentence, fruitsInSentence, listInSentence)
    newSentence = subVeg(listInSentence, sentence)
    printNew(newSentence)
main()



