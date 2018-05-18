# Hangman game

# user supplies one guess-letter each round
# respond if it's there or not
# at the end of each round, return partially guessed word and remaining letters

# 8 guesses allowed
    # guess of same letter should not take away guess, instead print message
# lose guess ONLY when incorrect

# -----------------------------------
# Helper code

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
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

    # return 'hellou' # for testing
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    hold = []
    check = set(list(secretWord))
    for i in lettersGuessed:
        if i in secretWord:
            hold.append(i)
    if len(hold) == len(check):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    hold = ''
    for i in secretWord:
        if i in lettersGuessed:
            hold += i
        else:
            hold += '_ '
    return hold


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    all = string.ascii_lowercase
    for i in lettersGuessed:
        all = all.replace(i, '')
    return all

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
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is %i letters long.'%(len(secretWord)))

    sep = '-------------'
    guessed_letters = []
    guesses = 8

    def round():
        nonlocal guesses
        print(sep)
        print('You have %i guesses left.' % guesses)
        print('Available letters: %s'%(getAvailableLetters(guessed_letters)))
        u_input = input('Please guess a letter: ')
        if u_input.lower() in guessed_letters:
            print("Oops! You've already guessed that letter: %s"%(getGuessedWord(secretWord, guessed_letters)))
        else:
            guessed_letters.append(u_input)
            if u_input in secretWord:
                print('Good guess: %s'%(getGuessedWord(secretWord, guessed_letters)))
            else:
                print('Oops! That letter is not in my word: %s'%(getGuessedWord(secretWord, guessed_letters)))
                guesses -= 1

    while isWordGuessed(secretWord, guessed_letters) is False:
        if guesses is 0:
            print(sep)
            print('Sorry, you ran out of guesses. The word was %s'%secretWord)
            break
        else:
            round()
    else:
        print(sep)
        print('Congratulations, you won!')


if __name__ == '__main__':
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)
