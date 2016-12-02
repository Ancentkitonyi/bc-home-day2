def wordcount(data):
    wordcount= {}
    for word in data.split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    return wordcount
print wordcount("olly olly in come free")

