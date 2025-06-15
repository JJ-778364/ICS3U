"""
Jenna Jawarneh
June 14th, 2025
Wordle Game
778364
ICS3U

    This code allows users to play The Wordle Game through python.
    Please ensure the "pastwordles.txt" and "valid_wordle_words.txt" files are in the 
    same location, available to be opened.

Variable Dictionary for binarySearch function:

    wordList: List of valid words to search through
    target: The word the user guessed, being searched for in wordList
    low: Lower boundary for the binary search
    high: Upper boundary for the binary search
    mid: Middle index used to compare with the target word

ANSI Colour Dictionary:

    GREEN: ANSI code to colour correct letters green
    YELLOW: ANSI code to colour misplaced letters yellow
    RESET: ANSI code to reset color formatting

Random Number Generator Dictionary:

    timeRightNow: Current time in seconds since Jan 1, 1970
    decimalTime: Decimal part of current time (used to generate random number)
    finalRandomNum: Integer used to select a random word from "wordleBank"

File Dictionary:

    wordleBank: List of possible answer words for the game
    validWords: List of all valid guess words
    fh, fh2: File handles used to read word lists
    line, line2: Strings used to store each line from the files
    endofFile: Boolean variable to determine when the end of file is reached

Game Dictionary:

    word: The randomly selected Wordle word for the game session
    guessCorrect: Boolean variable to track if the user has guessed the word
    valid: Boolean variable to track if the user's guess is valid
    tryNum: Guess attempt number
    numTries: Boolean variable to track when the user reaches max tries
    guess: User's inputted guess
    feedbackForWord: Strings for each character in each word for feedback using colour
    wordCharacters: List of characters in the correct word
    guessedWordCharacters: List of characters in the user's guessed word
    
"""

# Imports the time library which is later used to generate a random number
import time

# Binary Search function
def binarySearch(wordList, target):
    
    # Sets the lower end to 0
    low = 0
    # Sets the higher end to the length of the word list - 1
    high = len(wordList) - 1

    # Loop that goes on until all words are checked
    while low <= high:
        
        # Calculates the middle index of the list of words
        mid = (low + high) // 2
        # If the word being searched for is directly in the middle,
        if wordList[mid] == target:
            # then the function returns "True", meaning the word is valid
            return True
        
        # If the word is alphabetically before the word being searched for,
        # then it has to be in the upper half of the list
        elif wordList[mid] < target:
            # Starts searching the upper half
            low = mid + 1
        
        # Otherwise,
        else:
            # the word is in the lower half of the list
            high = mid - 1

    # If the word was not found in the list, then return False
    return False

# Green ansi code
GREEN  = "\033[1;32m"
# Yellow ansi code
YELLOW = "\033[1;33m"
# Reset ansi code
RESET = "\u001B[0m"

# Gets the the time in seconds since Jan 1st, 1970, as float
timeRightNow = time.time()
# Gets the decimal value in order to create a random number
decimalTime = timeRightNow - int(timeRightNow)
# Multiple the decimal number by 1437 (which is the number of words in the wordle database),
# and add 1 to account for the fact that indices start at 0
# This generates the random number that will be used later to find a random 5 letter word
finalRandomNum = int(decimalTime * 1437) + 1

# Print statements introducing the code
print("WORDLE")
print("Rules: Your goal is to guess the selected word in 6 tries.")
print("Enter valid words to check if the letters are in the selected word.")
print("A green letter indicates the letter is in the word and in the right spot.")
print("An orange letter indicated that it is in the word, but not the right spot.")

# Empty array for the wordle database
wordleBank = []
# Empty array for the valid 5 letter words
validWords = []

# Tries to open the file
try:
    # File handle of the pastwordles
    fh = open("pastwordles.txt", "r")
    # Sets end of the file to false for now
    endofFile = False
    # While not at the end of the file, it keeps reading through it
    while not endofFile:
        # Reads each line and strips the newline character
        line = fh.readline().strip()
        # If there's an empty line
        if line == "":
            # Then the end of file has been reached and the loop can stop
            endofFile = True
        # Otherwise,
        else:
            # Append the line into the wordle database array
            wordleBank.append(line)
    # Close the file to avoid corruption
    fh.close()
# Catches OSErorrs instead of crashing the entire code
except OSError as err:
    # Prints the error
    print("OSError: ", err)
# Catches EOFErrors instead of crashing the entire code
except EOFError as err2:
    # Prints the error
    print("EOFError: ", err2)
    # Closes the file
    fh.close()

# Same process but on the file for the valid words
try:
    fh2 = open("valid_wordle_words.txt", "r")
    endofFile = False
    while not endofFile:
        line2 = fh2.readline().strip()
        if line2 == "":
            endofFile = True
        else:
            validWords.append(line2.upper())
    fh2.close()
except OSError as err:
    print("OSError: ", err)
except EOFError as err2:
    print("EOFError: ", err2)
    fh2.close()

# Chooses a random word using the previous random number that was generated
word = wordleBank[finalRandomNum % len(wordleBank)]

# Sets guess correct to false until the user guesses the word
guessCorrect = False
# Valid is set to true for now
valid = True
# Start at 1 try
tryNum = 1
# The limit of tries is set to false for now
numTries = False

# Loops while the user has not reached the max number of tries
while not numTries:
    # Sets valid as true at the start of every loop
    valid = True
    # If the user has not guessed the word yet
    if not guessCorrect:
        # Print their attempt number
        print("ATTEMPT #", tryNum, end="")
        # Their word as input
        guess = input(": ")
        # Convert their word to capital
        guess = guess.upper()

        # Binary search for their word using the function created earlier
        # to see if it is a valid five letter word from the file
        valid = binarySearch(validWords, guess)
       
        # If their word is not valid,
        if not valid:
            # print statement
            print("Please enter a valid word.")

        # If the word is valid
        elif valid:
            # An array for each letter in the word, empty for now
            feedbackForWord = ["", "", "", "", ""]
            # List the random word characters
            wordCharacters = list(word)
            # List the users guess characters
            guessedWordCharacters = list(guess)

            # For loop for the number of letters in each word (which is always 5)
            for i in range(5):
                # If the letter in the guessed word is the same as the random word
                if guessedWordCharacters[i] == wordCharacters[i]:
                    # make the letter green using ansi sequence
                    feedbackForWord[i] = GREEN + guessedWordCharacters[i]
                # Otherwise,
                else:
                    # keep the character empty for now
                    feedbackForWord[i] = ""
            
            # For loop for the number of letters in each word (which is always 5)
            for i in range(5):
                # If the character was not green
                if feedbackForWord[i] == "":
                    # If the character of the guessed word is in the random word
                    if guessedWordCharacters[i] in wordCharacters:
                        # and if it is not in the correct position in the word
                        if guessedWordCharacters[i] != wordCharacters[i]:
                            # Then turn it yellow!
                            feedbackForWord[i] = YELLOW + guessedWordCharacters[i]
                    
                    # Otherwise,
                    else:
                        # makes the colour of the other letters grey
                        feedbackForWord[i] = RESET + guessedWordCharacters[i]

            # For each coloured letter in the feedback of the word
            for i in feedbackForWord:
                # Prints each letter with its colour to inform the user
                print(i, end="")
            
            # Resets the colour formatting after printing the word
            print(RESET)

            # Adds to the number of tries
            tryNum += 1

        # If the user guesses the word,
        if guess == word:
            # print statement
            print("You win! The word is", word)
            # Set guess correct to true
            guessCorrect = True
            # Sets the number of tries to true, ending the loop
            numTries = True

        # If the user reached the max of six guesses,
        if tryNum > 6 and not guessCorrect:
            # print statement saying they are out of words
            print("Out of tries! The word was", word)
            # Sets the number of tries to true, ending the loop
            numTries = True
