PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()

    for name in names:
        name = name.strip()

        with open("./Input/Letters/starting_letter.txt") as starting_letter:
            letter = starting_letter.read()
            final_letter = letter.replace(PLACEHOLDER, name)

            with open(f"./Output/ReadyToSend/Letter_to_{name}.txt", "w") as ready_to_send:
                ready_to_send.write(final_letter)