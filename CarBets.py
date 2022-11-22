import random
def rand():
        return random.randrange(0,10)

def test(carNumber):
    cars = []
    for i in range(carNumber):
        cars.append(rand())
    return cars

def test2(arr1):
    for i in arr1 :
        if(i <=0):
            return False
    return True

def test3(arr1,arr2):
    for i in range(len(arr1)):
        arr1[i]= arr1[i]-arr2[i]

def test4(x,value):
    arr = []
    for i in range(x):
        arr.append(value)
    return arr

