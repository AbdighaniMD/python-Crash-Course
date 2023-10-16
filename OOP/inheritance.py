#Inheritance allows us to define a class that inherits all the methods and properties from another class.

class Person: # Parent Class
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def testing(self):
        print("testing parten class")

    def __str__(self):
        return f"Person: {self.firstname} {self.lastname}"  

#Use the Person class to create an object, and then execute the printname method:
x = Person("Abdighan", "MD")
print(x)
#x.testing()


class Student1(Person): #Basic Child Class
  pass
#Use the Student class to create an object, and then execute the printname method:
x = Student1("Osman", "MD")
print(x)
#x.testing()



"""
By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

"""
class Student(Person): #Child Class
    #The __init__() function is called automatically every time the class is being used to create a new object.
    def __init__(self, fname, lname, Course, graduationyear ):
        super().__init__(fname, lname)
        self.Course = Course
        self.graduationyear = graduationyear

    def __str__(self):
        return f"Student: {self.firstname} {self.lastname} {self.Course} {self.graduationyear}"
    
x = Student("Abdighani", "MD", "Computer Sciece", 2024)
print(x)
#x.testing()
