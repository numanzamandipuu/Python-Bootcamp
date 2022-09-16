alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text_letter, shift_ammount):
    cipher_text = ""

    for n in text_letter:
        text_position = alphabet.index(n)
        new_position = text_position + shift_ammount

        if new_position > 25:
            new_position = new_position - 26

        new_letter = alphabet[new_position]
        cipher_text += new_letter

    print(f"The encoded text is {cipher_text}")


encrypt(text_letter = text, shift_ammount = shift)