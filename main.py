alf= ["abcdefghijklmnopqrstuvwxyz"]
message="hello world"
encryptedMessege=""
for i in message:
    place=alf.find(i)
    newPlace =place
    if i in alf:
        encryptedMessege+=alf[newPlace]
    else:
        encryptedMessege+=i
print(encryptedMessege)