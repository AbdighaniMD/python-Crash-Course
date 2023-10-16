"""
Encapsulation binds together the attributes (data) and the methods (functions and procedures) that manipulate the data. It does this so that the data is protected.

Data should never be accessed directly. Instead, 
    getter and setter methods must be provided that will allow access to the attributes:

types of access modifiers:
    PUBLIC:
        Accessible anywhere from the outside the class
    PRIVATE MEMBER:
        Accessible within the class itself
    PROTECTED MEMBER
        Accessible within the class and subclass
"""


class Employee:
    def __init__(self, name, salary, project):
        self.name = name
        self.salary = salary
        self.__project = project #Private member

    #show the employee data
    def show_details(self):
        return f"The name is {self.name}, and Salary is {self.salary}"
    
    #show the employee data
    def work(self):
        return f"{self.name}, is working on, {self.__project}"
    
    def get_project(self):
        return self.__project
    
    def set_project(self, new_project):
        self.__project = new_project
        
#Objects for employee
employee01 = Employee("Marcelo", 100000, "Video Game")

#Access prevate attribute name
#print("the name value is:" , employee01.name)

print(employee01.show_details())
print(employee01.work())
employee01.set_project("Developer")
print(employee01.name + ",", employee01.get_project())