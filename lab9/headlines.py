from big_letters import *

def build_headline(inputText):
    letters = list(inputText)
    bigLettersStringList = ["", "", "", "", ""]
    bigLettersString = ""

    for letter in letters:

        headLineLetter = get_letter(letter.upper()).split('\n')

        bigLettersStringList[0] += headLineLetter[0]
        bigLettersStringList[1] += headLineLetter[1]
        bigLettersStringList[2] += headLineLetter[2]
        bigLettersStringList[3] += headLineLetter[3]
        bigLettersStringList[4] += headLineLetter[4]

        bigLettersString = "\n".join(bigLettersStringList)
    
    return bigLettersString

# print(build_headline("It snows"))