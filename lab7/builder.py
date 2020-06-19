from conlltoken import *

class ConLLUTokenBuilder:    

    def buildToken(self, line):
        splitedLine = line.split()

        conllToken = ConLLToken(splitedLine[1], splitedLine[2], splitedLine[3], splitedLine[5])    

        return conllToken


class ConLL09TokenBuilder:

    def buildToken(self, line):
        splitedLine = line.split()

        conll09Token = ConLLToken(splitedLine[1], splitedLine[2], splitedLine[4], splitedLine[6])

        return conll09Token

conllUBuilder = ConLLUTokenBuilder()
testObj = conllUBuilder.buildToken("1 The the DET _ Definite=Def|PronType=Art _ _ _ _")
print(type(testObj))
