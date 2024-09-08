from data import MENU, resources


def print_report(mon):
    """
    Prints a report of the resources and money in the machine
    """
    print()
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${mon}")
    print()



def sufficient_resources(selection):
    """
    Takes the coffee selection and compares if there are enough resources
    """

    for key in MENU[selection]["ingredients"]:
        # print(key)

        if resources[key] < MENU[selection]["ingredients"][key]:
            # Not enough resources to make the specific drink
            print(f"\nSorry there is not enough {key}")
            return False
        
        else:
            # There are enough resources
            return True



def process_coins():
    """
    returns total amount from the coins inserted
    """

    print("\n" * 2)
    print("Insert Coins.")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
    return (total)



def transaction_successful(input_money, selection):
    """
    Returns True if the payment is accepted.
    Returns False if the amount is insufficient.
    """
    
    print()
    print(f"The money you put in was ${input_money:.2f}")
    print(f"The money required is ${MENU[selection]["cost"]:.2f}")

    if input_money >= MENU[selection]["cost"]:
        change = input_money - MENU[selection]["cost"]
        print(f"Here is ${change:.2f} in change")
        return True
    
    else:
        print("\nSorry that's not enough money. Money refunded")
        return False



def make_coffee(selection):
    for key in MENU[selection]["ingredients"]:
        resources[key] -= MENU[selection]["ingredients"][key]



is_running = True
money_in_machine = 0.0

while is_running:
    print("Type 'off' to turn off the program")
    print("Type 'report' to get a report")
    coffee_selection = input("\nWhat would you like? (espresso/latte/cappuccino): ")



    if (coffee_selection == "off"):
        is_running = False

    elif (coffee_selection == "report"):
        print_report(money_in_machine)

    elif(coffee_selection == "espresso" or coffee_selection == "latte" or coffee_selection == "cappuccino"):
        enough_resources = sufficient_resources(coffee_selection)

        if enough_resources:
            inputted_money = process_coins()
            successful_transaction = transaction_successful(inputted_money, coffee_selection)

            if successful_transaction:
                money_in_machine += MENU[coffee_selection]["cost"]
                make_coffee(coffee_selection)
                print(f"\nHere is your {coffee_selection}. Enjoy!")
            else:
                pass

        else:
            pass

    
    # print_report(money_in_machine)

