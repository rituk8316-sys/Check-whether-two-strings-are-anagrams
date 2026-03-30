# Program to check whether two strings are anagrams
# Author: Your Name
# Description: This program checks if two strings contain the same characters

def are_anagrams(str1, str2):
    # Convert both strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Remove spaces
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    # If lengths are different → not anagram
    if len(str1) != len(str2):
        return False

    # Count characters manually
    char_count = {}

    for ch in str1:
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1

    for ch in str2:
        if ch in char_count:
            char_count[ch] -= 1
        else:
            return False

    # Check all values are 0
    for value in char_count.values():
        if value != 0:
            return False

    return True


# Taking input from user
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

# Function call
if are_anagrams(string1, string2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")
