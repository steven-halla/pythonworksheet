
def favoriteProgrammingLanguage():
    programmingList = ["python", "c#", "react", "typescript"]
    print("Here is the programming list please input one of the following",programmingList)
    userInput = input("type something out")
    print("Your input is:", userInput)
    if userInput in programmingList:
        print("you got it right!")
    elif userInput != programmingList[:]:
        print("you got it wrong")

favoriteProgrammingLanguage()