def checkio(words):
    str1 =str.lower(words)
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    print (dict)
    d3={v:k for k,v in dict.items()}
    return d3[max(d3)]
