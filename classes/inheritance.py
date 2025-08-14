class A:
    def feature1(self):
        print("Feature 1 of class A")

    def feature2(self):
        print("Feature 2 of class A")

class B:
    def feature3(self):
        print("Feature 3 of class B")

    def feature4(self):
        print("Feature 4 of class B")

class C(A, B):
    def feature5(self):
        print("Feature 5 of class C")

class D(A):
    def feature6(self):
        print("Feature 6 of class D")   

class E(D, C):
    def feature7(self):
        print("Feature 7 of class E")

a1 = A()

a1.feature1()
a1.feature2()

b1 = B()
b1.feature3()
b1.feature4()

c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()

d = D()
d.feature1()
d.feature2()
d.feature6()

e = E()
e.feature1()
e.feature2()
e.feature6()
e.feature5()
e.feature7()
