from classes import *
from functions import *
import threading
# Going to create a high-school simulator
# Classes will include: Student, Teacher, Courses in classes.py file
# Functions will include: Register (for school), IN PROGRESS!!

# Test instances

"""BRANDON = Student("Dzrk")
mrMercado = Teacher("Mr. Mercado")
testClass = Course("Computer Science", True, False)

print(BRANDON)
print(mrMercado)
print(testClass)
print()

print(testClass.addTo(BRANDON))
print()
print(BRANDON.schedule)
print(BRANDON.reportCard)"""


# Start of program execution

if __name__ == "__main__":

    options = {

        "R" : "Show Report Card",
        "S" : "Show Schedule",
        "A" : "Add Class",
        "D" : "Drop Class"

    }

    actions = {

        "G" : "Go To Class",
        "Sk" : "Skip Class"

    }

    class_list = [
        
        "Math 1: Algebra", 
        "Science: Living Earth Sciences",
        "History: World History",
        "English 1: Reading and Writing Composition"
        
    ]

    introduction()
    stuName = input("Please enter your first and last name: ")
    clear_terminal()
    student = create_student(stuName)

    clear_terminal()
    register_classes(student, class_list)

    print(student.schedule)
    print(student.reportCard)

    # Before sending the student to his first class, we need to get him 
    # registered into classes
    # IMPLEMENT ADDING CLASSES TO THE STUDENT'S SCHEDULE!!!!!!!!!!!

    # Creating a countdown for student's first class bell
    countdown_thread = threading.Thread(target=first_class_countdown)
    countdown_thread.start()

    while True:
        if not countdown_thread.is_alive():
            input()
            printOptions(actions)
            break
