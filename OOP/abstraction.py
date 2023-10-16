"""
Hiding the internal implementatins of a process or method from the user

hierarchical classification 
abstract class
"""

from abc import ABC, abstractclassmethod
class Car(ABC):

    def insert(self, x):
        print("Inserted value: ", x)
     #abstract methods
    @abstractclassmethod
    def mileage(self):
        pass


class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 30kmph")   
class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 25kmph ")   
class Duster(Car):   
     def mileage(self):
        print("The mileage is 24kmph ")   
  
class Renault(Car):   
    def mileage(self):
        print("The mileage is 27kmph ") 


# Driver code   
t= Tesla ()   
t.mileage()
#t.insert(3)
    
s = Suzuki()   
s.mileage()

d = Duster()   
d.mileage()

r = Renault()   
r.mileage() 