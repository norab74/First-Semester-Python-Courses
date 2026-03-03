class FoodExpert:
    def __init__(self):
        self.goodFood = [] #instansiate an internal variable as an empty list
    def addGoodFood(self,food): #add method "addGoodFood"
        self.goodFood.append(food)
    def likes(self,x): #add method "likes"
        return x in self.goodFood #Returns the entire list, as individual values
    def prefers(self,x,y): #add method "prefers"
        x_rating = self.goodFood.index(x) #find indicies of the food items
        y_rating = self.goodFood.index(y)
        if x_rating > y_rating: #compare indicies, return lower indexed item.
            return y
        else:
            return x
        
