#Question 16(a)
print("*******************") #(ii)
print("Times Table Program") #(i)
print("*******************") #(ii)

number = int(input("Enter a number: ")) #(iii)

if number < 0: #(iv)
    print("This program does not support negative numbers")
else:
    print("Multiplication of", number)

    for i in range (13): #(v)
        print(i,"x", number, "=", number*i) #(vi)
        
#Question 16(b)
print("Welcome to the Temperature Alert System")

degree = int(input("Enter a temperature value in degrees Celsius: "))

if degree < 20:
    print("Too cold. Turn up heating.")
elif degree >=20 and  degree <=24:
    print("Temperature is just right.")
else:
    print("Too warm. Turn the heating down.")
