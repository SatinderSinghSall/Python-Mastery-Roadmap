# Object-Oriented Programming: OOP

# Classes and Object:
# Class is a blueprint of an Object.
# An Object is an instance of a class.

# Class:
class Student:
    def __init__ (self, name, subject, university, year_of_admission):
        self.name = name
        self.subject = subject
        self.university = university
        self.year_of_admission = year_of_admission
        print("Constructor called")

    subject = "Python Programming"
    university = "University"
    year_of_admission = "2020"

# Object:
student = Student("Satinder Singh Sall", "Java Programming", "REVA University", "2020")
print(student)
print(student.name)
print(student)
print(student.name)
print(student.subject)
print(student.university)
print(student.year_of_admission)
print()
print(student.subject)
print(student.university)
print(student.year_of_admission)

print()
print()

student2 = Student("Soni Vaibhav Kumar", "C++ Programming", "REVA University", "2020")
print(student2)
print(student2.name)
print(student2.subject)
print(student2.university)
print(student2.year_of_admission)
print()
print(student2.subject)
print(student2.university)
print(student2.year_of_admission)

print()
print()

print(student.subject, student.university, student.year_of_admission)
print(student2.subject, student2.university, student2.year_of_admission)

# Attributes & Methods: OOP
# Constructor: init() method (to initialize the objects)
