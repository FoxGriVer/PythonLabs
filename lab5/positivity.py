def positivize(review):

    reviewInSmallCase = review.lower()
    resultString = ""
    coursor = 0
    lastEdit = 0

    while(coursor < len(review) + 1):       

        if(reviewInSmallCase.find("bad", lastEdit, coursor) != -1):        
            if(review[reviewInSmallCase.find("bad", lastEdit, coursor)].islower()):
                editedPartOfString = review[lastEdit : coursor].replace("bad", "good")
            else:
                editedPartOfString = review[lastEdit : coursor].replace("Bad", "Good")

            notEditedPartOfString = review[coursor : len(review)]
            resultString += editedPartOfString
            lastEdit = coursor
        elif(reviewInSmallCase.find("horrible", lastEdit, coursor) != -1):        
            if(review[reviewInSmallCase.find("horrible", lastEdit, coursor)].islower()):
                editedPartOfString = review[lastEdit : coursor].replace("horrible", "fantastic")
            else:
                editedPartOfString = review[lastEdit : coursor].replace("Horrible", "Fantastic")

            notEditedPartOfString = review[coursor : len(review)]
            resultString += editedPartOfString
            lastEdit = coursor
        elif(reviewInSmallCase.find("dirty", lastEdit, coursor) != -1):        
            if(review[reviewInSmallCase.find("dirty", lastEdit, coursor)].islower()):
                editedPartOfString = review[lastEdit : coursor].replace("dirty", "clean")
            else:
                editedPartOfString = review[lastEdit : coursor].replace("Dirty", "Clean")

            notEditedPartOfString = review[coursor : len(review)]
            resultString += editedPartOfString
            lastEdit = coursor
        elif(reviewInSmallCase.find("disgusting", lastEdit, coursor) != -1):        
            if(review[reviewInSmallCase.find("disgusting", lastEdit, coursor)].islower()):
                editedPartOfString = review[lastEdit : coursor].replace("disgusting", "sublime")
            else:
                editedPartOfString = review[lastEdit : coursor].replace("Disgusting", "Sublime")

            notEditedPartOfString = review[coursor : len(review)]
            resultString += editedPartOfString
            lastEdit = coursor
        elif(reviewInSmallCase.find("expensive", lastEdit, coursor) != -1):        
            if(review[reviewInSmallCase.find("expensive", lastEdit, coursor)].islower()):
                editedPartOfString = review[lastEdit : coursor].replace("expensive", "affordable")
            else:
                editedPartOfString = review[lastEdit : coursor].replace("Expensive", "Affordable")

            notEditedPartOfString = review[coursor : len(review)]
            resultString += editedPartOfString
            lastEdit = coursor
        elif(reviewInSmallCase.find("moldy", lastEdit, coursor) != -1):       
            if(review[reviewInSmallCase.find("moldy", lastEdit, coursor)].islower()):
                editedPartOfString = review[lastEdit : coursor].replace("moldy", "flavourful")
            else:
                editedPartOfString = review[lastEdit : coursor].replace("Moldy", "Flavourful")

            notEditedPartOfString = review[coursor : len(review)]
            resultString += editedPartOfString
            lastEdit = coursor
        elif(reviewInSmallCase.find("frozen", lastEdit, coursor) != -1):        
            if(review[reviewInSmallCase.find("frozen", lastEdit, coursor)].islower()):
                editedPartOfString = review[lastEdit : coursor].replace("frozen", "farm-fresh")
            else:
                editedPartOfString = review[lastEdit : coursor].replace("Frozen", "Farm-fresh")

            notEditedPartOfString = review[coursor : len(review)]
            resultString += editedPartOfString
            lastEdit = coursor        

        coursor += 1

    resultString += review[lastEdit : coursor]

    if(resultString.find("minutes") != -1):
            positionOfWordMinutesInString = review.find("minutes")
            positionOfMinutes = positionOfWordMinutesInString - 2
            numberOfMinutes = ""

            while(review[positionOfMinutes].isnumeric()):
                numberOfMinutes += review[positionOfMinutes]
                positionOfMinutes -= 1        

            resultString = resultString.replace(numberOfMinutes[::-1], toFixed(int(numberOfMinutes[::-1])/2))

            positionOfWordMinutesInString = resultString.find("minutes")
            positionOfMinutes = positionOfWordMinutesInString - 2
            numberOfMinutes = ""

            while(resultString[positionOfMinutes].isnumeric()):
                numberOfMinutes += resultString[positionOfMinutes]
                positionOfMinutes -= 1                
        
            resultString = resultString[:positionOfMinutes] + " only" + resultString[positionOfMinutes : len(resultString)]
            
    if(review[0].islower()):
        resultString = resultString[0].lower() + resultString[1 : len(resultString)]
    else:
        resultString = resultString[0].upper() + resultString[1 : len(resultString)]

    return resultString

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

# positivize("We got disgusting mushrooms. And they prepared it for 16 minutes ! Moldy")