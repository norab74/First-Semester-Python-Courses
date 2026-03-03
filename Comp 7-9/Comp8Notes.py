#Comp 7 review:
'''
    What is a class?    
        1: Builds a skeleton for an object
        2: Has attributes(data) which describe the object
        3: Has methods(functions) which describe what the object can do
    Why?
        Allows us to make our program using Object Oriented Programming
        Enables us to build a workflow
''''''
#Comp 7 Demo:
class fruits:
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
fruit1 = fruits("Mango")
fruit2 = fruits("Banana")
print(fruit1.name, fruit2.name)
'''

###
### EXCEPTIONS:
###
'''
    Exceptions are a special type of class that define how an error is meant to be handled
    
    If an error is not handled, a traceback (kinda like an error message, but more verbose) will be returned with the error
    
    example:
        >>> 1/0
        returns:
        Traceback (most recent call last):
            File "<stdin>", line 1, in ?
        ZeroDivisionError: integer division or modulo by zero
        
    There are many types of exceptions
        For a complete list of built-in Exceptions, see: https://docs.python.org/3/library/exceptions.html
        
    Default behavior if an error occurs is to immediately kill the program to prevent potentially unwanted effects.
        We define exceptions to handle errors gracefully.
        We do this through reference of an exception class via a "Try->Except" block

####example:
try:
    1/0
except ZeroDivisionError:
    print("Hey, thats illegal bub, gonna sic the math police on ya")
finally:
    print("Good thing we caught that error")

#returns:
#    "Hey, thats illegal bub, gonna sic the math police on ya"
####endExample:


            


#Another example:
try:
    number = int(input("Enter a number"))
    postDivide = 1/number
    print(f"After division we have {postDivide}")
except ZeroDivisionError:
    print("tsk,tsk,tsk... Math crimes")
except ValueError:
    print("Whoa bucko, slow your roll, you can't divide by something that isn't a number")
except Exception as e: ##contextually, this should only ever trip due to bit-rot, cosmic radiation, code-injection by user.
    print("Yo, the fark did you just enter? I can't even")
    
    
    
    
OK great, so what is it?

    To represent exceptional conditions, Python uses exception objects
    If such an exception object is not hnandled in any way, the program will terminate to prevent damage.
    
    Each exception is an instance of the associate class
    These may be raised and caught in various ways
    This allows you to trap the error and do something about it, instead of just terminating.
    `  in business tech, failure is not an option, make sure things fail your way, or not at all   `
    
To raise an exception, you use the "raise" statement with an argument that is either a class or instance of a class
    if using a class, it is automatically instantiated anonymously
    ex: raise ValueError("invalid input")
    
    
    To print all exceptions, use "print(dir(Exceptions))"






Custom Exceptions:

    All exceptions MUST inheret from BaseException
    
    Custom exceptions will inheret from Exception, which inherets from BaseException
    You may also specify a specific exception to inheret from, for example to ban the number 2 from inputs you could:
        class TwoIsIllegal(ValueError):
            pass
    This will do everything ValueError does, as well as anything Exception does, as well as BaseException because of the 
        chain of inheretence.
    
    Do not deviate from this unless you know EXACTLY what you are doing.
    
    Example:
        class CustomException(Exception):
            pass
            
A Try-Except block may contain as many exceptions as it damn well please
    try:
        stuff
    except exception1:
        more stuff
    except exception2:
        even more stuff
    ...
    
    
    Sometimes there is a lot of bad stuff that can happen.
    Sometimes errors don't do anything potentially harmful,
        in these cases you may pass an exception. Literally
        just ignore it, as though it didn't happen.t
    try:
        x=int('abc')
    except ValueError:
        pass #Ignore the error


#Demo for Catching more than one Exception:
try:
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    print(x/y)
except (ZeroDivisionError, TypeError, ValueError):
    print("Those numbers were trash...")
'''
'''
#Demo for catching the object
try:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    print(x/y)
except (ZeroDivisionError, TypeError, ValueError) as e:
    print("You've entered an invalid number")
    print(f"Error:  {e}")
#This is called catching the object, because Exceptions are objects
# of the class exception, by catching them as an object, we can 
# interact with them as an object

#another demo for the above
try: #open try block
    from datetime import datetime #import datetime
    date=datetime.strptime(input("Input your date with the format DD-MM-YY:  "), "%d-%m-%y") #accept input into datetime.strptime(), instantiate as date
    print(f"Your flight is booked for: {datetime.strftime(date, "%d-%m-%Y")}")
except ValueError as e:
    print(f"Illegal date:{e}")
    
    
To Catch ALL exceptions without specifying them, we can just except, or except Exception as e

try:
    stuf
except:
    print("Oopsie Poopsie")
    
    
or

try:
    stuff
except Exception as e:
    print(f"oopsie, we had an ewwow: {e}")
    
    
    
else:
    Using an else statement at the end of a try/except block allows for an action to occur only if there are no exceptions
    
Finally:
    A finally statement will always be run at the end of a Try/Except block
    
    
    
    
#This example is actually malformed, it exists to demonstrate only.


try:
    file=open("example.txt", "r")
    data = file.read()
except FileNotFoundError:
    print('File not found')
finally:
    print("closing file")
    file.close()
    


'''
try:
    a = int( input( "Enter a whole: "))
    result = 10/a
    print( f'10 divided by your number is {result}')
except ZeroDivisionError:
    print("Calling the math police on your ass bub, that's disgusting")
except ValueError:
    print("Have you considered following simple instructions?")
finally:
    print("cleaning up your mess")
    del a, result 




