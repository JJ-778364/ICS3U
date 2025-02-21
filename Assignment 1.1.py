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
