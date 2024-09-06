from art import logo
print(logo)

def caesar(original_text, shift_amount, encode_or_decode):
    
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter in alphabet:
            current_position = alphabet.index(letter)
            next_position = current_position + shift_amount

            # To avoid out of range error
            next_position = next_position % len(alphabet)
            output_text += alphabet[next_position]

        else:
            output_text += letter

    print(f"Here is the {encode_or_decode}d result: {output_text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
is_running = True

while is_running:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart = input("Do you want to go again (yes or no): \n").lower()

    if restart == "no":
        is_running = False
        print("Goodbye")








