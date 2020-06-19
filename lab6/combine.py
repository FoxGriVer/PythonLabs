def combine_dict(d1, d2):
    resultDitct = dict()

    resultDitct = d1.copy()
    resultDitct.update(d2)

    for key in resultDitct:
        if(d1.get(key) != None and d2.get(key) != None):           
            resultDitct[key] = d1[key] + d2[key]

    return resultDitct

# d1 = { "a" : 10, "b" : 1, "c" : 15 }
# d2 = { "a" : 1, "c" : 2, "d" : 20 }


# print(combine_def(d1, d2))
            