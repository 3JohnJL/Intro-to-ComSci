def getvalues(data,value):
    values=[]
    for i in range(len(data)):
        if data[i].count(value.lower())>1 or data[i].count(value.upper())>1:
            values.append(data[i])
    return values