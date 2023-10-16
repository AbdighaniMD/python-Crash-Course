print("Function-Methods")


#In Python a function is defined using the def keyword:
def my_function():
    print("Hello from a function")

#Calling a Function
my_function()


#Arguments
def my_function_name(fname):
  print("welcome, " + fname)

my_function_name("abdighani");
my_function_name("Emil");

"""
From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.

"""

#Arguments: call with correct number of arguments
def my_function_name(fname, lname):
  print(fname + " " + lname)

my_function_name("Abdighani", "MD")


#Arbitrary Arguments, *args
def my_kidsfunction(*kids):
  print("The youngest child is " + kids[2])
  """
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

  """

my_kidsfunction("Emil", "Tobias", "Linus") # 0, 1, 2


#Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])
"""
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: 
** before the parameter name in the function definition.

"""

my_function(fname = "Abdighani", lname = "MD")


#Return Values
def my_functionReturn(x):
  return 5 * x

print(my_functionReturn(3))


#Recursion
def tri_recursion(k):
  if(k > 0): # 5 + 4+ 3+ 2+1 = 15 First loop 
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result


tri_recursion(5)
"""
1: 5 + 4 + 3 + 2 + 1 = 15 First loop
2: 4 + 3 + 2 + 1 = 10 
3: 3 + 2 + 1 = 6 
4: 2 + 1 = 3
5: 1 = 1
6: 0 
"""