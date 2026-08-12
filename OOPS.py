

""" OOPS (Object-Oriented Programming System) is a programming paradigm that uses objects and classes to structure code.
    It allows for the creation of reusable and modular code by encapsulating data and behavior into objects. 
"""

""" Class --> A class is a blueprint for creating objects. 
    It defines a set of attributes and methods that the created objects will have. 
    In Python, classes are defined using the `class` keyword.

    Object --> An object is an instance of a class.
"""



# Basic example of a class and object 

# class Car: # Defining a class named Car
#     name = "Car"  
#     color = "Red"

# c1 = Car() # Creating an object of the class Car
# print(c1.name) 
# print(c1.color)




# using self keyword in class

# self is represent the object itself that is calling the method. It is used to access the attributes and methods of the class in python.

# class Student:
#     def StudentDetails(self):
#         print("This is a student class")

# s1 = Student()
# s1.StudentDetails()

        





# class Car:
#     def model(self, name, color): # passing Parameters
#         print(name, color)

# c1 = Car()
# c1.model("Toyota", "Blue") # passing arguments






# Constructor method in class

# class Car:
#     def __init__(self, name, color): # constructor method
#         print(name, color)
    
# c1 = Car("Toyota", "Blue")



# Encapsulation 

# Means protecting data inside the class
# allows access to the data only through methods of the class, not directly from outside the class.
# data safe, controlled, secure, and private

# class Car:
#     def __init__(self, name, color):
#         self.__name = name  # private attribute
#         self.__color = color  # private attribute

#     def get_details(self):  # public method to access private attributes
#         print(f"Car Name: {self.__name}, Color: {self.__color}")

# c1 = Car("Toyota", "Blue")
# # print(c1.get_details())
# # print(c1.__name)
# c1.get_details()


#without encapsulation, we can access the attributes directly, which is not recommended
# print(c1.__name)  # This will raise an AttributeError



# Inheritance

# Inheritance allows a child class to inherit attributes and methods from a parent class.
# It helps in code reuse and reduce duplication code.
# It make the code more organized and easier to maintain.

# class Employee:
#     def work(self):
#         print("Employee is working")
    
# class Developer(Employee):  # Developer class inherits from Employee class
#     def code(self):
#         print("Developer is coding")

# class Tester(Employee):  # Tester class inherits from Employee class
#     def test(self):
#         print("Tester is testing")

# d = Developer()
# d.work()  # Inherited method from Employee class
# d.code()  # Direct method from Developer class

# t = Tester()
# t.work()  # Inherited method from Employee class
# t.test()  # Direct method from Tester class




# Polymorphism

# polymorphism allows different classes to use the same method name, but with different actions.
# When a child class has the same method name, python call the child class first.

# class Employee:
#     def work(self):
#         print("Employee is working")

# class Developer(Employee):
#     def excute(self):
#         super().work()  # calling the parent class method


#     def work(self):
#         print("Developer is coding")

# class Tester(Employee):
#     def work(self):
#         print("Tester is testing")

# d = Developer()
# d.excute()  
# d.work()




# Abstraction
# Abstraction is the process of hiding the internal details and showing only the functionality to the user.

# from abc import ABC, abstractmethod

# class Employee(ABC):
#     @abstractmethod
#     def work(self):
#         pass
    
# class Developer(Employee):
#     def work(self):
#         print("Developer is coding")

# class Tester(Employee):
#     def work(self):
#         print("Tester is testing")

# d = Developer()
# d.work()

# t = Tester()
# t.work()