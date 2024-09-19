myString = "Lucy Finn"
print(myString)

length = len(myString)
print(length)
print(myString[0])
print(myString[5])

print(myString[:4])
print(myString[5:])
print(myString[5:8])
print(myString[len(myString)-1])

myName = "Lucy Boden"
print(myName.__contains__("L"))
print(myName.__contains__("B"))

#Challenge
print()
string = input("Please enter your name: ")
length = len(string)
print(length)

if length > 8 and string[0].isupper():
    print(string, "is greater than 8 characters and starts with an upper case letter!!")
else:
    print("Sorry", string, "is not greater than 8 characters and it does not start with a upper case letter!")
