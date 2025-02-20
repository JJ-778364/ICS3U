import math
print("Welcome to the product even/odd detector!!")
n1 = input("Please input your first number: ")
n1 = int(n1)
n2 = input("Please input your second number: ")
n2 = int(n2)
if n1 % 2 == 0:
  m1 = 2
else:
  m1 = 3
  if n2 % 2 == 0:
    m2 = 2
  else:
    m2 = 3
    if m1 * m2 == 4:
      m1 == 4
    if m1 * m2 == 6:
      m1 == 4
    else:
      m1 == 9
      if m1 == 4:
        print("Your number is ODD!")
      else:
        print("Your number is EVEN!!")
