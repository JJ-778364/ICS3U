print("Make a choice from the following menu: ")
print("A: apples")
print("B: bananas")
print("C: cherries")

ch = input("Your choice: ")

if (ch == "A"):
    print("I prefer apples")
elif (ch == "B"):
    print("I prefer bananas")
elif (ch == "C"):
    print("I prefer cherries")
else:
  print("Please input your choice from the options stated above!")


print("Number grades to letter grades converter.")
x = input("Please input your number grade: ")
x = int(x)
if (x >= 80) and (x <= 100):
  print("Your final grade is an A")
elif (x >= 70) and (x <= 79):
  print("Your final grade is a B")
elif (x >= 60) and (x <= 69):
  print("Your final grade is a C")
elif (x >= 50) and (x <= 59):
  print("Your final grade is a D")
elif (x < 50) and (x >= 0):
  print("Your final grade is an F")
elif (x > 100) or (x < 0):
  print("Please input a valid grade!")
