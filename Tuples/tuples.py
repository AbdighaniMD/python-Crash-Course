print("Tuple is a collection which is ordered and unchangeable. Allows duplicate members.")

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#From Python's perspective, tuples are defined as objects with the data type 'tuple':
thistuple = tuple(("abc", 34, True, 40, "male"))
print(thistuple)

print(" ")
print("Access Tuple Items")
print(thistuple[0])

print(" ")
print("Negative indexing")
print(thistuple[-1])

print(" ")
print("Range of indexes")
print(thistuple[1:4])

print(" ")
print("Check if Item Exists")
if 40 in thistuple:
  print("Yes, 40 is in the Tuple")


print(" ")
print("Tuples are unchangeable, or immutable as it also is called.")
print("You can convert the tuple into a list, change the list, and convert the list back into a tuple.")
changeToList = list(thistuple)
changeToList[0] = "kiwi"
backToTuple = tuple(changeToList)
#print(thistuple)
print(backToTuple)


print("1 ")
print("Tuples is immutable.")
print("You can convert the tuple into a list, change the list, and convert the list back into a tuple. to add item into the tuple")
changeToList = list(thistuple)
changeToList.append("Orange")
backToTuple = tuple(changeToList)
#print(thistuple)
print(backToTuple)

print("2 ")
print("Tuples is immutable.")
print("Add tuple to a tuple")
y = ("Banana ",)
thistuple += y
print(thistuple)

print(" ")
print("Remove Items ")
print("it unChangeable: You cannot remove items in a tuple.")
changeToList = list(thistuple)
changeToList.remove("abc")
thistuple = tuple(changeToList)
print(thistuple)

print("2 ")
print("Remove Items ")
print("it unChangeable: You cannot remove items in a tuple.")
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists

print(" ")
print("Loop Through a Tuple")
for x in tuple1:
  print(x)


print(" ")
print("Loop Through a Tuple")
print("Use the range() and len() functions to create a suitable iterable.")
for x in range(len(tuple1)):
  print("index: ", x, tuple1[x])


print(" ")
print("Join Tuples")
print("To join two or more tuples you can use the + operator:")
print(tuple2+tuple3)