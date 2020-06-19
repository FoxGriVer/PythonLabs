def rotated(lst, n):
    
    reversedLst = []
    resultLst = []

    if(len(lst) == 0):
        return []
    
    numberOfSymbolsForRotation = n % len(lst)        

    for i in range(numberOfSymbolsForRotation):
        reversedLst.append(lst[i]) 
    
    for i in range(numberOfSymbolsForRotation, len(lst)):
        resultLst.append(lst[i])

    resultLst += reversedLst

    return resultLst


