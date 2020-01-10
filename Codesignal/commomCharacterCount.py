def commonCharacterCount(s1, s2):
    lookup=set(s1).intersection(s2)
    res=[]
    for i in lookup:
        res.append(min(s1.count(i),s2.count(i)))
    return sum(res)
