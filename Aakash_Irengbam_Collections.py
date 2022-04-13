import csv
import string
import Aakash_Irengbam_Dictionary as dic
letter_occurence = dict( (key, [0,0,0,0,0]) for key in string.ascii_lowercase )
def alphabet_likely():
    f = open("wordListNew.txt", "r")
    content = f.read()
    WordsList = content.split('\n')
    f.close()
    for word in WordsList:
        count = 0
        for letter in word:
            letter_occurence[letter][count] += 1
            count+=1
    
    flag = 0
    for word in WordsList:
        flag += 1
    for letter in string.ascii_lowercase:
        for i in range(5):
            letter_occurence[letter][i] = round((letter_occurence[letter][i] / flag),5)

    f = open("letterFrequency.csv", 'w')
    f.write("letter,first_pos, second_pos, third_pos, fourth_pos, fifth_pos \n")
    for letter in string.ascii_lowercase:
        f.write(f"{letter}, {letter_occurence[letter][0]}, {letter_occurence[letter][1]}, {letter_occurence[letter][2]}, {letter_occurence[letter][3]}, {letter_occurence[letter][4]}\n")
    f.close()

def Convert_To_tuple(dic):
    for key in dic.keys():
        dic[key] = tuple(dic[key])

def ParseToTuples():
    f = open("letterFrequency.csv", 'r')
    content = f.read()
    tempList = content.split('\n')
    myDict = {}
    for line in range(1,len(tempList)):
        temp = tempList[line].split(", ")
        if len(temp[0]) != 0:
            myDict[temp[0]] = (temp[1],temp[2],temp[3],temp[4],temp[5])
    return myDict
        
def occur_likely():
    f = open("wordListNew.txt", "r")
    content = f.read()
    WordsList = content.split('\n')
    f.close()
    occur_like = {}
    for word in WordsList:
        if checkLen(word):
            occurence_likelihood = float(letter_occurence[word[0]][0]) * float(letter_occurence[word[1]][1]) * float(letter_occurence[word[2]][2]) * float(letter_occurence[word[3]][3]) * float(letter_occurence[word[4]][4])
            occur_like[word] = occurence_likelihood

    sorted_list = sorted(occur_like.items(), key=lambda x:x[1])
    sorted_list.reverse()
    f = open("wordRank.csv", 'w')
    f.write("Rank, Word, Likelihood \n")
    flag = 1
    for word in sorted_list:
        f.write(f"{flag}, {word[0]}, {word[1]}\n")
        flag += 1
    f.close()
    
def checkLen(word):
    if len(word) != 0:
        return True
    else:
        return False

