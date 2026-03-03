#BellP4
#Programmer: Nora Bell
#Email: nbell8@cnm.edu
#Purpose: To demonstrate understanding of dictionaries.
from time import sleep

#Ensure the script loops back to the beginning
while True:
#Create a dictionary with common phrases and their translations in another language
        translate = {
                "Hello" : "Guten Tag", 
                "Good Morning" : "Guten Morgen", 
                "I am eating a sandwich" : "Ich isst eine Belegtes Broet",
                "I Love you" : "Ich liebe Dich", 
                "My cat is too fat" : "Meine Katze ist zu gross",
                "There are plenty of fish in the sea" : "Dar sind Sehrfischen in Das Meer",
                "I can see a rainbow" : "Ich kann sehst einen Regenbogen!", 
                "Potatoes are very delicious" : "Kartoffeln bist sehr lecker"}
        #Display Display a list of the phrases in language 1 to the user (hint use the .keys() method of the dictionary class)
        #Make our display more pretty
        englishPhrases = str(translate.keys())
        englishPhrases = str(englishPhrases).replace('[','\n')
        englishPhrases = str(englishPhrases).replace(']','\n')
        englishPhrases = str(englishPhrases).replace('dict_keys(\n','')
        englishPhrases = str(englishPhrases).replace(')','')
        print(str(englishPhrases).replace(', ','\n'))
        #Ask the user to type in a phrase to translate
        userPhrase = str(input("Type one of the above phrases here, then hit enter:"))
        #Display the translation
        print(f"In German, this is :{translate[userPhrase]}")
        sleep(4)
