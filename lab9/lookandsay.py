def countSequence(number):
    resultSequance = ""

    repeat = number[0]
    number = number[1:] + " "
    times = 1
 
    for actual in number:
        if actual != repeat:
            resultSequance += str(times) + repeat
            times = 1
            repeat = actual
        else:
            times += 1
 
    return resultSequance

def S(n):
    sequence = "1"

    for iteration in range(n):
        sequence = countSequence(sequence)
    
    return int(sequence)

# print(S(5))