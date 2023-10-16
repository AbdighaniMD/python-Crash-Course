"""
The word "polymorphism" means "many forms", 
and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

"""
class Transport:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    

class Car(Transport):
  def move(self):
    print("Drive!")

class Boat(Transport):
  def move(self):
    print("Sail!")

class Plane(Transport):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()