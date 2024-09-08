
### --- PART 1 --- ###

# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)

# timmy.shape("turtle")
# timmy.color("coral")

# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)

# my_screen.exitonclick()

### -------------- ###



### --- PART 2 --- ###

# from prettytable import PrettyTable

# table = PrettyTable()
# # print(table)

# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])

# table.align = "l"

# print(table)

### -------------- ###


### --- Building the Coffee Machine Program in OOP --- ###


### -------------------------------------------------- ###
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_running = True

while is_running:

    
    print("\nType 'off' to turn off the program")
    print("Type 'report' to get a report")

    options = menu.get_items()
    coffee_selection = input(f"\nWhat would you like? ({options}): ")
    print()

    
    if coffee_selection == "off":
        is_running = False

    elif coffee_selection == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(coffee_selection)

        if (coffee_maker.is_resource_sufficient(drink)) and (money_machine.make_payment(drink.cost)):

            coffee_maker.make_coffee(drink)

        else:
            pass

        
