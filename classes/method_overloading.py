class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def info(self):
        print(f"mark1: {self.m1}, mark2: {self.m2}")

    def sum(self, a=None, b=None, c=None):
        s = 0
        if a is not None:
            s += a
        if b is not None:
            s += b
        if c is not None:
            s += c
        return s


s1 = Student(59.0, 68.0)
print(s1.sum(5, 6))