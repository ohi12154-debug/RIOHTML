# Object-Oriented Programming (OOP) - Part 2

# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print("\n----- Person Details -----")
        print("Name :", self.name)
        print("Age  :", self.age)

# Child Class (Inheritance)
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def show_student(self):
        self.show_person()
        print("Grade:", self.grade)

print("===== Student Information System =====")

# Taking input from the user
name = input("Enter Student Name: ")
age = input("Enter Student Age: ")
grade = input("Enter Student Grade: ")

# Creating an object
student1 = Student(name, age, grade)

# Displaying details
student1.show_student()