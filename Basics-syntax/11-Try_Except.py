
"""
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.

"""

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


#Raise an exception
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")


#User Input
username = input("Enter username:")
print("Username is: " + username)


#String Formatting
price = 49
txt = "The price is {} dollars"
print(txt.format(price))