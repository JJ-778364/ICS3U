print("Welcome to the Wordle Database!!!")
x = input("Enter W if searching for a word and D if searching for a date: ")
if x == "W":
  word = input("Enter your word: ")
if x == "D":
  year = input("Enter the year: ")
  month = input("Enter the month: ")
  day = input("Enter the day: ")

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for i in range(months):
  numMonth = month[i] + 1

def date(month: str, day: str, year: str) -> int:
  finaldate = (year, month, day)
  return finaldate
def search(word: str):
  word = word
