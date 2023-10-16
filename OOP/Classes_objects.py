print("A Class is like an object constructor, or a 'blueprint' for creating objects.")

class MyBasicFixedClass:
  name = "abdighaniMD"
  age = 24


#Create Basic Object
person1 = MyBasicFixedClass()
print(person1.age)


print(" ")

"""
The __init__() Function
  All classes have a function called __init__(), which is always executed when the class is being initiated.
  Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

Self
The self parameter is a reference to the current instance of the class, 
and is used to access variables that belong to the class.
  
"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

#Method
  def setOccepation(self, value1, value2):
    self.job=value1
    self.salary = value2

  def __str__(self):
    return f"{self.name} ({self.age})"  

class Objects_Class:
  pass

# note: The __init__() function is called automatically every time the class is being used to create a new object.
p1 = Person("Abdighani", 24)
p1.setOccepation("Software Developer", 30000)
p2 = Person("Jenny",34)

print(p1.name, p1.age, p1.job)
print(p2.name, p2.age)