def encrypt(text, k):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'a' if char.islower() else 'A'
            result += chr((ord(char) - ord(base) + k) % 26 + ord(base))
        else:
            result += char
    return result

def decrypt(text, k):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'a' if char.islower() else 'A'
            result += chr((ord(char) - ord(base) - k) % 26 + ord(base))
        else:
            result += char
    return result

# Main Program
text = input("Enter a message: ")
k = int(input("Enter shift key (1-25): "))

print("\n1. Encrypt")
print("2. Decrypt")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Encrypted message:", encrypt(text, k))
elif choice == 2:
    print("Decrypted message:", decrypt(text, k))
else:
    print("Invalid choice!")
