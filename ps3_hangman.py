# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '   '''
    x=list(secretWord)
    p=[]
    for i  in range (len( lettersGuessed)):
            k=  lettersGuessed[i] in x
            if k==True:
              p.append( lettersGuessed[i])
    for element in x:
        if element not in p[:]:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    x=list(secretWord)
    p=[]
    p2=""
    for i  in range (len( lettersGuessed)):
            k=  lettersGuessed[i] in x
            if k==True:
              p.append( lettersGuessed[i])
    for element in x:
        if element in p:
            p2=p2+element
        else:
            p2=p2+'_'
    if lettersGuessed[-1] in x:
        return ("good guess: ",p2)
    return ("Oops! That letter is not in my word: ",p2)
   
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    x=string.ascii_lowercase
    p=''
    for element in x:
        if element not in lettersGuessed:
            p=p+element
    return p

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print ("Welcome to the game - Hangman")
    print ("I am thinking of a ",len(secretWord)," letter word")
    x1=8
    lettersGuessed=[] 
    while x1 > 0:
        print ("you have ", x1 ," guesses left")
        print ("Available letters: ",getAvailableLetters(lettersGuessed))
        l1 = input("Please guess a letter: ")
        l1=l1.lower()
        if l1 in lettersGuessed:
            A,B= getGuessedWord(secretWord, lettersGuessed) 
            print ("Oops! You've already guessed that letter:",B)
            x1=x1+1
        else:
            lettersGuessed.append(l1)
            A,B= getGuessedWord(secretWord, lettersGuessed)        
            if A=="good guess: ":
                print (A,B)
                x1=x1+1
            else:
                print (A,B)
        x1=x1-1
        A1=isWordGuessed(secretWord, lettersGuessed)
        if A1==True and x1==0:
            print ("Congratulations, you won!")
            break
        elif A1==False and x1>0:
             continue
        else:
            print ("Sorry!You ran out of guesses.The word was ",secretWord)

hangman(chooseWord(wordlist))





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
