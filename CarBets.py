import random

def rand():
        return random.randrange(0,10)

def randCarSpeed(carNumber):
    cars = []
    for i in range(carNumber):
        cars.append(rand())
    return cars

def carWinner(arr1):
    for i in arr1 :
        if(i <=0):
            return False
    return True

def calcDistance(arr1,arr2):
    for i in range(len(arr1)):
        arr1[i]= arr1[i]-arr2[i]

def numbersOfCars(x,value):
    arr = []
    for i in range(x):
        arr.append(value)
    return arr

def main():
    
    player = 2000
    carNumber = 2
    cont="y"
    while(cont=="y" and player>0):
        carBet = int(input())
        betAmount = int(input())
        x = numbersOfCars(carNumber , 100)
        while(carWinner(x)):
            newArr = randCarSpeed(carNumber)
            calcDistance(x,newArr)
            print(x)
        if(carBet == x.index(min(x))+1):
            player +=betAmount
        else:
            player -=betAmount
        print(player,x.index(min(x))+1)
        print("Want More Press yes")
        cont =input()

main()