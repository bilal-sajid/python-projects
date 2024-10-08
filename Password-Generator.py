import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

### ----- METHOD 1 ----- ###

# final_password = ""
#
# for char in range(0, nr_letters):
#     random_choice = random.choice(letters)
#     final_password = final_password + random_choice
#
# for char in range(0, nr_symbols):
#     random_choice = random.choice(symbols)
#     final_password = final_password + random_choice
#
# for char in range(0, nr_numbers):
#     random_choice = random.choice(numbers)
#     final_password = final_password + random_choice
#
# print("Your password is: ", final_password)

### ----- METHOD 2 ----- ###

password_list = []

for char in range(0, nr_letters):
    random_choice = random.choice(letters)
    password_list.append(random_choice)

for char in range(0, nr_symbols):
    random_choice = random.choice(symbols)
    password_list.append(random_choice)

for char in range(0, nr_numbers):
    random_choice = random.choice(numbers)
    password_list.append(random_choice)

print("\nSelected these characters: ")
print(password_list)

print("\nShuffling...\n")
random.shuffle(password_list)

final_password = ""
for char in password_list:
    final_password += char

print("Your password is: ", final_password)
print()
