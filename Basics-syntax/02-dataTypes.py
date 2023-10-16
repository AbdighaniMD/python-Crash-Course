print("Built-in Data Types")


# Text Type: String
amString = "Hello, World" #str("Hello, World")
print(amString)


#Numeric Types:	int, float, complex
amInt, amFloat, amComplex = 20, 20.5, 1j
print(amInt, amFloat, amComplex)


#Sequence Types: list, tuple, range
mylist = ["apple", "banana", "cherry"] # index not fixed changeable
mytuple = ("apple", "banana", "cherry") #fixed set of array index, unchangeable
myRange = range(3)


#Mapping Type:	dict
thisdict = {
  "name": "Abdighani",
  "age": 24,
  "Occupation": "Software Engineer"
}


#Set Types:	set, frozenset
myset = {"apple", "banana", "cherry"} #set(("apple", "banana", "cherry"))
myFrozenset = frozenset(("apple", "banana", "cherry"))


#Boolean Type:	bool
myTrue = True #print(10 > 9)
myFalse = False #print(10 == 9)


#Binary Types:	bytes, bytearray, memoryview
myBytes = bytes(5)
myBytearray = bytearray(5)
myMemoryview = memoryview(bytes(5))