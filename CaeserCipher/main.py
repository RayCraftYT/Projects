print("Welcome to the encryption/decryption machine.")
list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
        "s", "t", "u", "v", "w", "x", "y", "z"]


def switch():
    print("Encrypt/Decrypt Program")
    print("Menu")
    print("=================")
    print("Choose an option from below")
    print(" ")
    print("1. Encrypt")
    print("2. Decrypt")

    mode = input("Choose your option?")
    if mode == '1':
        encrypt()
    elif mode == '2':
        decrypt()
    else:
        print("Not valid")
        switch()


def encrypt():
    word = input("Please enter the word you would like to encrypt.")
    direction = input("Please enter the direction of the shift (r/l).")
    number = int(input("Please enter how much you would like to shift by."))
    if number > 26:
        print("Error.")
        encrypt()
    else:
        length = len(word)
        code = " "
        if direction == "r":
            for i in range(0, length):
                newPos = list.index(word[i]) + number
                code = code + list[newPos]

        elif direction == "l":
            for i in range(0, length):
                newPos = list.index(word[i]) - number
                code = code + list[newPos]

        print("Original word was: " + word)
        print("Encrypted word is: " + code)


def decrypt():
    code = input("Please enter the code to decrypt")
    direction = input("Please enter the direction this code was originally encrypted in.")
    number = int(input("Please enter how much this was originally shifted by."))
    if number > 26:
        print("Error.")
        decrypt()
    else:
        length = len(code)
        word = " "
        if direction == "r":
            for i in range(0, length):
                newPos = list.index(code[i]) - number
                word = word + list[newPos]

        elif direction == "l":
            for i in range(0, length):
                newPos = list.index(code[i]) + number
                word = word + list[newPos]

        print("Original word was: " + code)
        print("Decrypted word is: " + word)


switch()