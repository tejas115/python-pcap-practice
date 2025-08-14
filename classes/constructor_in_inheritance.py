# How constructor behaves in Inheritance
# How to user super () in inheritance
# method resolution order

class A:
    def __init__(self):
        print("Constructor of class A")

    def feature1(self):
        print("Feature 1 of class A")

    def feature2(self):
        print("Feature 2 of class A")

class B:
    def __init__(self):
        print("Constructor of class B")

    def feature1(self):
        print("Feature 1 of class B")

    def feature4(self):
        print("Feature 4 of class B")

class C(A, B):
    def __init__(self):
        super().__init__() # How to use super() in multiple inheritance
        print("Constructor of class C")

    def feature2(self):
        print("Feature 2 of class C")


# Object Instantiation
# Method resolution order goes left to right.
a1 = A()
b1 = B()
c1 = C()    
c1.feature1()
c1.feature4()