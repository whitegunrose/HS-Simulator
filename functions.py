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

    return newStuObj


def printOptions(list):

    
    print("=========================\n")

    print("What would you like to do next?")

    for action in list:
        print(f"{action} - list{action}")   

    print("\n=========================")
