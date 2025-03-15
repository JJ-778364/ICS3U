import random
print("Hello! Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100. You have 6 tries.")
number = random.randrange(1, 100, 1)
attempts = 0
guesscorrect = False
while attempts < 6:
  attempts += 1
  guess = int(input("Guess #%d: " % attempts))
  if guess < number:
    print("Higher!")
  elif guess > number:
    print("Lower!")
  else:
    guesscorrect = True
    attempts += 6
if guesscorrect:
  print("You Guessed right!")
else:
  print("Sorry, you are out of guesses! The answer was", number)
