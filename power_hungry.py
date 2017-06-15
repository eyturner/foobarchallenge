def multList(list):
    answer = 1
    for item in list:
        answer *= item
    return answer

#list of negative numbers - make biggest positive number possible!
def bigNeg(Nlist):
    Nlist.sort()
    Nlist.reverse()
    test = multList(Nlist)
    if(test < 0):
        test /= (Nlist[0])
    return int(test)

def answer(xs):
    tempAns = 0
    ans = 1
    negList = []
    if(len(xs) == 1):
        return xs[0]
    for item in xs:
        if(item > 0):
            ans *= item
            tempAns -= 1
        elif(item < 0):
            negList.append(item)
    addOn = bigNeg(negList)
    ans *= addOn
    if(tempAns < 0):
        return ans
    else:
        return 0
