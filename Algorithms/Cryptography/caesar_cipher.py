# Each letter of plain text is replaced by a letter with some fixed number of positions down with alphabet
# Kind of shifting the indexes of letters.

def encrypt(text, shift):
    result = ""

    # transverse the plain text
    for i in range(len(text)):
        char = text[i]

        # ----- Checkers --------
        print('Ord Value: ', ord(char))
        print('Chr Value: ', chr(ord(char)))

        # Uppercase letters encryption
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        if char.isupper():
            result += chr((ord(char) + shift - 97) % 26 + 97)

    return result


# Example Case
message = "ENCRYPTION Text"
_shift = 2

print("Raw Text : ", message)
print("Shift Value : ", str(_shift))
print("Encrypted Text : ", encrypt(message, _shift))






