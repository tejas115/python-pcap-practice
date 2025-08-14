class Student:

    school = 'ABC High School'


    def __init__(self, name, age, student_id, m1, m2, m3):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    @classmethod
    def display_school(cls):
        print(f"School: {cls.school}")

    @classmethod
    def getSchool(cls):
        return cls.school
    
    @staticmethod
    def info():
        print("This is a student class in abc module.")


# instance methods

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")
        print(f"Student ID: {self.student_id}")

    def calculate_average(self):
        return (self.m1 + self.m2 + self.m3) / 3
    

    def study(self):
        print(f"{self.name} is studying.")

    def take_exam(self):
        print(f"{self.name} is taking an exam.")


# Getter and Setter for m1
    def get_m1(self):
        return self.m1
    
    def set_m1(self, value):
        self.m1 = value

    def get_m2(self):
        return self.m2

    def set_m2(self, value):
        self.m2 = value

    def get_m3(self):
        return self.m3

    def set_m3(self, value):
        self.m3 = value

student1 = Student("Alice", 20, "S123", 85, 90, 88)
student1.display_info()
student1.study()
student1.take_exam()

student2 = Student("Bob", 22, "S456", 78, 82, 80)
student2.display_info()
student2.study()
student2.take_exam()

print(f"Average marks of {student1.name}: {student1.calculate_average()}")
print(f"Average marks of {student2.name}: {student2.calculate_average()}")

Student.info()