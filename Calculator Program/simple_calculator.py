import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}


def calculator():
    continue_operations = True
    first_num = float(input("Enter the First Number: "))

    while continue_operations:

        for symbol in operations:
            print(symbol)
        op = input("Enter Operation: ")

        second_num = float(input("Enter the Next Number: "))

        result = operations[op](first_num,second_num)

        print(f"Result is: {result}")
        continuing = input(f"Type 'y' to continue with {result}, or type 'n' to start a new calculation: ")

        if continuing == 'n':
            continue_operations = False
            print("\n" * 20)
            calculator()
        else:
            first_num = result

calculator()