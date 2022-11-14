import random

numb1 = 0
numb2 =not numb1
count= 0
while(numb1!=numb2):
    numb1 = random.randrange(0,10000)
    numb2 = random.randrange(0,10000)
    print(numb1,numb2)
    count+=1

print(count)
