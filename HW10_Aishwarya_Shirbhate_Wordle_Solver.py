# Homework Assignment 10
# from Aishwarya Shirbhate 20005242
import csv
from operator import itemgetter


class Wordle_Solver:
    def __init__(self, words):  # self function for taking in words
        self.words = words

    def find_words(self, clue, guess) -> list:
        # itemgetter returns a callable object that fetches item from its operand
        get_columns = itemgetter('rank', 'words')
        words = []
        res = []
        with open('wordRank.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile.readlines()[0:])
            [words.append(get_columns(row)) for row in reader]

        for rank, word in self.words:
            flag = True

            for i in range(5):
                if clue[i] == "\"":
                    if word[i] == guess[i]:
                        flag = False
                        break

                    instances = [i for i, ltr in enumerate(
                        guess) if ltr == guess[i]]
                    okCount = 0
                    for j in instances:
                        if clue[j] != "\"":
                            okCount += 1
                    instances = [i for i, ltr in enumerate(
                        word) if ltr == guess[i]]
                    if len(instances) > okCount:
                        flag = False
                        break
                elif clue[i] == " " and guess[i] != word[i]:
                    flag = False
                    break
                elif clue[i] == "`" and guess[i] not in word:
                    flag = False
                    break
                elif clue[i] == "`" and guess[i] == word[i]:
                    flag = False
                    break
            if flag:
                res.append((rank, word))

        return res
