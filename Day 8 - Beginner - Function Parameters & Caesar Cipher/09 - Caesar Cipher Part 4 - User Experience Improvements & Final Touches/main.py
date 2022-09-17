def ceasar(direction_parameter, text_parameter, shift_parameter):
    cipher_text = ""

    for n in text_parameter:
        if n in alphabet:
            text_position = alphabet.index(n)

            if direction_parameter == "encode":
                new_position = text_position + shift_parameter
                if new_position > 25:
                    new_position = new_position % 26

            elif direction_parameter == "decode":
                new_position = text_position - shift_parameter
                if new_position < 0:
                    new_position = new_position % 26
                    
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += n
            
    print(f"Here's the {direction_parameter}d result: {cipher_text}")


import art
print(art.logo)

cipher_end = False
while cipher_end == False:

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
    else:
        print("Please pick a valid keyword.")
        break

    if direction == "encode" or direction == "decode":
        ceasar(direction_parameter = direction, text_parameter = text, shift_parameter = shift)

    cipher_command = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if cipher_command == "yes":
        cipher_end = False
    elif cipher_command == "no":
        cipher_end = True
        print("Goodbye!")
    else:
        print("Please pick a valid keyword.")
        break