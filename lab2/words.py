def enterWords():
    word = None
    words = list()

    while (word != "done"):
        try:
            word = input("Enter a word: ")

            if(word == ""):
                raise Exception("Entered value is empty")
            
            if(word != "done"):
                # print("{} added in a dictionary".format(word))
                words.append(word.lower())
            # else:
            #     print("End of adding words")
        except Exception as e:
            print(e)

    # print(words)
    return words

def printFirstAndLastWords(words):
    print("{} comes first in the dictionary".format(min(words)))
    print("{} comes last in the dictionary".format(max(words)))

words = enterWords()
printFirstAndLastWords(words)

    