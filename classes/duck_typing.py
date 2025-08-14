# "Duck typing" = Another way to achieve polymorphism in Python besides Inheritance.
# Object must have the minimum necessary attributes/methods.
# "if it looks like a duck and quacks like a duck, it's a duck"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Car: # minimum attributes/methods, you can treat it like a different object, even though car is not an animal.
    alive = False
#    def horn(self):
    def speak(self):
        print("Honk!")


animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)  # Accessing inherited attribute from Animal class
