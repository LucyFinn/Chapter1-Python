#Task 1
counter = 100
while(counter < 1500):
    print(counter)
    counter +=1
print("Yes I've finally made:",counter)
counter = 1600
while(counter < 1500):
    print(counter)
    counter +=1
print("Yes I've finally made:",counter)
#a while loop only runs while something is True

#Task 2
number = 20
while(number >10):
    print(number)
    number -=1
print("Made it to" ,number)

#Task 3
bankBalance = -1
while bankBalance < 0:
    print("NO MONEY!!")
    break

password = "1234"
passwordInput = input("Enter Password: ")
while (passwordInput != password):
    print("Wrong Password!")
    break 
    
#Task 4
num = int(input("Enter a number, 0 to finish: "))
total = num
while num != 0:
    num = int(input("Enter another number, 0 to finish: "))
    total+=num
print("The total is:", total)

#Task 5
print("*************************************")
print("*             My Menu               *")
print("*************************************")
print("* 1 Calculate area of a circle      *")
print("* 2 Calculate the volume of a sphere*")
print("* 3 Exit                            ")
print("*************************************")
option = int(input("Enter option (1-3): "))
while (option!=3):
    if option == 1:
        r = float(input("Enter radius: "))
        area = 3.14*(r**3)
        print("Area is:", area)
        option = 0
    elif(option ==2):
        r = float(input("Enter radius: "))
        vol = (4/3)*(3.14*(r**3))
        print("Volume is:", vol)
        option = 0
    else:
        print("Invalid Choice!")
    print("1 Calculate area of a circle")
    print("2 Calculate the volume of a sphere")
    print("3 Exit")
    option = int(input("Enter option (1-3):"))
print("Time to rest!!")
