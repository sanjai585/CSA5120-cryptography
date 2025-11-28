def caesar_cipher(text, k):
    result = ""

    for char in text:
        if char.isalpha():
            base = 'a' if char.islower() else 'A'
            result += chr((ord(char) - ord(base) + k) % 26 + ord(base))
        else:
            result += char

    return result


# Main program
text = input("Enter a message: ")
k = int(input("Enter shift key (1-25): "))

if 1 <= k <= 25:
    encrypted = caesar_cipher(text, k)
    print("Encrypted message:", encrypted)
else:
    print("Invalid key! Key must be between 1 and 25.")
