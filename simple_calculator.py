# This is a Simple Calculator Program

import math
import time

def addition(num1, num2):
    return (num1 + num2)

def subtraction(num1, num2):
    return (num1 - num2)

def multiplication(num1, num2):
    return (num1 * num2)

def division(num1, num2):
    if(num2 == 0):
        return ("Divisor cannot be 0")
    return (num1 / num2)

def square_root(num1):
    return math.sqrt(num1)

def power(num1, num2):
    return pow(num1,num2)

def modulo(num1, num2):
    return (num1 % num2)


while True:
    print("\n This is a Calculator")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Exponentiate")
    print("7. Modulo")
    print("8. Exit")

    choice = input("Select and option (1-8): ")

    if (choice == "8"):
        print("Exiting the Calculator")
        break

    if (choice in ['1','2','3','4','6','7']):
        number1 = float(input("Enter First Number: "))
        number2 = float(input("Enter Second Number: "))
    else:
        number = float(input("Enter Number to Square Root: "))

    if (choice == '1'):
        result = addition(number1, number2)
        print("Result: ", result)

    elif(choice == '2'):
        result = subtraction(number1, number2)
        print("Result: ", result)
    
    elif(choice == '3'):
        result = multiplication(number1, number2)
        print("Result: ", result)
    
    elif (choice == '4'):
        result = division(number1, number2)
        print("Result: ", result)

    elif(choice == '5'):
        result = square_root(number)
        print("Result: ", result)

    elif(choice == '6'):
        result = power(number1, number2)
        print("Result: ", result)

    elif(choice == '7'):
        result = modulo(number1, number2)
        print("Result: ", result)

    else:
        print("Invalid Option. Try Again")


    time.sleep(2)

    
