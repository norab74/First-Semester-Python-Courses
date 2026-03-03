class Person:
    def __init__(self):
        self.name = "unknown"

    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print(f"Hello world! My name is {self.name}.")

#instantiate a person
person_one = Person()

print(person_one.name)
print(person_one.get_name())
person_one.greet()
