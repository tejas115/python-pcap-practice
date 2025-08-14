a = 5
b = 6
c = '5'
d = "6"
print(a + b)  # Output: 11
print(c + d)  # Output: 56

print(int.__add__(a, b))  # Output: 11

print(str.__add__(c, d))  # Output: 56

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3
    
    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = self.m2 + other.m2
        if r1 > r2:
            return True
        else:
            return False
        
    def __str__(self):
        return self.m1, self.m2
    
    

s1 = Student(10, 20)
s2 = Student(30, 40)

s3 = s1 + s2  # This will raise an error unless __add__ is defined in the Student class

print(s3.m1, s3.m2)  # Output: 40 60

if s1 > s2:  # This will raise an error unless __gt__ is defined in the Student class
    print("s1 wins")
else:
    print( "s2 wins")

a = 9 
print(a.__str__())

print(s1.__str__())  # This will raise an error unless __str__ is defined in the Student class