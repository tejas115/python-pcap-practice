class A:
    def show(self):
        print(" in A show")

# method overriding.
class B(A):
    def show(self):
        print(" in B show")

class C(A):
    pass

a1 = A()
a1.show()  # Output:  in A show

b1 = B()
b1.show()  # Output:  in B show (override in B)

c1 = C()
c1.show()  # Output:  in A show (inherited from A, since C does not override show)
