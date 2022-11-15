with open("D:/Python-Bootcamp/Day 24 - Intermediate - Files, Directories and Paths/06 - Introducing the Mail Merge Challenge/Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()
    for i in names:
        i = i.strip()

        with open("D:/Python-Bootcamp/Day 24 - Intermediate - Files, Directories and Paths/06 - Introducing the Mail Merge Challenge/Input/Letters/starting_letter.txt") as starting_letter:
            first_line = starting_letter.readlines()
            for line in first_line:
                line = line.strip()
                new_line = line.replace("[name]", i)
                with open(f"D:/Python-Bootcamp/Day 24 - Intermediate - Files, Directories and Paths/06 - Introducing the Mail Merge Challenge/Output/ReadyToSend/letter_for_{i}.txt", mode= "a") as new_letter:
                    new_letter.write(f"{new_line}\n")