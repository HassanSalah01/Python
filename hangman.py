strArr = []
solution = []
word = "python"

for i in word:
    strArr.append(i)


print(strArr)
def isRight(word,wChar):
    for i in word:
        if(i==wChar):
            solution.append(i)
            break

def lines(word,wChar):
    str =""
    for i in range(len(word)):
        if(word[i]==wChar):
            str+=word[i]
        else:
            str+="_"
    print(str)

def main():
    # game start 
    #take Input
    #check turn 
    #Check Char 
    #return ---- word


lines("python","o")
lines("python","p")

