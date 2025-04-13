print("Palindrome program!")
words = ["racecar", "noon", "desk", "civic", "store", "rotor", "madam", "kayak", "school", "refer"]
for i in range(len(words)):
    word = words[i]
    palindrome = True
    for j in range(len(word) // 2):
        if word[j] != word[len(word) - 1 - j]:
            palindrome = False
    if palindrome:
        print(word, "is a palindrome")
    else:
        print(word, "is not a palindrome")
