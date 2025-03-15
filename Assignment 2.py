"""
Name: Jenna Jawarneh
Student Number: 778364
Course Code: ICS3U
Variable Dictionary:
  number = the random number selected that the user attempts to guess
  attempts = the number of tries the user gets
  guesscorrect = boolean variable to see if the user guessed correctly
"""

import random

print("Hello! Welcome to the number guessing game!")
  # A print statement to introduce the game
print("I am thinking of a number between 1 and 100. You have 6 tries.")
  # A print statement explaining the rules

number = random.randrange(1, 100, 1)
  # The number the user must guess is set to be random from 1-100 with 1 space in between each number.
  # random.randrange is used to set this range
attempts = 0
  # The user starts off with 0 attempts at guessing
guesscorrect = False
  # Their guess is set to false unless proven otherwise

while attempts < 6:
# This is a loop that keeps their guesses going and stops at 6 guesses
  attempts += 1
  # The number of attempts goes up by one
  guess = int(input("Guess #%d: " % attempts))
  # The number they guess is set to be an integer, and the code displays the number of attempts they are at
  if guess < number:
  # If their guess is lower than the number...
    print("Higher!")
    # The code tells them the number is higher
  elif guess > number:
  # And if their guess is higher than the number...
    print("Lower!")
    # The code tells them to guess lower
  else:
  # If none of the previous conditions apply...
    guesscorrect = True
    # The users guess is correct, setting the "guesscorrect" vairable to True
    attempts += 6
    # The number of attempts is increased by 6 to immediately exit the loop
if guesscorrect:
# After exiting the loop, if the users guess was correct...
  print("You Guessed right!")
  # The code prints this out letting them know they were correct
else:
# If the loop ends without "guesscorrect" being set to True, meaning they got the number right...
  print("Sorry, you are out of guesses! The answer was", number)
  # The code will inform the user that they are out of guesses, and what the number was
