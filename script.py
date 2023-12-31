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
        "S" : "Skip Class"

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

    # Saving name of student's classes to separate variable

    first_class = student.schedule[0].split(": ")[1]
    second_class = student.schedule[1].split(": ")[1]
    third_class = student.schedule[2].split(": ")[1]
    fourth_class = student.schedule[3].split(": ")[1]
    
    # Creating a countdown for student's first class bell
    countdown_thread = threading.Thread(target=first_class_countdown)
    countdown_thread.start()

    while True:
        if not countdown_thread.is_alive():
            time.sleep(2)
            printOptions(actions)
            break
    
    print()
    print()

    answer = grab_action(actions)
    clear_terminal()

    # FIX THIS: Grab new action and ask if they want to go to next class
    #           Present option to go to lunch before third class
    #           Ask if they want to hang out with friends after fourth class
    attend_class(student.name, first_class, answer, actions)
    attend_class(student.name, second_class, answer, actions)
    attend_class(student.name, third_class, answer, actions)
    attend_class(student.name, fourth_class, answer, actions)
    # This is where i got lazy and hit a creative roadblock.
    # I temporarily have the student go throughout his day in an instant