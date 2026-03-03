#Part 1: Functions
'''
Functions are re-usable codeblocks.
    Don't repeat yourself. Define the function once, call it as many times as you need.
Functions are the most basic level of abstraction: They serve to keep the complicated parts of the code behind the scenes.

'''
#Laziness is a virtue: Here is a demo of a simple recursion which prints fibbonacci numbers
'''
fibs = [0,1] #initialize a list with the first two values in the fibonacci sequence
for i in range(8): #set a limit of 9 places
    fibs.append(fibs[-2]+fibs[-1]) #logically apply formal definition of the fibonnacci sequence
print(fibs)
''' #this code is fine if we only wanna do it once, but what about if we wanna do it multiple times? It'd quite quickly become unruly to 
#continually add more and more instances of this code snippet.
'''
fib_numbers = [0,1]
amount = int(input('How many fibonaccis you want?  '))
for i in range(amount-2):
    fib_numbers.append(fib_numbers[-2]+fib_numbers[-1])
print(fib_numbers)
'''
#This is more flexible, but still not ideal.


#Lets define a function to make this less unruly:
'''
def fibs(num): #open function
    result = [0,1] #init result list
    for i in range(num-2): #iterate accross user defined range
        result.append(result[-2]+result[-1]) #do your math and shit
    return result #give the variable result back to the global scope
while True: #open a loop
    fibNumStr = input("How many Fibs?  ") #ask for input
    if fibNumStr == '' or fibNumStr == 0: #establish an exit condition
        break
    else:
        print(fibs(int(fibNumStr))) #do shit

        #DO NOT RUN THIS CODE WITH TOO MANY ITERATIONS, YOU WILL CRASH YOUR PC
   '''
'''
def fibs(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    fibs = [0,1]
    for i in range (n-2):
        fibs.append(fibs[-2]+fibs[-1])
    return fibs
fibOutput = fibs(int(input("How many fibs do you want?  ")))
print(fibOutput)
#This code is equivalent to the previous code, but is much cleaner
'''

#Simple function demo:
'''
def sayCat():
    speech = ["cat"]
    num = int(input("How many times should I say cat? I'm Logarithmic, be careful! "))
    for i in range(num):
        speech = speech*num
    print(speech)
sayCat()

#Do not run this code with too many iterations, above 8 starts to really stress the PC, above 9 will probably kill it.
#It's kind of a fork bomb
'''

#An actual fork bomb: using a simple recursive function. If we call sayCat() inside sayCat() we 
#can dramatically lower the threshhold where it will cause unwanted behavior
#Do not run this code, it is malicious.
'''
def bomb():
    while True:
        bomb()

bomb()
'''
'''
#Create a function to find th area of a rectangle
#Check Length and Width
def rectArea(L,W): #define our function, and the needed parameters
    print(f"The area of your rectangle is {L*W}")

L , W = (input("Please enter your Length and Width, separated by a space:  ").split()) #Gather the needed parameters for our function
rectArea(int(L),int(W)) #actually run the function
'''
'''
#Create a function to find the area of a circle
#Check radius and do math to it
def circArea(r): #define our function, call our paramaters
    import math
    pi=math.pi
    print(f"The area of your circle is {pi * r**2}.")
r = int(input("Please enter the radius of your circle:  ")) 
circArea(r)
'''


