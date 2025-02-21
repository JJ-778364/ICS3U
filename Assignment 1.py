# Part 1
import math
print("Welcome to the product even/odd detector!!")
n1 = input("Please input your first number: ")
n1 = float(n1)
n2 = input("Please input your second number: ")
n2 = float(n2)
if (n1 % 2 == 0) and (n2 % 2 == 0):
  print("Your number is EVEN!")
elif (n1 % 2 > 0) and (n2 % 2 == 0):
  print("Your number is EVEN!")
elif (n1 % 2 > 0) and (n2 % 2 > 0):
  print("Your number is ODD!")

# Part 2
import math
print("Welcome to the cube diagonal calculator!")
s = input("Please input the side length of your cube: ")
s = int(s)
if 0>s:
  print("Please input a postive length!")
else:
  d = s*math.sqrt(3)
  d = round(d, 2)
  print("The length of the inner diagonal of a cube with a side length of", s, "is", d, "!")

# Part 3
import math
print("Welcome to the coin calculator!")
ch = input("Please input your change in CENTS: ")
ch = int(ch)
ch = ch % 100
n25 = ch/25
n25 = int(n25)
rest = ch % 25
n10 = rest/10
n10 = int(n10)
rest2 = rest % 10
n5 = rest2/5
n5 = int(n5)
rest3 = rest2 % 5
n1 = rest3/1
n1 = int(n1)
print("Your change is", n25, "quarters,", n10, "dimes,", n5, "nickels, and", n1, "pennies")
