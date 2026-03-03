'''
Conditional statements = Decision making

Tell the computer to make a decision.

These are logic conditions, at their most basic these act as "yes/no/or" gates. 

If you'd like to make more complicated logic, you may string together conditionals to handle (for example) xor or nand logic.
Keep in mind, in an interpretive language such as python, NAND logic may cause infinite loops.
'''

'''
##Example##

if condition0:
    then
elif condition1:
    then
else:
    then

##/Example##
'''

'''
Loops:
    While a condition is true, keep doing the thing over and over and over and over and over and over
'''




#ASSIGNMENT OPERATIONS
'''
A=5
Cat='cute'
Assignment operations assign a value to a variable.

Assignment operations can also modify a value
A+=1 will iterably add one to the value assigned to A
in a loop:
    while True:
        a+=1
        print(a-1)
will constantly count up by one, starting at 0, in a printout to the user.
'''

#SEQUENCE UNPACKING
'''
x, y, z = 1, 2, 3
print(x, y, z) #output: 1 2 3
x, y = y, x
print(x, y, z) #output: 2 1 3

Sequence unpacking allows you to assign values from a sequence into multiple variables.
'''
#a,b=[1,2]
#print(a) #output 1
#print(b) #output 2
'''the Python interpreter unpacks the input:
    [1,2]
   into 1 and 2, assigning them to the requested variables in order of occurance.
   You may do this with lists, strings, and tuples. Remember a string is a string of single characters
.popitem() is a built-in Python method that can take no arguments.

It removes the last item from a dictionary and returns a tuple containing the key and value of that item,
 which can then be stored or used as needed.
'''

#dict = {
#    'key1':'value1',
#    'key2':'value2',
#    'key3':'value3'
#    }
#key, value = dict.popitem()
#print(key,value)
#print(dict)


'''
Chained Assignments:
y = math.pow(3,2) 
print(y) #output 9
x = y
print (x)#output 9
y = math.pow(2,3)
print(y, x) #output 8 9


in order to set a value to multiple variables, one must first assign the value to one variable, then assign that variable to the rest of the variables
 that should share the value, this is not persistant, so above the last line [   print(x,y)   ] results in [    8 9     ].

 This is because variables are independent of one another, even when assigned to eachother it is only their values that are being assigned, not the variable itself


 you may also enter y=x=math.pow(3,2), which is more compact and therefore results in a smaller script that will run faster

'''

#x=y=z=0
#x+=5
#print(x,y,z)


#AUGMENTED ASSIGNMENT
'''
x=2
x+=1

Augmented Assignment will perform a mathematical operation, then update the value.

This may also be done with strings, but note that instead of mathematical operations we will be using logical operations.

x="Cat"
x+="Dog"
print(x) #output CatDog

In this case, the logical operation we are performing is concatenation, this may also be done with multiplication by a numeral value
#Logical Multiplaction example:
#x="Cat"
#x*=9
#print(x)

All of the binary operators may be used for these logical operations (+, -, *, /, //, %)

#syntax : variable<operator>=expression

Division and Modulus cannot be applied to strings, this is illegal because one cannot divide by letters in base-10 maths, in certain circumstances it may be legal
but is frowned upon
'''

#Boolean Values
'''
a=True
b=False
print(a,b)
print(bool(0)) #false
print(bool('hi')) #true
print(bool([])) #false
print(bool({})) #false
print(bool([1,2])) #true
name=''
if not bool(name):
    print("The name is empty")


Boolean values and operators are used for simplifying logical operation

>>>bool('literally anything that is not an empty string or a literal 0 or None')
True
>>>bool('')
False
>>>bool(0)
False

'''

#Conditionals
'''
Conditional statements in python are used to make decisions in code
They allow your program to execute certain blocks of code only if a condition is true
The main conditional statements in Python are if, elif, and else

Syntax:
    if condition:
        action      #run if the first check succeeds
    elif otherCondition:   
        otherAction     #run if the first check fails, but the second check succeeds
    else:
        exceptionAction   #runs if above checks all fail

Conditionals follow basic logical syntax:
    If Condition is true, then do action, else ...
'''

#Example:
'''
age = int(input("How old are you? "))
if age >= 18: #Check if age is greater than 
    print('You can vote')
    if age >= 150:
        print('I diagnose you with dead')
    elif age >= 65:
        print('You are legally old')

elif age == 17: #check if age is exactly equal to 
    print('You are almost old enough to vote')
elif age <= 16:
    print('You are a minor')
else:
    print('You are a generic adult')
    '''

'''
More conditionals:
    name = input("What's ya name?")
    if name.endswith("namington"):
        print("Whaddup friend namington")
    else:
        print('sup stranger?')


Basically:
    Anything that could return a boolean can be used as a condition to build a conditional.

If you make a conditional statement that is always true:
    ---ex:  
        while True:
    ---
    You end up with an infinite loop

name = ''
while not name:
    name = input("Type ur name: ")
print("Yo, %s!"%name)
'''

#for i in range(0,10,-1):
'''So, here's an anomalous code snippet, the code overflows and iterates upwards to 0 from -100
This is clearly a bug, this should throw an error and that it doesn't means this is a potentially
 abusable unhandled exception who could have security implications.

 For example, consider the case of improperly sanitized inputs, the user could theorhetically input
 code which could iterate over variables meant to be private thereby printing information that should be secure to a console
 The information would of course not be formatted as it would be needed, but that it is potentially grabbable is neat.
'''
