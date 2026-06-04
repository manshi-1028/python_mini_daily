PLACEHOLDER_TEXT = "[name]"
with open("./Input/Names/invited_names.txt","r") as name:
    names = name.readlines()
with open("./Input/Letters/starting_letter.txt","r") as letter:
    letters = letter.read()
    for name in names:
        new=letters.replace(PLACEHOLDER_TEXT, name.strip())
        print(new)
        print("\n"*4)
        with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.docx","w") as new_letters:
            new_letters.write(new)


