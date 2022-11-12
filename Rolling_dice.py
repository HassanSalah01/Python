import sys
import random

def main():
    x = ""
    for i in range(int(sys.argv[1])):
        x+=str(random.randrange(0,6))+" "
    print(x)



main()
