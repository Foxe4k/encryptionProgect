ALPHABET = "abcdefghijklmnopqrstuvwxyz"
MessageToEncrypt = input("Введите строку для шифра")
encryptedMessege=""
for letter in MessageToEncrypt:
    place = ALPHABET.find(letter)
    newPlace = (place + 1 + len(ALPHABET)) % len(ALPHABET)
    if letter in ALPHABET:
        encryptedMessege+=ALPHABET[newPlace]
    else:
        encryptedMessege+=letter
print(encryptedMessege)