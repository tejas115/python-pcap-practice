from abc import ABC, abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("Processing on Laptop")

class Desktop(Computer):
    def process(self):
        print("Processing on Desktop")

class Programmer:
    def work(self, com):
        print("Programmer is working...")
        com.process()

class Whiteboard(Computer):
    def write(self):
        print("Writing on whiteboard")

    def process(self):
        print("Processing on Whiteboard")



# com = Computer()  # This will raise an error because Computer is an abstract class
# com.process()  # This will also raise an error because process is an abstract method

com1 = Laptop()
com1.process()  # Output: Processing on Laptop

com2 = Desktop()
com2.process()  # Output: Processing on Desktop

prog1 = Programmer()
prog1.work(com1)  # Output: Programmer is working...


com3 = Whiteboard()
com3.write()  # Output: Writing on whiteboard
prog1.work(com3)