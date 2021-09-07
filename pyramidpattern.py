def pyramidPattern():
    print("pyramid")
    count = 5
    upsideDown = 0
    firstRow = int(input("Type in a random number"))

    for a in range(firstRow):
        print("*", end=" ")


    for i in range(count, 0, -1):
        upsideDown += 1
        for j in range(1, i + 1):
            print("*", end=" ")
        print("")


pyramidPattern()