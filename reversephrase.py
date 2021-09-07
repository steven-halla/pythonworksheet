def reversePhrase(phrase):
    newPhrase = phrase.split(" ")
    reverseWords = [i[ : : -1] for i in newPhrase]
    reverseSentence = " ".join(reverseWords)
    return reverseSentence

print(reversePhrase("Hello world how are you?"))