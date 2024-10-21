class Car:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def __str__(self):
        str1=f"The car brand is : {self.brand} and the speed is : {self.speed}km/h"
        return str1
car1=Car("Toyota",150)
print(car1)