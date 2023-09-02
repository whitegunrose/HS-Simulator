from classes import *
import os

import time
# After 30 seconds of the program executing, a message will appear notifying
# the student that their first class is starting. Need threading and time modules

def first_class_countdown():
    for num in range(3, 0, -1):
        print("...")
        time.sleep(1)
    
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
    print("Click enter to continue...")
    input()

    return newStuObj


def printOptions(options):

    
    print("=========================\n")

    print("What would you like to do next?\n")

    for action in options:
        print(f"{action} - {options[action]}")   

    print("\n=========================")
