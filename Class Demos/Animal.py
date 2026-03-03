class car:
    def __init__(self,color, brand):
        self.color="red"
        self.brand="toyota"
car1=car("toyota","red")
car2=car("ford","yellow")
car3=car("honda","green")
print(car1.brand,car1.color)
print(car3.brand,car3.color)
print(car2.brand,car2.color)