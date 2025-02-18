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
