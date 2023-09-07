from classes import *
import os

import time
# After 30 seconds of the program executing, a message will appear notifying
# the student that their first class is starting. Need threading and time modules

def first_class_countdown():
    for num in range(3, 0, -1):
        print("...")
        time.sleep(1)
    clear_terminal()
    
    print("\nRing! Ring! Ring! Your first class is starting soon!")


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def introduction():
    print()
    print()
    print("                   ________________          ")
    print("         _________/                \_________")
    print("        /       J. ROBERT OPPENHEIMER        \ ")
    print("       /             HIGH SCHOOL              \ ")
    print("       |______________________________________|")
    print("       |          |      ____      |          |")
    print("       |          |     |    |     |          |")
    print("       |          |     |   -|     |          |")
    print("       |__________|_____|____|_____|__________|")
    print()
    print()
    print("Welcome to J.R.O. high school. Let's get you registered")
    input()

def create_student(name, year = 1):
    
    newStuObj = Student(name, year)
    print()
    print(newStuObj)
    print("\nClick enter to continue...")
    input()

    return newStuObj


def printOptions(options):

    
    print("=====================================\n")

    print("What would you like to do next?\n")

    for action in options:
        print(f"{action} - {options[action]}")   

    print("\n===================================")


def print_classes(class_list):

    for item in class_list:
        
        print(f" - {item.upper()}\n")


def print_class_helper(class_list):

    for item in class_list:

        print(f" + {item.split(':')[0]}\n")
    print(f" + ALL\n")


def register_classes(student, class_list):
    print("It's time to register you for classes. Let's take a look at your options:\n")

    print_classes(class_list)
    input()

    clear_terminal()
    print("Which class would you like to add to your schedule? (The district recommends you choose all!)\n")
    print_class_helper(class_list)
    
    to_add = input("Type here: ")

    match to_add.upper():
        case "MATH 1":
            print("\nYou chose Math 1")
            student.schedule.append(class_list[0])
            student.reportCard[class_list[0].split(':')[1]] = "N/A"

        case "SCIENCE":
            print("\nYou chose Science")
            student.schedule.append(class_list[1])
            student.reportCard[class_list[1].split(':')[1]] = "N/A"

        case "HISTORY":
            print("\nYou chose History")
            student.schedule.append(class_list[2])
            student.reportCard[class_list[2].split(':')[1]] = "N/A"

        case "ENGLISH 1":
            print("\nYou chose English 1")
            student.schedule.append(class_list[3])
            student.reportCard[class_list[3].split(':')[1]] = "N/A"

        case "ALL":
            print("\nYou chose All")

            for class_name in class_list:
                student.schedule.append(class_name)
                student.reportCard[class_name.split(':')[1]] = "N/A"


        case _:
            print("Invalid selection. Click enter to try again...")
            input()
            clear_terminal()
            register_classes(student, class_list)

    if len(student.schedule) < 4:
        print("You're a couple of classes short. To add more, click enter... ")
        input()
        clear_terminal()
        register_classes(student, class_list)
    else:
        time.sleep(2)
        print("\nGreat, you're all set!\n")

def attend_class(stuName, className, decision, options):

    # Make branch statements based on the answer of student's action
    # If decision = G: go to class, start class
    # If decision  = S: skip class, ask again until student says go to class
    if decision == "S":
        print("Ooh. Good try but, better luck next time :)")
        time.sleep(1)
        clear_terminal()
        printOptions(options)
        new_ans = grab_action(options)
        attend_class(stuName, className, new_ans, options)
    else:
        course = Course(className)
        print(course)
        time.sleep(5)

        # There are going to be different teachers for every class
        # Write a match switch to assign teacher a different name
        # depending on what className is

        teacher = Teacher("Mr. Krabs")
        start_class(stuName, teacher, course)


def start_class(stuName, teacher, course):
    clear_terminal()
    time.sleep(1)
    print(teacher)


def grab_action(options):

    next = input("Enter option here: ")

    if next.upper() in options.keys():
        return next.upper()
    else:
        print("Invalid entry. Try again")
        time.sleep(1)
        clear_terminal()
        printOptions(options)
        grab_action(options)
        
    time.sleep(1)
    return next