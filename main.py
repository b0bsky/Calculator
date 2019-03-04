
# imports
import os
from msvcrt import getch

# variables
pointer = "<---"
currentPos = 0
menuRunning = True

# function that checks for validity of input
def validity(checkVariable):
    return checkVariable.isnumeric()


# function that adds 2 numbers and outputs the result
def add():
    # instructions
    print("Use the UP and DOWN arrow keys to navigate the calculator")
    print("ADD", pointer, "\nSUBTRACT\nMULTIPLY\nDIVIDE")
    # checks for users selection and adds
    key_press = ord(getch())
    if key_press == 13:
        os.system("cls")
        first_num = input("First Number: ")
        # checks validity of users input
        if validity(first_num):
            first_num = int(first_num)
            second_num = input("Second Number: ")
            if validity(second_num):
                second_num = int(second_num)
                print("Result:", int(first_num + second_num))
            else:
                print("Incorrect Value, please enter a whole number")
        else:
            print("Incorrect Value, please enter a whole number")

        # outputs result
        print("\nPress any key to return to calculator")

# function that subtracts 2 numbers and outputs the result
def subtract():
    # instructions
    print("Use the UP and DOWN arrow keys to navigate the calculator")
    print("ADD\nSUBTRACT", pointer, "\nMULTIPLY\nDIVIDE")
    # checks for users selection and subtracts
    key_press = ord(getch())
    if key_press == 13:
        os.system("cls")
        first_num = input("First Number: ")
        # checks validity of users input
        if validity(first_num):
            first_num = int(first_num)
            second_num = input("Second Number: ")
            if validity(second_num):
                second_num = int(second_num)
                print("Result:", int(first_num - second_num))
            else:
                print("Incorrect Value, please enter a whole number")
        else:
            print("Incorrect Value, please enter a whole number")

        # outputs result
        print("\nPress any key to return to calculator")

# function that adds 2 numbers and outputs the results
def multiply():
    # instructions
    print("Use the UP and DOWN arrow keys to navigate the calculator")
    print("ADD\nSUBTRACT\nMULTIPLY", pointer, "\nDIVIDE")

    # checks for users selection and multiplies
    key_press = ord(getch())
    if key_press == 13:
        os.system("cls")
        first_num = input("First Number: ")

        # checks validity of users input
        if validity(first_num):
            first_num = int(first_num)
            second_num = input("Second Number: ")
            if validity(second_num):
                second_num = int(second_num)
                print("Result:", int(first_num * second_num))
            else:
                print("Incorrect Value, please enter a whole number")
        else:
            print("Incorrect Value, please enter a whole number")
        # outputs result
        print("\nPress any key to return to calculator")

#function that adds 2 divide and outputs the result
def divide():
    # instructions
    print("Use the UP and DOWN arrow keys to navigate the calculator")
    print("ADD\nSUBTRACT\nMULTIPLY\nDIVIDE", pointer)
    # checks for users selections and multiplies
    key_press = ord(getch())
    if key_press == 13:
        os.system("cls")
        first_num = input("First Number: ")
        # checks for validity of users input
        if validity(first_num):
            first_num = int(first_num)
            second_num = input("Second Number: ")
            if validity(second_num):
                second_num = int(second_num)
                print("Result:", int(first_num / second_num))
            else:
                print("Incorrect Value, please enter a whole number\n")
        else:
            print("Incorrect Value, please enter a whole number\n")
        # outputs result
        print("\nPress any key to return to calculator")

# opens menu
add()

# menu loop
while menuRunning:

    # checks what user wants to do and acts applicably
    key_press = ord(getch())
    if key_press == 72:
        currentPos -= 1
    if key_press == 80:
        currentPos += 1
    if currentPos == 0:
        os.system("cls")
        add()
    elif currentPos == 1:
        os.system("cls")
        subtract()
    elif currentPos == 2:
        os.system("cls")
        multiply()
    elif currentPos == 3:
        os.system("cls")
        divide()
    elif currentPos == -1:
        os.system("cls")
        divide()
        currentPos = 3
    elif currentPos == 4:
        os.system("cls")
        add()
        currentPos = 1
currentPos = 1