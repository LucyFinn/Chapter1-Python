#selections if, elif, else 
print("Hi")
colour = input("What is your fav colour? ")
if colour == "purple":
    print("I like purple too!!")
elif colour == "blue":
    print("I like blue too, but purple is better!!")
else:
    print("I hate that colour!!")
    
#Password task
print()
password = int(input("Please enter a password: "))
if password == 123456:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
    
#True or False
print()
blackCoffee = 5
whiteCoffee = 10
print(blackCoffee > whiteCoffee)
print((blackCoffee == 6) and (whiteCoffee == 10))
print((blackCoffee == 5) and (whiteCoffee == 10))
#with and both sides have to be true for it to print true
#with or only one side has to be right to print true
print((blackCoffee != 6) or (whiteCoffee == 10))
print(not(blackCoffee > 6) and (whiteCoffee == 10))

#GunsnRoses login page
username = "axl@gnr"
password = "novrain"

entname = input("Enter your username: ")
entpass = input("Enter your password: ")

if (entname == username) and (entpass == password):
    print("Welcome", username, "you are logged in!")
else:
    print("Sorry wrong details!")
