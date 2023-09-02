from classes import *
from functions import *
# Going to create a high-school simulator
# Classes will include: Student, Teacher, Courses in classes.py file
# Functions will include: Register (for school), IN PROGRESS!!

# Test instances

BRANDON = Student("Dzrk")
mrMercado = Teacher("Mr. Mercado")
testClass = Course("Computer Science", True, False)

introduction()

stuName = input("Please enter your first and last name: ")

create_student(stuName)

"""print(BRANDON)
print(mrMercado)
print(testClass)
print()

print(testClass.addTo(BRANDON))
print()
print(BRANDON.schedule)
print(BRANDON.reportCard)"""