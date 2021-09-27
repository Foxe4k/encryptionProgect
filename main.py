alf= "abcdefghijklmnopqrstuvwxyz"
message=input("Введите строку для шифра")
encryptedMessege=""
for i in message:
    place = alf.find(i)
    newPlace =(place + 1 + len(alf)) % len(alf)
    if i in alf:
        encryptedMessege+=alf[newPlace]
    else:
        encryptedMessege+=i
print(encryptedMessege)