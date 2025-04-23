"""
Jenna Jawarneh
778364
ICS3U

Variable Dictionairy:
words = The list of words beig checked for palindromes
word = Every word in the list
Palindrome = set to either True or False to determine if the word is a palindrome or not
i = counting index
x = coutning index

"""
# Title to describe what the program does.
print("Welcome to the Palindrome Program! This program will determine if a word is a palindrome.")

# The list of words that we want to check for palindromes in an array, set to the variable "words".
words = ["racecar", "noon", "market", "park", "civic", "rotor", "refer", "play", "kayak", "class"]

# A loop that checks every index of the list, which is every word in the array.
for i in range(len(words)):
    
    # Every word is an index in the array, starting at 0 with "racecar"
    # and ending at 9 with "class"
    word = words[i]
    
    # The code assumes the words are not palindromes, until proven true.
    palindrome = False
    
    # This loop turns every word into an array, dividing the number of characters by 2 and rounding down.
    for x in range(len(word) // 2):
        
        # This if statement checks if every letter in the first half of the word is the same as its  
        # corresponding letter in the second half of the word.
        # It checks by using the length of the word, then subtracting 1 to account for the loop starting
        # at 0, then subtracting the index. For example with the word "racecar", it calculates first if
        # r = the letter at 7 - 1 - 0, which is the r again.
        # a = the letter at 7 - 1 - 1 which is a, and so on.
        if word[x] == word[len(word) - 1 - x]:
            
            # If the previous condition applies, it sets the palindrome as true.
            palindrome = True

    # If it was proven as true, it prints this statement.
    if palindrome:
        print(word, "is a palindrome")
    
    # In any other scenario, it will be false, meaning the word is not a palindrome.
    else:
        print(word, "is not a palindrome")
        
        
        
