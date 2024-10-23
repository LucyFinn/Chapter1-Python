#Computers Open Book Test

#Challenge 2
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a second number: "))
answer = ((num1 + num2)/2)
print("The average of your 2 numbers: ", answer)

#Challenge 6
name = input("Enter your name: ")
if name == "Lucy":
    print("Your cool!")
else:
    print("Nice to meet you!")

#Challenge 7
hours = int(input("How many hours a day do you spend watching TV? "))

if hours < 2:
    print("That shouldn't rot your brain too much!")
elif hours >= 2 and hours <= 4:
    print("Aren't you getting square eyes?")
else:
    print("Fresh air beats channel flicking!")

#Challenge 8
print("Welcome to the Marking System!")
grade = int(input("What score did you get? "))
if grade >= 75:
    print("Well done you got an A !!")
elif grade >= 60:
    print("Good job you got B !!")
elif grade >= 35:
    print("You got a C !!")
else:
    print("You got a D !!")

#Challenge 10
import random
print("Welcome to Rock, Paper, Scissors")
turn = input("Please pick rock, paper or scissors: ")
actions = ["rock", "paper", "scissors"]
compAction = random.choice(actions)
print("you chose", turn,"computer chose", compAction)

if turn == compAction:
    print("It's a tie!!")
elif turn == "rock":
    if compAction == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose!")
elif turn == "paper":
    if compAction == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose!")
elif turn == "scissors":
    if compAction == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose!")
        
#Challenge 11
sen = input("Please enter a random sentence: ")
nums = len(sen)
print("The number of characters in your sentence is:", nums)

#Challenge 12
sentence = input("Please enter a random sentence: ")
sentence = sentence.upper()
print(sentence)

#Challenge 15
sen = input("Please enter another random sentence: ")
sen = sen.lower()
print(sen)

#Challenge 16
for number in range (1, 11):
    print(number)
    
#Challenge 18
number = int(input("Please enter a number: "))
print("Times tables for", number)
for i in range (1, 11):
    print(number, "x", i, "=", number*i)
