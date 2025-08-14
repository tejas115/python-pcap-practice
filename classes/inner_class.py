# Inner class

class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.laptop = self.Laptop("Dell", "XPS 13")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        self.laptop.display_info()

    def study(self):
        print(f"{self.name} is studying.")

    def take_exam(self):
        print(f"{self.name} is taking an exam.")

    class Laptop:
        def __init__(self, brand, model):
            self.brand = brand
            self.model = model

        def display_info(self):
            print(f"Laptop Brand: {self.brand}")
            print(f"Laptop Model: {self.model}")



s1 = Student('Navin', 20, 'S001')
s2 = Student('John', 22, 'S002')

s1.display_info()
s2.display_info()   


# create object of Laptop (inner class) inside the outer class 
lap1 = s1.laptop
lap2 = s2.laptop



print(lap1.display_info())
print(lap2.display_info())

# create object of inner class outside the outer class provided you use the outer class name to call it.

lap3 = Student.Laptop("Lenovo", "ThinkPad X1")
print(lap3.display_info())


print(id(lap1))
print(id(lap2))
print(id(lap3))