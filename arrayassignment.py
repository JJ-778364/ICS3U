# Import the array module
from array import array

# Define a list of words
words = ["apple", "banana", "cherry", "date", "elderberry"]

# Access and print the words in the array
for word in words:
    IsPalindrum = true
    letters = list(word)
    length = letters.length
    for(in index = 0 to length)
      if(letters[i] != letters[length-i])
        IsPalindrum = false
        break
    print("word : {word}  Palindrum is: {IsPalindrum} ")
      
    

# Add or modify words in the array if needed
words.append("fig") # Adding a new word
print("\nUpdated Array:", words)
