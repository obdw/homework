import random
def createArray():
    r=0
    print('Enter first index matrix: ')
    n = int(input())
    print('Enter second index matrix: ')
    m = int(input())
    array = []

    for i in range(n):
        array.append([])
        for j in range(m):
            array[i].append(random.randint(0,100))
            r+=1
    min = array[0][0]
    max = 0
    for i in range(n):
        for j in range(n):
            if (array[i][j] < min):
                min = array[i][j]
            elif (array[i][j] > max):
                max = array[i][j]
    for i in range(n):
        print(array[i])
    print(max, min)
createArray()
