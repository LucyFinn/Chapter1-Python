#Practical Question
score = int(input("Please enter your house energy score: "))
if score <= 10:
    print("Your energy rating is a F")
elif score <= 20:
    print("Your energy rating is an E")
elif score <= 30:
    print("Your energy rating is a D")
elif score <= 40:
    print("Your energy rating is a C")
elif score <= 70:
    print("Your energy rating is a B")
else:
    print("Your energy rating is an A!!")
