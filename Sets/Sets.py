print("Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.")

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {"a","b","c", 9,  False}

#From Python's perspective, sets are defined as objects with the data type 'set':
myset = set(("apple", True, 2, "cherry", False, 1,))


print(" ")
print("Access Sets Items")
print("You cannot access items in a set by referring to an index or a key. So For-loop")
for x in myset:
    print(x)

print(" ")
print("Add to a set")
print("Once a set is created, you cannot change its items, but you can add new items.")
set1.add("Orange")
print(set1)
print("To add items from another set into the current set, use the update() method.")
set1.update(set3)
print(set1)

print(" ")
print("Remove item in a set")
print("To remove an item in a set, use the POP(), remove(), or the discard() or even Clear() method to remove all.")
set1.remove("Orange")
print(set1)


print(" ")
print("Join two Sets")
print("the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:")
set4 = set2.union(set3)
print(set4)


print("2 ")
print("Join two Sets")
print("The intersection_update() method will keep only the items that are present in both sets.")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)


print("3 ")
print("Join two Sets")
print("The symmetric_difference() method will keep only the items that are present in both sets.")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference(y)
print(x)