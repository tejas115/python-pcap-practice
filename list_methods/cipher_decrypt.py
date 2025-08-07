cipher = input('Enter your encrypted message: ')


def decrypt(cipher):
    result = ""
    # Iterate through the cipher
    for char in cipher:
        # Check if character is alphanumeric
        if char.isalpha():
            # Check char is either Z or z and append A, a respectively
            if char == 'A':
                result += 'Z'
            elif char == 'a':
                result += 'z'
            else:
                # Else shift to the next letter
                result += chr(ord(char) - 1)
        # If char is not alphanumeric just continue
        # Else append character as it is
        else:
            result += char

    return result


print("Cipher was :", cipher)
print("Decrypted message is :", decrypt(cipher))
