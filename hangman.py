

def test(wordSlice,word,wordCheker):
    count = 0
    for i in wordSlice:
        for j in range(len(word)):
            if(i==word[j]):
                wordCheker[j]=count
        count+=1
    
def test2(wordCheker,wordAsChar):
    newArray= ""
    for i in range(len(wordCheker)):
        if(type(wordCheker[i])==str):
            newArray+="_"

        else:
            newArray+=wordAsChar[i]
    return newArray
def test1(word,wordSlice,pInp,):
    for i in word :
        if(i==pInp):
            wordSlice.append(pInp)
            break

def main():
    word = "pythonjavascript"
    wordSlice = ["s"]
    wordAsChar=[c for c in word]
    wordCheker=wordAsChar[:]
    test(wordSlice,word,wordCheker)
    print(test2(wordCheker,wordAsChar))
    test1(word,wordSlice,"a")
    test(wordSlice,word,wordCheker)
    print(test2(wordCheker,wordAsChar))



    

 




main()