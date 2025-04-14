print("Palindrome program!")
words = ["racecar", "noon", "desk", "civic", "store", "rotor", "madam", "kayak", "school", "refer"]
for pali in range(len(words)):
    word = words[pali]
    palindrome = True
    for x in range(len(word) // 2):
        if word[x] != word[len(word) - 1 - x]:
            palindrome = False
    if palindrome:
        print(word, "is a palindrome")
    else:
        print(word, "is not a palindrome")
