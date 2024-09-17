#Question 16
print("Welcome to the driving licence eligibility checker.")
name = input("What is your name? ")
age = int(input("What age are you? "))
#this allows the user to input their age into the code
if age >= 74:
    print("You entered", age)
    print(name, "you are entitled to apply for a drivers licence.")
elif age:
    print("You entered", age)
    print(name, "you are entitled to a three year driving course.")
else:
    print("You entered", age)
    print(name, "you are not entitled to apply for a drivers licence.")

