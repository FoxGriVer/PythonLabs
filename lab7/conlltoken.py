class ConLLToken:

    def __init__(self, form, lemma, pos, morph):
        self.form = form
        self.lemma = lemma
        self.pos = pos
        self.morph = morph
    
    def __str__(self):
        return "{0},{1},{2},{3}".format(self.form, self.lemma, self.pos, self.morph)

    def is_punctuation(self):        
        return self.pos == "PUNCT"
    
    def is_inflected(self):
        return self.lemma.lower() != self.form.lower()

    def get_person(self):
        splitedLine = self.morph.split("|")

        for element in splitedLine:
            splitedElement = element.split("=")

            if(splitedElement[0] == "Person"):
                return splitedElement[1]
        
        return None

# collObj = ConLLToken("comes", "come", "VERB","Mood=Ind|Number=Sing|Person=3")
# print(str(collObj))
# print(collObj.get_person())