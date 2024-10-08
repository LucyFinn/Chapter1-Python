myList = [16, "Lucy", 3.14, True]
print(myList)
print(myList[1])
print(myList[-1])
print(myList[0])
print(myList[0:2])
#print(myList[5]) would be an error as there is no value for 5

#append means add to the end of the list
#insert puts a new variable in the place
#remove means that it will remove a variable
#pop will remove an item at its position and return its variable
myList.append("Hello")
myList.insert(1,"Groovy")
print(myList)
myList.remove(True)
print(myList)
myList.pop(3)
print(myList)

#pg37 Tasks
myString = "Lucy Finn"
print(myString)
myStringList = list(myString)
print(myStringList)

print(type(myString))
print(type(myStringList))

myStringList = ["L", "u", "c", "y", " ", "F", "i", "n", "n"]
print(myStringList[1])
print(myStringList[0])
print(myStringList[5])
print(myStringList[0:7])

if "u" in ["L", "u", "c", "y"]:
    print("It is in the list!!")
    
myCars = ["Fiat", "Honda", "Toyota", "BMW"]
print("Enter a make of cars: ")
carName = input()
if carName not in myCars:
    print("We do not stock", carName)
else:
    print("Yes! we stock", carName)

myList = [16, "lucy", 3.14, True]
print(myList)
for i in range(len(myList)):
    #print(myList[i])
    myList.pop(-1)
    print(myList)
    
myNums = []
for i in range(11):
    myNums.append(i)
    print(myNums)

myList = [16, "lucy", 3.14, True, 18, "hottie"]
counter = 0
print(myList)
while counter < (len(myList)):
    #print(myList[i])
    myList.pop(-1)
    print(myList)

myList = [27, 33, 9, 27, 8, 5, 27]
numSought = 27
freqNum = 0
counter = 0

while counter < len(myList):
    if myList[counter] == numSought:
        freqNum += 1
        print("Found at index: ",counter)
    counter+=1
    
print(numSought, "found", freqNum, "times!!")

myList = [1, -19, 27, 8, -5, 9]
print(myList)
counter = 0
while counter < len(myList):
    if myList[counter] < 0:
        myList[counter] = 0
    counter+=1
print(myList)

myList = [1, -19, 27, 8, -5, 9]
print(myList)
for item in myList:
    print(item)

myList = [1, -19, 27, 8, -5, 9]
print(myList)
for item in myList:
    if item < 0:
        item = 0 
print(myList)

myList = [1, -19, 27, 8, -5, 9]
print(myList)
for counter in range(len(myList)):
    if myList[counter] < 0:
        myList[counter] = 0
print(myList)
