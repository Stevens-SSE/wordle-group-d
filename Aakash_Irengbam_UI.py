import Aakash_Irengbam_Dictionary
class Length():
    def __init__(self, guess):
        self.guess = guess
    
    def __str__(self):
        return f"Length(guess:{str(self.guess)})"
        
    def WordLength(self):
        try:
            if(len(self.guess) == 0):
                return False
            else:
                return True
        except:
            print("Word length function not working")
    
class Correct():
    def __init__(self, guess, GuessedWordList):
        self.guess = guess
        self.GuessedWordList = GuessedWordList
    
    def __str__(self):
        return f"Length(guess:{str(self.guess,self.GuessedWordList)})"
        
    def GuessedWord(self):              #Check if the word has already been guessed
        try:
            if(self.guess in self.GuessedWordList):
                return True
            else:
                return False
        except:
            print("Guessed Word function not working")
        
class Author():
    def __init__(self, guess):
        self.guess = guess
    
    def __str__(self):
        return f"Length(guess:{str(self.guess)})"
    
    def AuthorizedWord(self):                            #To check if input has been according to the guidelines
        try:
            if((len(self.guess) > 5) or (len(self.guess) < 5) or (self.guess.isalpha() == False)):
                return True
            else:
                return False
        except:
            print("Authorized Word function not working")
    
class WordCorrect():
    def __init__(self, guess, RightWord):
        self.guess = guess
        self.RightWord = RightWord
    
    def __str__(self):
        return f"Length(guess:{str(self.guess,self.RightWord)})"
    
    def CorrectWord(self):                    #check if the entered word is correct
        try:
            if(self.guess == self.RightWord):
                return True
            else:
                return False
        except:
            print("Correct Word function not working")
    
    
def LoggingToFile(ToWrite,type):
    try:
        f = open("gameplay.log", "a+")
        f.write(f"{type}: {ToWrite}\n")
        f.close()
    except:
        print("LoggingToFile not working")

def CorrectPos(RightWord,guess):
    CorrectPosition = 0
    IncorrectGuess = 0
    IncorrectPosition = 0
    letter_counts: dict = {}
    appraisal = []

    for letter in RightWord:
        if letter in letter_counts.keys():
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

        for index in range(len(RightWord)):
            if guess[index] == RightWord[index]:
                appraisal.append(' ')
                letter_counts[RightWord[index]] -= 1
                CorrectPosition+=1
            else:
                appraisal.append('"')
                IncorrectGuess+=1

        for index in range(len(RightWord)):
            if guess[index] != RightWord[index]:
                if guess[index] in letter_counts:
                    if letter_counts[guess[index]] > 0:
                        letter_counts[guess[index]] -= 1
                        appraisal[index] = "'"
                        IncorrectPosition+=1

                    # print(" "*33 + ''.join(appraisal))
    return ''.join(appraisal)
    
class Interface():
    
    def __init__(self, RightWord):
          self.RightWord = RightWord
    
    def __str__(self):
        return f"Interface(RightWord:{str(self.RightWord)})"
          
    def userinterface(self):
    
        GuessedWordList = []     #To keep track of the words guessed by the user and notify if the same word has been guessed before
        attempt = 0
        CorrectPosition = 0
        IncorrectGuess = 0
        IncorrectPosition = 0
        Win = 0
        LoggingToFile(self.RightWord, "RightWord")
        while(attempt<6):         #To limit the number of attempts of the user to 6

            guess = input("Enter your 5 letter word guess:  ").lower()    #Take the input from the user
            LengthWord = Length(guess)
            Punt = Correct(guess, GuessedWordList)
            Authorised = Author(guess)
            WC = WordCorrect(guess, self.RightWord)
            if(LengthWord.WordLength() == False):
                quit()
            if(Punt.GuessedWord() == True):          
                print("This was a previous guess please try again")
            else:
                if((Authorised.AuthorizedWord() == True) or (Aakash_Irengbam_Dictionary.checking(guess) == False)):   #To check if input has been according to the guidelines
                    print("The input should be 5 letters and alphabets and in dictionary only")
                    continue
                elif (WC.CorrectWord() == True):           
                    print("This is the correct word")
                    Win+=1
                    break
                else:                              #to check the condtions on if and where the entered letter locations match with the correct word
                    letter_counts: dict = {}
                    appraisal = []

                    for letter in self.RightWord:
                        if letter in letter_counts.keys():
                            letter_counts[letter] += 1
                        else:
                            letter_counts[letter] = 1

                    for index in range(len(self.RightWord)):
                        if guess[index] == self.RightWord[index]:
                            appraisal.append(' ')
                            letter_counts[self.RightWord[index]] -= 1
                            CorrectPosition+=1
                        else:
                            appraisal.append('"')
                            IncorrectGuess+=1

                    for index in range(len(self.RightWord)):
                        if guess[index] != self.RightWord[index]:
                            if guess[index] in letter_counts:
                                if letter_counts[guess[index]] > 0:
                                    letter_counts[guess[index]] -= 1
                                    appraisal[index] = "'"
                                    IncorrectPosition+=1

                    print(" "*33 + ''.join(appraisal))
            attempt+=1
            GuessedWordList.append(guess)
            LoggingToFile(guess, "Guess")
            #WriteToFile(RightWord)
        else:                                                                #if the number of attempts have exceeded 6 enter the condition
            print("Failed in 6 tries no more tries left, try again next time")
        print("The game statistics were as follows:\n")
        print("Attempts: ", attempt, "\n")
        print("Incorrect position: ",IncorrectPosition, "\n")
        print("Correct position: ", CorrectPosition, "\n")
        print("Incorrect guess: ", IncorrectGuess, "\n")
        print("Win count", Win)
        LoggingToFile(attempt, "Attempt")
        LoggingToFile(Win, "Win")
        
    def userinterfaceSecond(self,betterguess):
    
        GuessedWordList = []     #To keep track of the words guessed by the user and notify if the same word has been guessed before
        # attempt = 0
        # CorrectPosition = 0
        # IncorrectGuess = 0
        # IncorrectPosition = 0
        # Win = 0
        # LoggingToFile(self.RightWord, "RightWord")
        # while(attempt<6):         #To limit the number of attempts of the user to 6
        appraisal = []
        guess = betterguess    #jhTake the input from the user
        LengthWord = Length(guess)
        Punt = Correct(guess, GuessedWordList)
        Authorised = Author(guess)
        WC = WordCorrect(guess, self.RightWord)
        if(LengthWord.WordLength() == False):
            quit()
        if(Punt.GuessedWord() == True):          
            print("This was a previous guess please try again")
        else:
            if((Authorised.AuthorizedWord() == True) or (Aakash_Irengbam_Dictionary.checking(guess) == False)):   #To check if input has been according to the guidelines
                print("The input should be 5 letters and alphabets and in dictionary only")
            elif (WC.CorrectWord() == True):           
                print("This is the correct word")
                quit()
            else:                              #to check the condtions on if and where the entered letter locations match with the correct word
                letter_counts: dict = {}
                appraisal = []

                for letter in self.RightWord:
                    if letter in letter_counts.keys():
                        letter_counts[letter] += 1
                    else:
                        letter_counts[letter] = 1

                for index in range(len(self.RightWord)):
                    if guess[index] == self.RightWord[index]:
                        appraisal.append(' ')
                        letter_counts[self.RightWord[index]] -= 1
                    else:
                        appraisal.append('"')

                for index in range(len(self.RightWord)):
                    if guess[index] != self.RightWord[index]:
                        if guess[index] in letter_counts:
                            if letter_counts[guess[index]] > 0:
                                letter_counts[guess[index]] -= 1
                                appraisal[index] = "'"

                    # print(" "*33 + ''.join(appraisal))
            # attempt+=1
        # GuessedWordList.append(guess)
        # LoggingToFile(guess, "Guess")
        return appraisal
            #WriteToFile(RightWord)
        # else:                                                                #if the number of attempts have exceeded 6 enter the condition
        #     print("Failed in 6 tries no more tries left, try again next time")
        # print("The game statistics were as follows:\n")
        # print("Attempts: ", attempt, "\n")
        # print("Incorrect position: ",IncorrectPosition, "\n")
        # print("Correct position: ", CorrectPosition, "\n")
        # print("Incorrect guess: ", IncorrectGuess, "\n")
        # print("Win count", Win)
        # LoggingToFile(attempt, "Attempt")
        # LoggingToFile(Win, "Win")