def checkLeapYear(inputYear):

    if((inputYear % 4) != 0):
        print("{0} is not a leap year".format(inputYear))
    elif ((inputYear % 100) == 0):
        if((inputYear % 400) == 0):
            print("{0} is a leap year".format(inputYear))
        else:
            print("{0} is not a leap year".format(inputYear))
    else:
        print("{0} is a leap year".format(inputYear))

def enterIntValue():
    value = None

    while (type(value) is not int) or (value < 0):
        try:
            value = int(input("Enter a year A.D.(positive int value): "))
            if(value < 0):
                raise Exception("Entered value is not positive")
            else:
                return value            
        except ValueError:
            print("Entered value is not int")
        except Exception as e:
            print(e)

year = enterIntValue()
checkLeapYear(year)
