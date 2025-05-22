"""
Jenna Jawarneh
May 16th, 2025
Wordle Database
778364
ICS3U

This code is a database for the game wordle. Users can search for words and their 
corresponding dates, or dates and their corresponding words.

Variable Dictionary:
    
    choice: Stores the user's input, either "W" or "D"
    months: An array of the months used to convert month names to numbers
    monthNum: Holds the number version of a month
    monStr: A string version of the month number
    day: The day part of the date entered or read from file
    dayStr: Same as "day" but always two digits
    finalDate: A string of the full date in the format "YYYYMMDD"
    sarr: A list that stores all raw lines read from the file
    dates: A list that stores dates converted to integers
    words: A list that stores the corresponding word for each date in the file
    fh: File handle used to open and read the "wordle.dat" file
    eof: Used to check whether the end of the file has been reached
    line: A single line read from the Wordle data file
    parts: The parts from each line as: month, day, year, word
    m, d, y: Variables holding the month, day, and year
    w: The raw word from each line which might contain an extra character at the end
    newWord: The final version of the word after removing unwanted characters from the end
    lastLetter: The last character in the word used to check if it's a letter or a newline
    target: The word the user wants to search for
    found: Indicates if the word or date being searched for was found
    q: The date entered by the user converted to an integer
    earliest: The earliest date stored in the Wordle database
    latest: The latest date stored in the Wordle database

"""


# Introduction print statement
print("Welcome to the Wordle Database!!!")

# Variable to see if the user wants to search for a date or word
choice = input("Enter W if searching for a word and D if searching for a date: ")

# Array of months to convert the month needed to its corresponding number
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Function to determine the date as an integer
def inDate(mon, day, year):
    # Sets the variable that will be used for the month number to zero for now
    monthNum = 0
    # Loop that uses the previous array to determine the month number
    for i in range(len(months)):
        # If the month being searched for is equal to what is in the array...
        if months[i] == mon:
            # then its index gets 1 added to it, because the index starts at 0
            monthNum = i + 1

    # If the length of the date number is only 1...
    if len(day) == 1:
        # then it needs a 0 in front of it in order to match what's in the wordle file
        day = "0" + day
    # Changes the month to a string
    monStr = str(monthNum)
    # If the length of the month number is only 1...
    if len(monStr) == 1:
        # then it needs a 0 in front of it in order to match what's in the wordle file
        monStr = "0" + monStr

    # The final date from this function is in the order: year, month, day
    finalDate = year + monStr + day
    # Returns it as an integer to be used later in the code
    return int(finalDate)

# An empty array that will hold all lines read from the file
sarr = []
# An empty array that will hold the dates as integers
dates = []
# An empty array that will hold the word from each line
words = []

#  A try command to try the following code
try:
    # Tries to open the file to read and assigns it to this variable
    fh = open("wordle.dat", "r")
    # This marks the end of the file and is set to false until it reaches the end
    eof = False
    # A loop that goes until we reach the end of the file
    while not eof:
        # Reads the next line of the file into this variable
        line = fh.readline()
        # If the line is empty, then the program reached the end of the file...
        if line == "":
            # and the "end of file" variable is set to true to stop the loop
            eof = True
        # If the line is not empty, then it keeps going through the file
        else:
            # Adds every line to the "sarr" array
            sarr.append(line)
    
    # Closes the file
    fh.close()

# Catches OSErorrs instead of crashing the entire code
except OSError as err:
    # Prints the error
    print("OSError: ", err)
# Catches EOFErrors instead of crashing the entire code
except EOFError as err2:
    # Prints the error
    print("EOFError: ", err2)
    # Closes the file if needed in this case
    fh.close()

# While the index each line is lower than the number of lines in the file...
for i in range(len(sarr)):
    # Splits each line into 4 parts to divide the month, day, year, and word
    parts = sarr[i].split(" ")
    # The first part of each line is the month, set to this variable
    m = parts[0]
    # The second part of each line is the day, set to this variable
    d = parts[1]
    # The third part of each line is the year, set to this variable
    y = parts[2]
    # The last part of each line is the word, set to this variable
    w = parts[3]
        
    # This variable is set as an empty string to hold the final version of each word
    newWord = ""
    # This stores the last character of the word
    lastLetter = w[len(w)-1]

    # Checks if the last character is a capital letter from A-Z
    if lastLetter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        # If it is, then the final version of the word is set to this variable as is
        newWord = w
    # Otherwise, the last character is not a letter and needs to be removed
    else:
        # Goes through every letter except the last
        for j in range(len(w)-1):
            # This copies every letter except the last into the final variable of the word
            newWord = newWord + w[j]

    # The final version of the word is set to this variable to be used later
    w = newWord

    # Calls the function created earlier to convert all the date strings into integers
    dNum = inDate(m, d, y)
    # Appends the integer dates into the dates array
    dates.append(dNum)
    # Appends the words into the words array
    words.append(w)

# If the user is searching for a word
if choice == "W":
    # The target word is the input that the user puts in
    target = input("Enter your word (uppercase, exactly as it appears in the file): ")
    # This variable is set to false for now until the word is found
    found = False
    # Loop that goes through all the words
    for i in range (len(words)):
        # If the word is the same as the one being searched for by the user...
        if words[i] == target:
            # then a print statement along with the date using the same index to find it
            print(target, "was on", dates[i])
            # Found is set to true because the word was found
            found = True
    # Otherwise, the word does not exist in the wordle file
    if not found:
        # Print statement to inform the user
        print(target, "not found.")

# If the user is searching for the date instead...
elif choice == "D":
    # The year is set to this variable
    y = input("Enter the year: ")
    # The month is set to this variable
    m = input("Enter the month (only first 3 letters: e.g. Jan): ")
    # The date is set to this variable
    d = input("Enter the day: ")

    # Calls in the function to convert the string dates to integers
    q = inDate(m, d, y)

    # This is the earliest date in the file
    earliest = 20210619
    # This is the latest date in the file
    latest = 20240421

    # If the integer of the date inputted is less than the earliest date...
    if q < earliest:
        # then a print statement to inform the user it's not found in the file
        print(q, "is too early. It is before", earliest)
    # And if its more than the latest date...
    elif q > latest:
        # then a print statement to inform the user it's not found in the file
        print(q, "is too late. It is after", latest)
    
    # Otherwise the word has to be in the file for the date inputted
    else:
        # Found is set to false until the word is located in the file
        found = False
        # Loop to go through all the dates
        for i in range(len(dates)):
            # If the date is equal to the date being searched for...
            if dates[i] == q:
                # then a print statement along with the word on that day
                print("On", q, "the word was", words[i])
                # Found is set to true
                found = True
        # If the date was not found...
        if not found:
            # then a print statement to inform the user there was no word on that day
            print("No entry for", q)

# If the user did not input a W or D...
else:
    # then a print statement asking them to try again with a W or D
    print("Invalid choice. Please run again with W or D.")
