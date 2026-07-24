# Object-Oriented Programming (OOP) - Part 1

class Student:
    # Constructor
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    # Method to display student details
    def display_details(self):
        print("\n----- Student Details -----")
        print("Name :", self.name)
        print("Age  :", self.age)
        print("Grade:", self.grade)


print("===== Student Information System =====")

# Taking input from the user
name = input("Enter Student Name: ")
age = input("Enter Student Age: ")
grade = input("Enter Student Grade: ")

# Creating an object
student1 = Student(name, age, grade)

# Calling the method
student1.display_details()