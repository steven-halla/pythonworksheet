import datetime

#inputs needed
#need two inputs for name and age
#make variable current year
#take 100 - user age and add result to the current year variable to see when they are 100 years old

def userInfo():
    now = datetime.datetime.now().year
    nameInput = input("input your name")
    ageInput = input("input your age")
    userAge = int(ageInput)
    yearOfHundred = 100 - userAge + now
    print(str("Your name is ") + str(nameInput) + str(" and you will turn 100 years old in ") + str(yearOfHundred) + str("."))


userInfo()