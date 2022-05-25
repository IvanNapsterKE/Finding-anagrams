def finding_anagrams(word):

    str1 = input("First word: ")
    str2 = input("Second word: ")

    return sorted(str1) == sorted(str2)


print(finding_anagrams("word"))