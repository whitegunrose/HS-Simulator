from classes import *
import os


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
    print("Click enter to continue...")
    input()



# Commented out function
"""def register(stuName, stuYear = 1):
    sentence = f"{stuName} is being registered here at J.R.O. High School for their "

    match stuYear:
        case 1:
            sentence += "1st year as an incoming freshman."

        case 2:
            sentence += "2nd year as a sophomore."

        case 3:
            sentence += "3rd year as a junior."

        case 4:
            sentence += "4th year as a senior."

    print(sentence)

    stuObj = Student(stuName, stuYear)
    print("The student can now be accessed under the object {name}".format(name = stuName))
    return stuObj"""

    