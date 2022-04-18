import random
import os
import string

from numpy import array


try:
    f = open("/Users/aakashirengbam/Downloads/words.txt", "r")       #open the text file
    wordlist = f.read()                                              #read the text file
    wordslist = wordlist.split("\n")
    f.close()
except IOError:
            print('An error occured trying to read the file.')
            print('Please make sure "words.txt" is present in the directory before running the program')
            quit()
            
try:
    f = open("wordListNew.txt", "w")
    for x in wordslist:
        if len(x) == 5:                                              #only read text file if the length of the letter is 5 words
            #newList.append(x.lower())
            f.write(f"{x.lower()}\n")
    f.close()
except IOError:
            print('An error occured trying to read the file.')
            print('Please make sure "wordListNew.txt" is present in the directory before running the program')
            quit()
            
try:
    f = open("wordListNew.txt", "r")
    content = f.read()
    newList = content.split("\n")
except IOError:
            print('An error occured trying to read the file.')
            print('Please make sure "wordListNew.txt" is present in the directory before running the program')
            quit()

        
        
def randomword() -> str:                                                #choose a random word from the dictionary 
    try:
        RightWord = random.choice(newList)    
        return RightWord
    except:
        print("Randomword function not working")

def checking(y) -> bool:                                                # check if the user entered word exists in the dictionary
    try:
        if y in newList:
            return True
        else:
            return False
    except:
        print("checking not working")
    
def removeWord(word) -> None:                                          #removes a word from the list
    with open("wordListNew.txt", "r") as f:
        lines = f.readlines()
    with open("wordListNew.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != word:
                f.write(line)
    if(fileStatus()):
        resetWords()

def resetWords() -> None:                  #Checks whether the word already exists in the list
    try:
        f = open("wordListNew.txt", "w")
        f.write(newList)
        f.close()
    except:
        print("Reset function not working")
        
def fileStatus() -> None:                   #Checks whether the list has values in it or not
    if(os.stat("wordListNew.txt").st_size == 0):
        return True
    else:
        return False
