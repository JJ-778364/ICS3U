# Part 1
import math # "This is needed to use the math library.
print("Welcome to the product even/odd detector!!") # An introduction to the code, explaining what its purpose is using "print".
n1 = input("Please input your first number: ") # The user inputs their first number with "n1" being the variable which is "input".
n1 = int(n1) # The number needs to be an integer which is done using "int".
n2 = input("Please input your second number: ") # The user inputs their second number with "n2" being the variable this time.
n2 = int(n2) # This number also needs to be an integer.
if (n1 % 2 == 0) and (n2 % 2 == 0): # If the remainder of the first number divided by two and the second one divided by two is zero then their product will be even because they are both even numbers. "%" is used to find the remainder and "==" if it is equal to zero.
  print("Your number is EVEN!") # If this statement is true, it prints that their number is even.
elif (n1 % 2 > 0) and (n2 % 2 == 0): # If the remainder of the first number divided by two is greater than zero and the second one divided by two is zero then their product will be even because one of them is even and one of them is odd. ">" is used to see if the remainder is greater than zero.
  print("Your number is EVEN!") # If this statement is true, it prints that their number is even.
elif (n1 % 2 > 0) and (n2 % 2 > 0): # If the remainder of the first number divided by two and the second one divided by two is greater than zero then their product will be odd.
  print("Your number is ODD!") # If this statement is true, it prints that their number is odd.

# Part 2 
import math # This is needed to use the math library.
print("Welcome to the cube diagonal calculator!") # An introduction to the code, explaining what its purpose is using "print" to display the text.
s = input("Please input the side length of your cube: ") # "s" is used as a variable to represent the side length of the cube.
s = int(s) # The side length must be an integer using "int".
if 0>s: # If the number inputed is below zero, a negative number, the code stops the user.
  print("Please input a postive length!") # The user is asked to input a positive length next time.
else: # If the first statement doesn't apply to them, and their side length is postive:
  d = s*math.sqrt(3) # The length of the diagnol is the square root of three multipled by the side length.
  d = round(d, 2) # This rounds it down to two decimal places.
  print("The length of the inner diagonal of a cube with a side length of", s, "is", d, "!") # This displays the final result.

# Part 3
import math # This is needed to use the math library.
print("Welcome to the coin calculator!") # An introduction to the code, explaining what its purpose is.
ch = input("Please input your change in CENTS: ") # "ch" is the variable representing the total change the user needs. It is an "input".
ch = int(ch) # It has to be an integer.
ch = ch % 100 # This removes any whole dollars from the money in order to calculate the change accurately without them. The remainder is what is used throughout the rest of the code, which is the cents.
n25 = ch/25 # The number of cents divided by 25, which is how many quarters can be obtained from it.
n25 = int(n25) # It is then rounded down to an integer because we want whole numbers for each coin. You cannot have decimal parts of a coin.
rest = ch % 25 # The next calculation for the rest of the coins will be used from the remainder, after all the quarters are accounted for.
n10 = rest/10 # The number of the remaining cents from the quarters, divided by 10, which is how many dimes can be obtained from it.
n10 = int(n10) # It is then rounded down to an integer because we want whole numbers for each coin. You cannot have decimal parts of a coin.
rest2 = rest % 10 # The next calculation for the rest of the coins will be used from the remainded, after all the quarters and dimes have been accounted for.
n5 = rest2/5 # The number of the remaining cents from the quarters and dimes, divided by 5, which is how many nickels can be obtained from it.
n5 = int(n5) # It is then rounded down to an integer because we want whole numbers for each coin. You cannot have decimal parts of a coin.
rest3 = rest2 % 5 # The next calculation for the rest of the coins will be used from the remainded, after all the quarters, dimes, and nickels have been accounted for.
n1 = rest3/1 # The number of the remaining cents from the quarters, dimes, and nickels, divided by 1, which is how many pennies can be obtained from it.
n1 = int(n1) # It is then rounded down to an integer because we want whole numbers for each coin. You cannot have decimal parts of a coin.
print("Your change is", n25, "quarters,", n10, "dimes,", n5, "nickels, and", n1, "pennies") # The final statement, providing the result to the user.
