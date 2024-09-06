import art
print(art.logo)



def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest = 0

    for key in bidding_dictionary:
        if bidding_dictionary[key] > highest:
            highest = bidding_dictionary[key]
            winner = key
    
    print(f"\nThe highest bidder was {winner} at a bid of ${bidding_dictionary[name]}")

bidding_dictionary = {}
is_running = True

while is_running:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))

    bidding_dictionary[name] = bid

    continue_adding = input("Are there more participants? Type 'yes' or 'no'. \n").lower()

    if continue_adding == 'no':
        find_highest_bidder(bidding_dictionary)
        is_running = False
    elif continue_adding == 'yes':
        print("\n" * 10)






