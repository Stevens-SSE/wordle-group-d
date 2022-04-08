import HW03_Aakash_Irengbam_Dictionary as dict   #import the other modules to use their functions
import HW03_Aakash_Irengbam_UI as UI
import WordleHelper as help



Rnd = dict.randomword()
UI = UI.Interface(Rnd)
def Solver(Betterattempts):
    BadLetters = []
    GoodLetters = []
    AutoGuessedList = []

    initialguess = 'sales'
    BetterGuessList = []
    BetterGuess = ''
    BufferGuess = ''
    i = 0
    
    
    while(Betterattempts<6):
            Pos = UI.userinterfaceSecond(initialguess)
            if(Pos[0] == ' ' and Pos[1] == ' ' and Pos[2] == ' ' and Pos[3] == ' ' and Pos[4] == ' '):
                print("This is the correct word")
            i = 0
            while (i < 5):
                #BufferGuess = BetterGuessList[Betterattempts-1]
                if(Pos[i] == " " or Pos[i] == "'") and not GoodLetters.__contains__(initialguess[i]):
                    GoodLetters.append(initialguess[i])
                else:
                    if not BadLetters.__contains__(initialguess[i]):
                        BadLetters.append(initialguess[i])
                i+=1
            j = 0
            BadLetters_Copy = BadLetters.copy()
            while(j < len(BadLetters_Copy)):
                if(GoodLetters.__contains__(BadLetters_Copy[j])):
                    BadLetters.remove(BadLetters_Copy[j])
                j += 1
            BufferList = help.rankedWords(GoodLetters,BadLetters)
            #BetterGuessList.append(initialguess)
            if(len(BufferList) > 0):
                initialguess = BufferList[0]
            Betterattempts+=1
            if(Betterattempts == 6):
                print("Failed to solve Wordle") 
Solver(0)     
            