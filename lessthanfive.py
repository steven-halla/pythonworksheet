#print only numbers in list divisbile by 5

def lessThanFive(numbersList):
    newList = []
    x = numbersList
    for i in x:
        if i % 5 == 0:
            if i not in newList:
                newList.append(i)
    print(newList)

lessThanFive([1,4,5,10,12,15,18,20, 20])