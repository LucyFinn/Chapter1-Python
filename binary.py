print(bin(128))

L = "L"
U = "u"
C = "c"
Y = "y"
L = ord(L)
U = ord(U)
C = ord(C)
Y = ord(Y)
print ("The decimal value for Lucy is:", L,U,C,Y)

myLetter = int(input("Enter a ASCII number: "))
key = int(input("Enter a key: "))
secretLetter = myLetter + key
print(secretLetter)
encryptedLetter = chr(secretLetter)
print(encryptedLetter)
