print("List is a collection which is ordered and changeable. Allows duplicate members.")
print("The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.")

list1 = ["Apple", "Banana", "Cherry"]
list2 = [10,9,8,7,6,5,4,3,2,1,0]
list3 = [True,False]
list4 = ["abc", 34, True, 40, "Male", False]

# From Python's perspective, lists are defined as objects with the data type 'list':

#The list() Constructor
thisList = list(("Apple","Banana", "Cherry", "Apple"))
print(thisList)

print(" ")
print("Access List items: ")
print(list1[0])

print(" ")
print("Negative Indexing: -1 refers to the last item, -2 refers to the second last item.")
print(list1[-1])

print(" ")
print("Range of index")
print(list2[2:5])


print(" ")
print("Change item value")
print(list1)
list1[0] ="blackCurrent"
print(list1)


print(" ")
print("Insert items in specified index")
print(list1)
list1.insert(0, "watermelon")
print(list1)

print(" ")
print("Add items")
print(list1)
list1.append("Orange")
print(list1)

print(" ")
print("To append elements from another list to the current list, use the extend() method.")
list1.extend(list2)
print(list1)

print(" ")
print("Remove Specified item ")
print(list1)
list1.remove("Orange")
print(list1)

print(" ")
print("Remove Specified index")
print(list1)
list1.pop(0)
print(list1)

print(" ")
print("Loop Through a List3")
for x in list3:
    print(x)


print(" ")
print("Loop Through a List3: Range:len()")
for x in range(len(list3)):
    print("index:", x, list3[x])


print(" ")
print("While Through a List3: using len()")
x=0
while x < len(list3):
    print("index:", x, list3[x])
    x = x + 1

print(" ")
print("Looping Using List Comprehension")
[print (x) for x in list4]


print(" ")
print("List objects have a sort() method that will sort the list alphanumerically, ascending, by default:")
print(list2)
list2.sort()
print(list2)


print(" ")
print("Copy a List two method: list(), copy()")
mylist4 = list4.copy()
print(mylist4)






