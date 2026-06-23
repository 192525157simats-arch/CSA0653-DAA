def firstPalindrome(words):
    for word in words:
        if word == word[::-1]:
            return word
    return ""

# Example 1
words = ["abc", "car", "ada", "racecar", "cool"]
print(firstPalindrome(words))   # Output: ada

# Example 2
words = ["notapalindrome", "racecar"]
print(firstPalindrome(words))   # Output: racecar
