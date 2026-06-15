import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary from the CSV
phonetic_dict = {
    row.letter: row.code
    for _, row in data.iterrows()
}

while True:
    word = input("Enter a word: ").upper()

    try:
        result = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Please enter only alphabetic characters.")
    else:
        print(result)
        break
