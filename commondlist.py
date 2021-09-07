import random



def makeList():
    newList = []
    array1 = []
    array2 = []
    for i in range(random.randint(1,12)):
        array1.append(random.randint(1,30))
        array2.append(random.randint(1,30))
    print(array1, array2)

    for j in array1:
        if j in array2:
            if j not in newList:
                newList.append(j)
    print(newList)

makeList()


def commonList(lista, listb):
    newList = []
    for i in lista:
        if i in listb:
            if i not in newList:
                newList.append(i)
    print(newList)


commonList([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
