import random
def gameLoop():
    x = random.randrange(0,10)
    print(x)
    playerTurn = 3 
    while(playerTurn):
        playerInput = int(input())
        if(playerInput==x):
            print("You Guessed The Right Number")
            break
        else:
            playerTurn-=1
            if(playerTurn==0):
                print("GameOver If You Want To Try Again Press Y Elese Press N")
                tryAgain = input()
                if(tryAgain == "Y"):
                    gameLoop()
                else:
                    exit()
            else:
                print("Try Again")        

def main():
    gameLoop()

main()

