#Question 16
print("Welcome to the driving licence eligibility checker.") #(i)

age = int(input("What age are you? ")) 
#(ii) this creates a variable that allows the user to input their age
print("You entered", age) #(iii)

name = input("What is your name? ") #(v)

#(vi)
if age >= 74:
    print(name, "you are entitled to apply for a three-years drivers licence.")
elif age >= 17:
    print(name, "you are entitled to apply for a drivers licence.")
else:
    print(name, "you are not entitled to apply for a drivers licence.") #(iv)

#Question 1
a = 21
b = 10
print(a == b) #False
print(b != a) #True
print(a > b) #True
print(b <= a) #True
print(a == 10) #False
print(b != 21) #True
