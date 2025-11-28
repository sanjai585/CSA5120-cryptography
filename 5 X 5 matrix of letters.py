def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    # Add key characters
    for ch in key:
        if ch.isalpha() and ch not in used:
            used.add(ch)
            matrix.append(ch)

    # Add remaining alphabet (I/J treated as one)
    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in used:
            used.add(ch)
            matrix.append(ch)

    # convert list into 5x5 matrix
    return [matrix[i:i+5] for i in range(0, 25, 5)]


def find_position(matrix, letter):
    if letter == "J":
        letter = "I"
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == letter:
                return r, c
    return None, None


def prepare_text(text):
    text = text.upper().replace("J", "I")
    filtered = "".join([c for c in text if c.isalpha()])

    result = ""
    i = 0
    while i < len(filtered):
        a = filtered[i]
        b = ""

        if i + 1 < len(filtered):
            b = filtered[i+1]

        if a == b:  # duplicate letter
            result += a + "X"
            i += 1
        else:
            result += a + (b if b else "X")
            i += 2

    if len(result) % 2 != 0:
        result += "X"

    return result


def encrypt_pair(a, b, matrix):
    r1, c1 = find_position(matrix, a)
    r2, c2 = find_position(matrix, b)

    # Rule 1: same row
    if r1 == r2:
        return matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]

    # Rule 2: same column
    if c1 == c2:
        return matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]

    # Rule 3: rectangle rule
    return matrix[r1][c2] + matrix[r2][c1]


def playfair_encrypt(plaintext, key):
    matrix = generate_key_matrix(key)
    prepared = prepare_text(plaintext)
    encrypted = ""

    for i in range(0, len(prepared), 2):
        encrypted += encrypt_pair(prepared[i], prepared[i+1], matrix)

    return matrix, prepared, encrypted


# ------------------ Main Program ------------------
key = input("Enter keyword: ")
plaintext = input("Enter plaintext: ")

matrix, prepared, encrypted = playfair_encrypt(plaintext, key)

print("\nPlayfair Matrix (5x5):")
for row in matrix:
    print(" ".join(row))

print("\nPrepared Text:", prepared)
print("Encrypted Text:", encrypted)
