import os
from msvcrt import getch

pointer = "<---"
currentPos = 0
menuRunning = True

def add():
    print("Use the UP and DOWN arrow keys to navigate the calculator")
    print("ADD", pointer, "\nSUBTRACT\nMULTIPLY\nDIVIDE")
    key_press = ord(getch())
    if key_press == 13:
        os.system("cls")
        first_num = int(input("First Number: "))
        second_num = int(input("Second Number: "))
        print("Result:", int(first_num + second_num))
        print("Press any key to return to calculator")
def subtract():
    print("Use the UP and DOWN arrow keys to navigate the calculator")
    print("ADD\nSUBTRACT", pointer, "\nMULTIPLY\nDIVIDE")
    key_press = ord(getch())
    if key_press == 13:
        os.system("cls")
        first_num = int(input("First Number: "))
        second_num = int(input("Second Number: "))
        print("Result:", int(first_num - second_num))
        print("Press any key to return to calculator")
def multiply():
    print("Use the UP and DOWN arrow keys to navigate the calculator")
    print("ADD\nSUBTRACT\nMULTIPLY", pointer, "\nDIVIDE")
    key_press = ord(getch())
    if key_press == 13:
        os.system("cls")
        first_num = int(input("First Number: "))
        second_num = int(input("Second Number: "))
        print("Result:", int(first_num * second_num))
        print("Press any key to return to calculator")

def divide():
    print("Use the UP and DOWN arrow keys to navigate the calculator")
    print("ADD\nSUBTRACT\nMULTIPLY\nDIVIDE", pointer)
    key_press = ord(getch())
    if key_press == 13:
        os.system("cls")
        first_num = int(input("First Number: "))
        second_num = int(input("Second Number: "))
        print("Result:", int(first_num / second_num))
        print("Press any key to return to calculator")

add()
while menuRunning:

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