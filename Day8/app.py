alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def run():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        print(f"Encrypted data: {encrypt(text, shift)}")
    else:
        print(f"Decrypted data: {decrypt(text, shift)}")


def encrypt(text, shift):
    text_list = list(text)
    encrypted = ""
    for i in range(0, len(text)):
        encrypted = encrypted + \
            alphabet[(alphabet.index(text_list[i])+shift) % 26]
    return encrypted


def decrypt(text, shift):
    text_list = list(text)
    decrypted = ""
    for i in range(0, len(text)):
        decrypted = decrypted + \
            alphabet[(alphabet.index(text_list[i])-shift) % 26]
    return decrypted


run()
