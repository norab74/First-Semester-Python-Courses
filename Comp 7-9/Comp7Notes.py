'''
Structural Programming
    Allows us to create and name computer memory locations that can hold values (variables)
        Write a series of steps or operations to manipulate 
    Identifier - one word name used to reference a variable
    Procedures/Methods (Functions) 
        Logical units that group individual operations used in a computer program.
        Gets "Called" or "Invoked" by other procedures or methods.

Object Oriented Programming
    An extension of procedural programming, the thing we've been doing.
    Objects: 
        Similar to concrete objects in the real world, they contain their own attributes and actions (variables and methods)
        Attributes - 
            Represent characteristics (data or variables) of an object
        State of an object - 
            The collective value of all its attributes at any point in time
        Behaviors of an object -
            The stuff an object can do
    Classes - 
        
        A catergory of objects, or a type of object
        The class definition is your Blueprint for your objects
        Describes the methods of every object in an instance of that class
            Instance here refers to the same as it does in gaming or webhosting, it is simply a running copy of the code with reserved memory.
        An object, defined above, is an instance of a class.


        Class                            Object
            Animal                      Dog, Cat, Squirrel


        Animals can have Legs, fur, colors, a noise they make.
        Each instance of the class 'Animal' has different Legs, fur, colors, or noises.
            Some of these things may be the same, or different accross different animals, but the class animal doesn't care
            that some things within it are different.

    OOP allows us to break our problem down into smaller, easier to handle units
    Control access via encapsulation to reduce accidental changes
    Simplyfy management of large projects with multiple programmers
    Simplify re-use of code
        _____________________________________________________________________________________________________________________
Don't Repeat Yourself - DRY
    Implementing classes allows us to have a healthy level of laziness by allowing for extremely abstract code with less limitations.



Encapsulation
    Technique of packaging an object's attributes and methods into a cohesive unit; an unidivided entity
    This helps us to make a "Black Box" of sorts, that keeps things away from the user and allows for more user friendly code.


~~~~~~~~~~~~~~~~~~~~~~
Example:
    A structured Top-Down approach has us list the steps the user will take to use our application
    Once each step the user should take is identified, we determine what routines need to occur for the desired output
    Focusing on a time-line style fashion helps to organize our code:

    In order to design an ATM program with classes we ask "Who's job is this"
        Who inserts the card? 
        Who reads the card? 
        Who verifies the Acct and Pin
        Who dispenses the cash?
        Who keeps track of the balance ?

   

Procedural programming -    Do something to data
OOP -                       Ask object to do something
Attributes -                What an object has
Methods(defined as func) -  What an object is allowed to do

    
Below: 
    the classs "Person" describes the blueprint for what a person can do
    They can set their name, they can know their name, they can greet you and introduce themself.

    The set function makes their name real, assigning a value to self.name
    The get function allows the object to know it's name, returning it one level of encapsulation up


Defining a Class

class Person:
    def setName(self, name): #Create a set method, to allow us to set the Attribute "name"
        self.name = name #assign name to the Attribute self.name
    def getName(self): #create a get method to allow us to retrieve the Attribure "name"
        return self.name
    def greet(self):
        print("Hello, I'm %s." %self.name)




Get and Set methods



How to instantiate an object from a class



How to call class methods from an object




Explain what a parameter is




Demonstrate how to write an __init__ method

class Fruit:
    def __init__(self):
        self.name = "Apple"
        self.color = "Red"
#Create an object, by instantiating class Fruit as object treeFruit
treeFruit = Fruit()
#Accessing Attributes as defined in __init__
    #Since these will apply to all objects who've not assigned their own values to these attributes
    #this should be considered only an initialization
print("My name is",treeFruit.name)
print("My color is",treeFruit.color)
#set the attributes of object treeFruit
treeFruit.color = "Green"
treeFruit.name =  "Kiwi Fruit"
print("My name is",treeFruit.name)
print("My color is",treeFruit.color)


Demonstrate how to write class methods
    Every method must have the parameter "self", 'self' allows us to create self-referential code.
    Allows us to access the attribute from other methods
    '''
'''
class Person:
    def __init__(self,name,job,timePeriod):
        self.name=name
        self.job=job
        self.timePeriod=timePeriod
    def setName(self, name): #Create a set method, to allow us to set the Attribute "name"
        self.name = name #assign name to the Attribute self.name
    def getName(self): #create a get method to allow us to retrieve the Attribure "name"
        return self.name
    def setJob(self, job): #Create a set method, to allow us to set the Attribute "job"
        self.job = job #assign name to the Attribute self.job
    def getJob(self): #create a get method to allow us to retrieve the Attribure "job"
        return self.job
    def setTimePeriod(self, timePeriod):
        self.timePeriod = timePeriod #assign name to the Attribute self.timePeriod
    def getTimePeridod(self): #create a get method to allow us to retrieve the Attribure "timePeriod"
        return self.timePeriod

    def greet(self): 
        print(f"Hello, I'm {self.name}, a {self.job} in the {self.timePeriod}")

jedi = Person("Anakin","General","Clone Wars") #Instantiate Person as jedi, with Name:Anakin and Job:General
jedi.greet() #Greet

janitor = Person("Craig", "Custodian", "Civil War")
janitor.greet()
'''
#Group Exercise
'''
class PizzaOrder:
    def __init__(self,diameter,toppings):
        self.diameter = diameter
        self.toppings = toppings

    #setters first
    def setPizzaSize(self, diameter):
        self.diameter = diameter
    def SetPizzaToppings(self, toppings):
        self.toppings = toppings
    
    #getters now
    def getPizzaSize(self):
        return self.diameter
    def getPizzaToppings(self):
        return self.toppings
    

    #Generate base price of pizza based on diameter
    def Price(self):
        if self.diameter <= 8:
            basePrice = 8
        elif self.diameter >= 8 and self.diameter <= 10:
            basePrice = 10
        elif self.diameter > 10:
            basePrice = 12
        toppingsPrice = 1 * len(self.toppings)
        return self.basePrice + toppingsPrice


    

Demonstrate how to initialize variables in a class
 See above, 



Day 2: Class Methods




    Overview:
        Self Parameter - For self referential code snippets, for class methods where the method must reference an instance of the class.
			Distinguishes methods from functions.
            The Self parameter should always be the first parameter given to any method
            The Self parameter is a special parameter which allows for the object which the class is instantiated as to be passed into the class
				without necessarily knowing the name of said object.
			Self doesn't necessarily need to be called "self", any variable will do, but "self" is traditional and leads to easier to read code.


        Methods - Like a function, but within a class. Similar to a library method/function, but defined by the programmer.

        Initializing Variables - an "__init__" magic function must be created to initialize any variables within the class to ensure they
            exist in the required memory space. Global variables should not be accessed inside classes outside of the __init__ function, they
            instead should be shadowed
        
        Object Oriented Design - Rather than focusing on manipulating data, Object Oriented Design encourages us to analyze the desired workflow
            of the application at hand, and code to match that workflow.
        




    __init__() method     
		Use to initalize the class, and all of it's variables
        
	refer to 'Class Demos/'
    
    

    Class Variables
		A variable assigned within a class is called a class variable
	Instance Variables
		created in __init__, unique to each instance of a class.
		When an Instance Variable is written over a global or 
        class variable, it is called 
    
    
'''