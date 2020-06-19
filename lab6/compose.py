def can_be_composed(word1, word2):
    lettersDict = dict()

    for char in word2:
        if(lettersDict.get(char) != None):
            lettersDict[char] += 1
        else:
            lettersDict[char] = 1

    for char in word1:
        if(lettersDict.get(char) != None and (lettersDict[char] - 1) >= 0):
            lettersDict[char] -= 1
        else:
            return False

    return True

# print(can_be_composed("dog", "god"))