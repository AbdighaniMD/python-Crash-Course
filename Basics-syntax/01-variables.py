"""
Python syntax can be executed by writing directly in the Command Line
Or by creating a python file on the server, using the .py file extension, and running it in the Command Line

"""

#This is a Hello comment
print("Hello, World!")


# Variables
name = "Abdighani-MD"
age = 24
print(name, age)

#String Concatenation
j = "Hello"
k = "World"
l = j + " " + k
print(l)

# Many Values to multiple Variables
a, b, c = "i like", " to eat", "Orange"
print(a,b,c)

#One Value to Multiple Variables
x = y = z = "Hello, Abdighani"
print(x,y,z)

#Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Global Variables
amGlobalVariable = "awesome"
def myfunc():
  print("Python is " + amGlobalVariable)
myfunc()