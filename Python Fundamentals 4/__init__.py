# Object-Oriented Programming: OOP

# Classes and Object:
# Class is a blueprint of an Object.
# An Object is an instance of a class.

# Class:
class Student:
    def __init__ (self, name, subject, university, year_of_admission, cgpa):
        self.name = name
        self.subject = subject
        self.university = university
        self.year_of_admission = year_of_admission
        self.cgpa = cgpa
        print("Constructor called")

    def get_cgpa(self):
        return self.cgpa

    subject = "Python Programming"
    university = "University"
    year_of_admission = "2020"

# Object:
student = Student("Satinder Singh Sall", "Java Programming", "REVA University", "2020", 8)
print(student)
print(student.name)
print(student)
print(student.name)
print(student.subject)
print(student.university)
print(student.year_of_admission)
print(student.cgpa)
print()
print(student.subject)
print(student.university)
print(student.year_of_admission)

print()
print()

student2 = Student("Soni Vaibhav Kumar", "C++ Programming", "REVA University", "2020", 9)
print(student2)
print(student2.name)
print(student2.subject)
print(student2.university)
print(student2.year_of_admission)
print()
print(student2.subject)
print(student2.university)
print(student2.year_of_admission)
print(student2.cgpa)

print()
print()

print(student.subject, student.university, student.year_of_admission)
print(student2.subject, student2.university, student2.year_of_admission)

print()
print()

print(student.cgpa)
print(student2.cgpa)

print()
print()

print(f"Student Information: {student.name}, {student.year_of_admission}, {student.cgpa}, {student.subject}, {student.university}")
print(f"Student Information: {student2.name}, {student2.year_of_admission}, {student2.cgpa}, {student2.subject}, {student2.university}")

print()
print()

# Attributes & Methods: OOP
# Constructor: init() method (to initialize the objects)
# Types of Constructors

# Attributes: Class & Instance
class StudentClass:
    university_name = "University" # Class Attributes
    PI = 3.1

    def __init__(self, name, cgpa):
        self.name = name # Instance Attributes
        self.cgpa = cgpa
        self.PI = 3.14
        print("Constructor called")

std = StudentClass("Satinder Singh Sall", 8)
print(std)
print(std.name)
print(std.cgpa)
print(std.PI)
print(StudentClass.PI)
