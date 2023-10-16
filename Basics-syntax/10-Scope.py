print("A variable is only available from inside the region it is created. This is called scope.")


"""
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
"""
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()



#Global Scope
#A variable created in the main body of the Python code is a global variable and belongs to the global scope.
x = 300
def myfunc():
  print(x)

myfunc()

print(x)


"""
Naming Variables
If you operate with the same variable name inside and outside of a function, 
Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):

""" 

x = 300
def myfunc():
  x = 200
  print(x)

myfunc()

print(x)



#Global Keyword: makes the variable global.
def myfunc():
  global x
  x = 300
  return x

print(myfunc())

print(x)