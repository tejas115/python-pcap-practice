# complete the code, so that the class variables are replaced with instance variables.
# Note: Use the super constructor in the subclass.


class Super:
    # Add your code here
    def __init__(self):
        self.supVar = 11


class Sub(Super):
    # Add your code here
    # subVar = 12
    def __init__(self):
        super().__init__()
        self.subVar = 12


obj = Sub()

print(obj.subVar)
print(obj.supVar)
