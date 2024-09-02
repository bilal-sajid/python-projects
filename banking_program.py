def show_balance(balance):
    print()
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: $"))

    if amount < 0:
        print()
        print("That's not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: $"))

    if amount > balance:
        print()
        print("Insufficient Funds")
        return 0
    elif amount < 0:
        print()
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

def main():
    balance =  0
    is_running = True

    while is_running:
        print()
        print("---------- Banking Program ----------")
        print()
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        match choice:
            case "1" :
                show_balance(balance)
            case "2" :
                balance += deposit()
            case "3" :
                balance -= withdraw(balance)
            case "4" :
                is_running = False
            case _ :
                print()
                print("Not a valid choice")
                print()


    print("Thank you! Have a nice day")

if __name__ == '__main__':
    main()