def main():
    details = input("Details to be encrypted: ")
    print(encrypt(details))


def encrypt(details: str) -> str:
    """
    Encrypt user input using rot13 technique.

    :param details: user input
    :type details: str
    :return : an encrypted string
    :rtype: str
    """

    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    encrypted = ""

    for letter in details:
        if letter.isalpha():
            if alphabet.index(letter) < 13:
                if letter.isupper():

                    encrypted += alphabet.upper()[alphabet.upper().index(letter) + 13]

                else:
                    encrypted += alphabet[alphabet.index(letter) + 13]

            else:
                if letter.isupper():
                    encrypted += alphabet.upper()[alphabet.upper().index(letter) - 13]

                else:
                    encrypted += alphabet[alphabet.index(letter) - 13]

        else:
            encrypted += letter

    return encrypted


if __name__ == "__main__":
    main()
