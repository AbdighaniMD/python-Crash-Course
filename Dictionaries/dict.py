print("Dictionary is a collection which is ordered** and changeable. No duplicate members.")


dict1 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

thisdict = dict(name = "Abdighani", age = 24, country = "UK")
print(thisdict)


print(" ")
print("Access Dictionary Items")
print("access the items of a dictionary by referring to its key name, inside square brackets:")
print(dict1["brand"])
print("method called get() that will give you the same result:")
print(dict1.get("colors"))
print("The keys() method will return a list of all the keys in the dictionary.")
print(dict1.keys())
print("The values() method will return a list of all the values in the dictionary.")
print(dict1.values())
print("The items() method will return each item in a dictionary, as tuples in a list.")
print(dict1.items())

print(" ")
print("Change VAlue")
print("You can change the value of a specific item by referring to its key name:")
dict1["year"] = 2018
print(dict1["year"])
print("The update() method will update the dictionary with the items from the given argument.")
dict1.update({"year":2020})
print(dict1["year"])

print(" ")
print("Add Dictionary Items")
print("Adding an item to the dictionary is done by using a new index key and assigning a value to it:")
print("before", dict1)
dict1["Model"] = "Mustang"
print("after", dict1)

print(" ")
print("Removing Items")
print("There are several methods to remove items from a dictionary:")
print("before", dict1)
dict1.pop("Model")
print("after", dict1)

print(" ")
print("Loop Dictionaries")
for x in dict1:
    print(x,":",dict1[x])

print(" ")
print("Copy Dictionaries")
print("one way is to use the built-in Dictionary method copy(), dict()")
mydict = dict1.copy()
print(mydict)
