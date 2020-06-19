from fragments import *

def easy_password(length):    
    numberOfSymbolsIsPossible = length
    finallPassword = ""

    try:
        if(length <= 1):
            raise Exception("Entered value is not positive")

        while(numberOfSymbolsIsPossible != 0):
            if(numberOfSymbolsIsPossible <= 1):
                return easy_password(length)
                
            if(numberOfSymbolsIsPossible <= 3):
                finallPassword += generateFragmentWithThreeOrLessSymbols(numberOfSymbolsIsPossible)
                return finallPassword

            oneFragment = get_random_text()

            finallPassword += oneFragment
            numberOfSymbolsIsPossible -= len(oneFragment)

        return finallPassword
        
    except Exception as e:
        print(e)

def generateFragmentWithThreeOrLessSymbols(requiredLength):
    fragmentWithThreeOrLessSymbols = False

    while(not fragmentWithThreeOrLessSymbols):
        oneFragment = get_random_text()

        if(len(oneFragment) == requiredLength):
            fragmentWithThreeOrLessSymbols = True
            return oneFragment

# password = easy_password(1000)
# print(password)

