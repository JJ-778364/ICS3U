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
