import math
x = input("Please input a whole number between 1 and 50: ")
x = int(x)
if x>50:
  print(x, "is greater than 50 :( TRY AGAIN")
else:
  y = input("Please input another number between 1 and 50:")
  y = int(y)
  if y>50:
   print(y, "is greater than 50 :( TRY AGAIN!!!")
  else:
    print("Now deciding if", y, "is a factor of", x, "...")
  if y == 0:
    print("Division by 0 is not allowed! Try again </3")
  else: 
   rem = x % y
  if rem == 0:
    print("Yes!", y, "is a factor of", x)
  if rem != 0:
    print("NOOOO!", y, "is NOT a factor of", x)
