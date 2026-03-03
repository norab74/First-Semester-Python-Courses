#Python 3.11
#Competency 3

#To open the class the Prof has recommended w3schools.com for additional learning.

#In comp2, we learned Sequences.
    #Today, we will be using Strings.
    #Strings are a type of Sequence, but they have some special rules
    # strings can be kept in quotes, double quotes, or triple quotes for multiline strings
        #Example:
            #'this is a string'
            #"this is also a string"
            #'''this 
#                    is        
#                        also 
#                                a 
#                                    string'''


#Lists and dictionaries are mutable, but strings, like tuples, are immutable
#   []          {}                         ''""            ()

"""#--------Begin Demo--------#
#A string is a sequence of characters enclosed in quotes
string='I am  string 1'
print(string)

string2="I am string 2"
print(string2)

string3='''Believe it or not,

I, 

am string 3'''
print(string3)


#--------End Demo----------#"""

#All operations that can be performed on a sequence EXCEPT item and slice assignments.
# As Strings also cannot be edited, they are immutable.

"""#--------Begin Demo--------#

website='http://www.python.org'
website[-3:]='com'
print(website)

# output
#Traceback (most recent call last):
#  File "/home/nora/SyncToOneDrive/Python/Python Fundamentals/Comp3 notes.py", line 47, in <module>
#    website[-3:]='comm'
#    ~~~~~~~^^^^^
#TypeError: 'str' object does not support item assignment

#--------End Demo----------#"""

"""#--------Begin Demo--------#
website='http://python.org'
website=website[:-3]+'com'
print(website)
#--------end Demo----------#"""
##Why this works:
    ## In Python, slicing a string returns a new string, so the expression website[:-3] is still a str.






#Reassigning a string
"""#--------Begin Demo--------#
text="Good Morning"
text="Good Night"
print(text)
#--------end Demo----------#"""


##printing with commas
"""#--------Begin Demo--------#
name = "Gumby"
title = "Mr"
salutation = "Hello"
print(salutation, title, name)
#--------End Demo----------#"""

##printing with plusses
##Concatenating varying types
        #A num cannot be concatenated onto a str. To make this occur, the num must be converted to an str. This may be done a few ways
            #one can permanently make the change by setting var=str(var), or one can make the change temporarily by calling str(var)
"""#--------Begin Demo--------#
name = "Gumby,"
title = "Mr"
salutation = "Hello"
age = 17
print(salutation + title + name + str(age))
age = str(age)
print(salutation + title, name + age)
#--------End Demo----------#"""





#Conversion Specifiers in old deprecated style


"""#--------Begin Demo--------#
format = "Hello, %s, %s enough for ya?"
values = ('world', 'Hot')
name = str(values[0])
print(format%values)
print("Hello,%s"%name)
#--------End Demo----------#
#--------MultiplePlaceholders Demo--------#
s1='Bob'
age = 25
print("Name: %s,Age: %s"%(s1,age))
#--------End MultiplePlaceholders Demo----#"""


#Float Format Specifiers

#       The format %.3f can be used to limit output of a num to 3 decimal places
#       the same can be done with 1 decimal (%.1f), 2 decimals (%.2f) or any other number

#To limit floating point precision, use :".`num`f"

# for example, 5.1238719287.5f=5.12382, $val.17f, `var`:.2f, `var`:.4f

#--------Begin Demo---------
#old format - deprecated as of 3.6
'''format = "Pi with three decimal places is equal to: %.3f"
pi = 3.14159265
print(format%pi)


#new format  - Recommended as of 3.6
pi = 3.14159265
print(f"Pi with three decimal places is equal to {pi:3f}")'''
#--------End Demo----------- # 


'''
# -------Begin Demo---------- 
#STRING FIND METHOD
    #Finds the argument in string and returns the index where arg begins in string
    #format =           string.find(arg)
sentence = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood'
numWood = sentence.find('wood')
print(numWood)

# You may specify a start and end index in your args
# format for such =     string.find(  arg  ,  startIndex  ,  endIndex  )
# As Always - startIndex is inclusive, endIndex is exclusive
'''
'''
Other Methods:
    rfind - 
    index - 
    rindex - 
    count - 
    startswith - 
    endswith - 
    '''
#--------End Demo-----------

#--------Begin Demo---------
seq = ['1','2','3','4','5']
sep = '+'
print(sep.join(seq))

#--------End Demo-----------




