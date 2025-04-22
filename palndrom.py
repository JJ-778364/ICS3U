"""
Jenna Jawarneh
778364
ICS3U

Variable Dictionairy:
words = The list of words we want to check for palindromes
"""
# Title to describe what the program does.
print("Welcome to the Palindrome Program! This program will determine if a word is a palindrome.")

# The list of words that we want to check for palindromes in an array, set to the variable "words".
words = ["racecar", "noon", "park", "civic", "store", "rotor", "play", "kayak", "class", "refer"]

# A loop that checks every index of the list, which is every word i
for i in range(len(words)):
    word = words[i]
    palindrome = True
    for x in range(len(word) // 2):
        if word[x] != word[len(word) - 1 - x]:
            palindrome = False
    if palindrome:
        print(word, "is a palindrome")
    else:
        print(word, "is not a palindrome")
        
        
        
