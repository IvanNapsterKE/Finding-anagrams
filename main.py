# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word):
    
    str1 = input("First word: ")
    str2 = input("Second word: ")
    
    return sorted(str1) == sorted(str2)  

print(find_anagrams("word"))



