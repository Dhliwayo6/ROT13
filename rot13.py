details = "pythoN"

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

new = ""

for letter in details:
    if letter in alphabet:
        if alphabet.index(letter) < 13:
            new += alphabet[alphabet.index(letter) + 13]
        else:
            new += alphabet[alphabet.index(letter) - 13]



print(new)

