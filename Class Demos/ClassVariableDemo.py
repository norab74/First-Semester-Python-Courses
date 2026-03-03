
class MyClass: #Remember, classes ar traditionally done with Capital letters
    var1 = "Initialized in a class, that makes me a class variable"
    var2 = "Also in a class"
    def get_var1(self):
        return self.var1
    def get_var2(self):
        return self.var2
    
obj = MyClass()
print(obj.get_var1())
print(obj.get_var2())
    #When calling these methods, rem