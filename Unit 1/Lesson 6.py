import math
print("Formatting your year of birth and age as Year.Age")
yob = input("Insert your year of birth: ")
yob = float(yob)
age = input("Insert your age: ")
age = float(age)
yob = yob*2+5
ans = yob*50+age
ans = (ans-250)/100
print("Your result is: ", ans)
