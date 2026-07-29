

""" OOPS (Object-Oriented Programming System) is a programming paradigm that uses objects and classes to structure code.
    It allows for the creation of reusable and modular code by encapsulating data and behavior into objects. 
"""

""" Class --> A class is a blueprint for creating objects. 
    It defines a set of attributes and methods that the created objects will have. 
    In Python, classes are defined using the `class` keyword.

    Object --> An object is an instance of a class.
"""

class Car:
    """ A class representing a car. """

    def __init__(self, make, model, year):
        """ Initialize the car with make, model, and year. """
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        """ Start the car's engine. """
        return f"The {self.year} {self.make} {self.model}'s engine has started."

    def stop_engine(self):
        """ Stop the car's engine. """
        return f"The {self.year} {self.make} {self.model}'s engine has stopped."