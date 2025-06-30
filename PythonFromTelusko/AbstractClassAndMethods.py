# Abstract Classes and Methods Tutorial with Example
# Autor: Serhad Hamamci
from abc import ABC, abstractmethod

# Abstract base class
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass  # subclasses must override this method

# Concrete class that implements the abstract method
class Laptop(Computer):
    def process(self):
        print("Laptop is processing...")

# Another class NOT inheriting from Computer
class WhiteBoard:
    def write(self):
        print("Writing on the whiteboard...")

# Class that works with any object having a 'process' method
class Programmer:
    def work(self, comp):
        print("Programmer starts solving bugs...")
        comp.process()  # expects the object to implement 'process'

# Instantiate Laptop (allowed)
com = Laptop()
com.process()  # Output: Laptop is processing...

# Instantiate WhiteBoard (not a Computer, just for contrast)
whiteboard = WhiteBoard()
whiteboard.write()  # Output: Writing on the whiteboard...

# Let a Programmer use the Laptop
prog = Programmer()
prog.work(com)  # Output: Programmer starts solving bugs... Laptop is processing...

# The following line would cause an error if uncommented:
# prog.work(whiteboard)  # AttributeError: 'WhiteBoard' object has no attribute 'process'