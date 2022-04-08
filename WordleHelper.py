import csv
rankDict = {}
with open('wordRank.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        rankDict[row[0].split(',')[0]] = row[1].split(',')[0]
rankDict.pop('Rank')


def rankedWords(correctLetters, incorrectLetters):
    myList = []
    defaultList = []
    if correctLetters == None and incorrectLetters == None:
        for i in range(1,51):
            defaultList.append(rankDict[str(i)])
        return defaultList
    if correctLetters != None:
        for key in range(1,len(rankDict)):
            flag = 0
            for letter in correctLetters:
                if letter not in rankDict[str(key)]:
                    flag = 1
            if flag == 0:
                myList.append(rankDict[str(key)])
    else:
        for key in rankDict:
            myList.append(rankDict[key])
    newList = myList.copy()
    if incorrectLetters != None:
        for word in myList:
            flag = 0
            for letter in incorrectLetters:
                if letter in word:
                    flag = 1
            if flag == 1:
                newList.remove(word)
    return newList

#Checking to see if the function is working right
# print(rankedWords([],['s','a','l','e']))