# if number is divisble by 4, buzz
# if number is divisbile by 7, fizz
# if number is divisbile by 28, buzzfizz
# print numbers in descending order



def reverseFizzBuzz(numbers):
    print("reverse fizz buzz")
    for i in range(numbers, 0, -1):
        if i % 28 == 0:
            print("buzzfizz")
        elif i % 4 == 0:
            print("buzz")
        elif i % 7 == 0:
            print("fizz")
        else:
            print(i)

reverseFizzBuzz(100)