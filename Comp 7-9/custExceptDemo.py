#Divider, but Two is illegal

class BanTwo(Exception):
    def __init__(self, message):
        super().__init__(message)
        
        
def divider(numer, denom): 
#    numer = input ("Gimme A number:  ")
#    denom = input ("Keep it coming, one more:  ")
    if numer == 2 or denom == 2:
        raise BanTwo(message = "Two is illegal")
    try:
        return numer / denom
    except ZeroDivisionError:
        print("Please don't divide by zero")
    except ValueError:
        print("You must enter a number")          
numer = int( input ("Gimme A number:  "))
denom = int( input ("Keep it coming, one more:  "))
print(divider(numer,denom))