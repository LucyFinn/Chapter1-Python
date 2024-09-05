print()
x = 5
y = 3.14
z = "Pi"
k = True
#the next code is to figure out what type of data your information is
print(type(x))
print(type(y))
print(type(z))
print(type(k))

print()
x = 5
print(type(x))
x = 5.1
print(type(x))
#we did not have to type out that x changeed to a float as it could be detected in our code

print()
x = float(5)
print(type(x))
x = int(5.1)
print(type(x))
#by running this code we are forcing an integer to be a float and forcing a float to be an integer

print()
a = 5
b = 2
c = 4
d = 7
#we are going to be using the symbols to do maths sums with our new variables
print("1. is:", a+b)
print("2. is:", c-a)
print("3. is:", d*a)
print("4. is:", c/b)
print("5. is:", d//b)
# // means the number before the decimal point after division is always an integer
print("6. is:", c%b)
# % means the remainder in wholenumbers after division
print("7. is:", a**d)
# ** means to the power of

#BOMDAS
print()
answer = 4+5*(5*8)
print(answer)
answer1 = 8*5/4+(12-6)
print(answer1)

print()
string1 = "Hello"
string2 = "World!"
answer = string1+string2
print (answer)

print()
g = 4
print(g)
for i in range(5):
  g-=6
  print(g)
  #this will -6 from 4 5 times

print()
pi = 3.14
r = 7
answer = ((4/3)*pi)*r**3
answer = int(answer)
print(answer)
