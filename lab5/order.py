def sort(words):
    position = 1

    while position < len(words):
        for dif in range(len(words) - position):
            if(words[dif] > words[dif + 1]):
                words[dif], words[dif + 1] = words[dif + 1], words[dif]
        position += 1
    
    return words