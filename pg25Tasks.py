#Task 1
artist = input("Who is your favourite artist? ")
comp = (" WOW! That artist is brilliant!")
print(artist + comp)

#Task 2
print()
fName = input("Please input your first name: ")
sNAme = input("Please input you second name: ")
print("Hi!",fName, sNAme)

#Task 3
print()
hour = int(input("Please enter a number of hours: "))
min = int(input("Please enter a number of minutes: "))
sec = int(input("Please enter a number of seconds: "))
second = 60
mins2 = (min*second)
hour1 = (hour*second)
hour2 = (hour1*second)
total = (hour2 + mins2 + sec)
print("Your total in minutes is:", total)

#Task 4
print()
number = int(input("Please enter a 5 digit number: "))
mins = 60
answer = (number // mins)
print("Your number represents", answer, "minutes!")

#Task 5
print()
letter = input("Please type in 5 letters of your choice: ")
ascii = [ord(char) for char in letter]
print(ascii)

#Task 6
print()
elect = 684
unit = 0.19
month = (elect*unit)
print("Ahmed is paying €",month , "of electricity per month")
user = int(input("Please enter the number of units of electricity you've used this month: "))
answer = (user*unit)
print("You need to pay €",answer , "of electricity this month")

#Task 7 
print()
fish = 4.50
chips = 2.80
orderF = int(input("How many portions of fish would you like? "))
orderC = int(input("How many portions of chips would you like? "))
fish2 = (fish*orderF)
chips2 = (chips*orderC)
price =(fish2 + chips2)
print("Your total price is €",price )
tax = 1.09
vat = (price*tax)
vat1 = (vat-price)
print("Your total VAT would be €", vat1)
