from typing import List
from LinkedList import Node
from LinkedList import SLinkedList


class Helper:

    # Function to return the best likely word as per the provided good,bad and positional letters
    def help(good_letters: str, bad_letters: str, new_answer: str, entered_words: List) -> str:

        goodWords = good_letters.upper()

        if len(goodWords) > 5:
            raise Exception("You can have only 5 maximum good letters")

        goodWords = list(goodWords.strip())

        badWords = bad_letters.upper()

        badWords = list(badWords.strip())

        if any(x in goodWords for x in badWords):
            raise Exception('WARNING : A letter cannot be both good and bad!')

        positionWords = new_answer.upper()
        if len(positionWords) != 0:
            if len(positionWords) != 5:
                raise Exception(
                    'WARNING : Word should be of length 5 or empty')

        if not all(x.isalpha() or x.isspace() for x in positionWords):
            raise Exception(
                'WARNING : Please enter a word containing only Alphabets or Spaces.')

        try:
            fs = open("wordRank.csv", "r")
            next(fs)

            wordlist = []
            tentative = []

            for x in fs:
                wordlist.append(x[0:5])

            # If user does not provide Good or bad words, then return the top rated word
            if len(goodWords) == 0 and len(badWords) == 0:
                return wordlist[0]

            for x in wordlist:
                goodflag = True
                badFlag = True
                for y in goodWords:
                    if y not in x:
                        goodflag = False
                        break
                for z in badWords:
                    if z in x:
                        badFlag = False

                if goodflag and badFlag:
                    tentative.append(x)

            finalWords = tentative[:]

            if(len(positionWords) == 5):
                for x in tentative:
                    for index in range(5):
                        if positionWords[index] != " " and positionWords[index] != x[index]:
                            finalWords.remove(x)
                            break

            fs.close()
        except IOError:
            print('An error occured trying to read the file.')
            print(
                'Please make sure "wordRank.csv" is present in the directory before running the program')
            quit()

        for word in entered_words:
            if word in finalWords:
                finalWords.remove(word)

        return finalWords[0]
