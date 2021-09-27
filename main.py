ALPHABET_EN = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_RU ="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


language=input("Введите язык(RU-Русский;EN-Английский)")
MessageToEncrypt = input("Введите строку для шифра")
encryptedMessege = ""
if language == "RU":
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
print(encryptedMessege)