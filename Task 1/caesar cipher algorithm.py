def encrypt(key, message):
    result = ""
    for letter in message:
        if letter.isalpha():
            alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            letter_index = (alpha.find(letter.upper()) + key) % 26
            result += alpha[letter_index]
        else:
            result += letter
    return result

def decrypt(key, message):
    result = ""
    for letter in message:
        if letter.isalpha():
            alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            letter_index = (alpha.find(letter.upper()) - key) % 26
            result += alpha[letter_index]
        else:
            result += letter
    return result

def main():
    message = input("Enter a message: ")
    key = int(input("Enter a shift value: "))

    encrypted = encrypt(key, message)
    print("Encrypted message:", encrypted)

    decrypted = decrypt(key, encrypted)
    print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()