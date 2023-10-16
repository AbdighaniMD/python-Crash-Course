"""
An iterator is an object that contains a countable number of values.

an iterator is an object which implements the iterator protocol, 
    which consist of the methods __iter__() and __next__().

Lists, tuples, dictionaries, and sets are all iterable objects.
    They are iterable containers which you can get an iterator from.

"""

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))

print(" ")

# also a use of for loop to iterate through an iterable object:
for x in mytuple:
    print(x)


print(" ")

#Create an Iterator 
class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
    
    
myObjectInstance = MyNumber()
myIter = iter(myObjectInstance);

for x in myIter:
    print(x)