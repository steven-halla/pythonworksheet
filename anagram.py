def isAnagram(string1, string2):
    print("anagram")
    print(string1, string2)

    if(sorted(string1) == sorted("".join(string2.split()))):
        print("True, these two words are an anamgrams")
    else:
        print("false, these two words are not an anagrams")

isAnagram("doggo", "ggood ")