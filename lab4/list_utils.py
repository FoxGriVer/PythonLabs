def last(l):
    return l[-1]

def middle(l):
    try:
        if(len(l) % 2 == 0):
            raise Exception("Number of elements in the list is not odd")

        middleIndex = int((len(l) - 1)/2)

        return l[middleIndex]

    except Exception as e:
        print(e)    

def product(l):
    result = 1

    for element in l:
        result *= element

    return result

def even_sum(l):
    result = 0
    position = 0

    for element in l:
        if(position % 2 == 0):
            result += element

        position += 1

    return result
