alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

if direction == "encode" or direction == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
else:
    print("Please pick a valid keyword.")


def encrypt(text_encrypt, shift_encrypt):
    cipher_text_en = ""

    for n in text_encrypt:
        text_position_en = alphabet.index(n)
        new_position_en = text_position_en + shift_encrypt

        if new_position_en > 25:
            new_position_en -= 26

        new_letter_en = alphabet[new_position_en]
        cipher_text_en += new_letter_en
    print(f"The encoded text is {cipher_text_en}")


def decrypt(text_decrypt, shift_decrypt):
    cipher_text_de = ""

    for n in text_decrypt:
        text_position_de = alphabet.index(n)
        new_position_de = text_position_de - shift_decrypt

        if new_position_de < 0:
            new_position_de += 26

        new_letter_de = alphabet[new_position_de]
        cipher_text_de += new_letter_de
    print(f"The decoded text is {cipher_text_de}")


if direction == "encode":
    encrypt(text_encrypt = text, shift_encrypt = shift)
elif direction == "decode":
    decrypt(text_decrypt = text, shift_decrypt = shift)