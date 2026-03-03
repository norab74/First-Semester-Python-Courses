class Person():
    def __init__(self, name, hasRug):
        self.name=name #store name in the object
        self.hasRug=hasRug
    def greet(self):
        print(f"Yo dawg, I'm {self.name}")
    def ruinRug(self):
        if self.hasRug == True:
            print("C'mon man that rug really tied the room together!")
        else:
            print("Fine I'll have them buy you a new rug")

#create two objects matching person:
dude = Person("The Little Lebowski",  True)
bigGuy = Person("The Big Lebowski",  False)
#self               name            hasRug
#These Objects replace 'self' within the class

dude.greet() 
bigGuy.greet()
dude.ruinRug()
bigGuy.ruinRug()