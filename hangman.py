word = "hassan"

z = ["s","a"]
wordAsChar=[c for c in word]
wordCheker=wordAsChar[:]

# print(arr1)
# print(arr2)
def test():
    count = 0
    for i in z:
        for j in range(len(word)):
            if(i==word[j]):
                wordCheker[j]=count
        count+=1
    return count

print(wordAsChar)
def main():
    

    print(wordCheker)
    sss= ""
    for i in range(len(wordCheker)):
    
        # print(type(i))
        if(type(wordCheker[i])==str):
            # print("strrrrrrrr")
            sss+="_"

        else:
            sss+=wordAsChar[i]

    print(sss)




main()


















#  for i in x :
#         for j in z:
#             # print(i,j)
#             if(i==j):
#                 arr2.append(i)
#             else:
#                  arr2.append("-")
#     print(arr2)