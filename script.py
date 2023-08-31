from classes import *

# Going to create a high-school simulator
# Classes will include: Student, Teacher, Courses in classes.py file

# Test instances

BRANDON = Student("Dzrk")
mrMercado = Teacher("Mr. Mercado")
testClass = Course("Computer Science", True, False)

print()
print(BRANDON)
print(mrMercado)
print(testClass)
print()

print(testClass.addTo(BRANDON))
print()
print(BRANDON.schedule)
print(BRANDON.reportCard)