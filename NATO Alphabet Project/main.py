import pandas

file_path = "NATO Alphabet Project/nato_phonetic_alphabet.csv"
data = pandas.read_csv(file_path)

phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}



def generate_phonetic():
    word = input("Enter a word: ").upper()

    try:
        output_list = [phonetic_dict[letter] for letter in word if letter != " "]

    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()

    else:
        print(output_list)

generate_phonetic()

