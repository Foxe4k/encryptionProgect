ALPHABET_EN = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_RU ="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def encryptedMessege(MessageToEncrypt,language):
    encryptedMessege = ""

    ALPHABET=ALPHABET_RU
    if language == "EN":
        ALPHABET=ALPHABET_EN

    for letter in MessageToEncrypt:
        place = ALPHABET.find(letter)
        newPlace = (place + 1 + len(ALPHABET)) % len(ALPHABET)

        if letter in ALPHABET:
            encryptedMessege += ALPHABET[newPlace]
        else:
            encryptedMessege += letter
    return encryptedMessege