class Person:
    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print(f"Hello world! My name is {self.name}.")

#instantiate a person
person_one = Person()
person_two = Person()

#set the persons name
person_one.set_name("Luke Skywalker")
person_two.set_name("Anakin Skywalker")

#display names
print(person_one.name)
print(person_two.name)

#get methods
print(person_one.get_name())
print(person_two.get_name())

#Greet
person_one.greet()
person_two.greet()
