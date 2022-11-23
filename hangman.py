

def labelChar(wordSlice,word,wordCheker):
    count = 0
    for i in wordSlice:
        for j in range(len(word)):
            if(i==word[j]):
                wordCheker[j]=count
        count+=1
    
def showingWord(wordCheker,wordAsChar):
    newArray= ""
    for i in range(len(wordCheker)):
        if(type(wordCheker[i])==str):
            newArray+="_"
        else:
            newArray+=wordAsChar[i]
    return newArray

def isCharRight(word,wordSlice,pInp,):
    for i in word :
        if(i==pInp):
            wordSlice.append(pInp)
            return True
    return False

def main():
    word = "pythonjavascript"
    wordSlice = ["s"]
    wordAsChar=[c for c in word]
    wordCheker=wordAsChar[:]
    playerTrun = 3
    while(playerTrun):
        x = input()
        if(isCharRight(word,wordSlice,x)):
            labelChar(wordSlice,word,wordCheker)
            print(showingWord(wordCheker,wordAsChar))
        else:
            playerTrun-=1
            print("Wrong Input")
main()