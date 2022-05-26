def finding_anagrams(word):

# Type first word and second word

    str1 = input("First word: ").lower()
    str2 = input("Second word: ").lower()

    
    for char in str1:
        
        if char not in str2:
            
            return False
    return True

#check length of words
    if len(str1) != len(str2()):
        
        return  False
    return True

  

print(finding_anagrams("word"))
