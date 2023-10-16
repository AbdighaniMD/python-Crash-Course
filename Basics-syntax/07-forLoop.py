print("Python has two primitive loop commands: While loops, For loops")

#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

for i in range(1, 4):
    print(i)


print(" ")


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print(" ")

#Looping Through a String
for x in "banana":
  print(x)


print(" ")

for x in range(6):
  print(x)
else:
  print("Finally finished!")


print(" ")

#Nested Loops

colour = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in colour:
  for y in fruits:
    print(x, y)


#The pass Statement
for x in [0, 6, 2]:
  pass