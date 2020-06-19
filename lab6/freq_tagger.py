def most_common(inputDict):
    mostCommonTag = ""
    maxNumberOfTags = 0

    for key in inputDict:
        if(inputDict[key] > maxNumberOfTags):
            maxNumberOfTags = inputDict[key]
            mostCommonTag = key

    return mostCommonTag

def read_conllu(filePath):
    listOfTuples = []

    with open(filePath, "r") as openedFile:
        for line in openedFile:   
            if(line.strip() == ""):         
                continue
            
            splittedText = line.split()
            # print(splittedText)

            # if(splittedText[2] == "_"):
            oneLineTuple = (splittedText[1], splittedText[3])
            # else:
            #     print(splittedText)
            listOfTuples.append(oneLineTuple)
    
        # print(listOfTuples)
    return listOfTuples

def train_and_tag(train_file, test_words):

    listOfTuplesFromFile = read_conllu(train_file)
    listOfTegsForNecessaryWords = list()
    # print(listOfTuplesFromFile)

    for word in test_words:
        listOfTegsForNecessaryWords.append("UNK")

        for elementOfTuple in listOfTuplesFromFile:            
            if(word.lower() == elementOfTuple[0].lower()):
                # print(word.lower())
                # print(elementOfTuple[0].lower())
                del listOfTegsForNecessaryWords[-1]
                listOfTegsForNecessaryWords.append(elementOfTuple[1])
                # print(listOfTegsForNecessaryWords)
                break

    
    return listOfTegsForNecessaryWords


# train_and_tag("c:/Users/MacPavel/Desktop/pythonLabs/lab6/small_train.conllu", [ "The", "citizens", "hate", "weapons", "but", "love", "Christmas" ])
# read_conllu("c:/Users/MacPavel/Desktop/pythonLabs/lab6/en_gold.conllu")