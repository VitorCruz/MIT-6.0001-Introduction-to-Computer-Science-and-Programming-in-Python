

# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"    
       
    for i in secret_word:
        if i not in letters_guessed:
            return False
    
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    word = ''
    for i in secret_word:
        if i not in letters_guessed:
            word += '_ '
        else:
            word += i
    
    return word
            
            
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    all_letters = string.ascii_lowercase
    avaliable_letters = []
    
    for i in all_letters:
        if i not in letters_guessed:
            avaliable_letters.append(i)
        
    return avaliable_letters    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
       
    letters = len(secret_word)    
    number_of_guesses = 6
    letter_guessed = []   
    warnings = 3
    vowels = ['a','e','i','o','u']
    unique_letters = len(list(set(secret_word)))
    
    print("")
    print("Welcome to the game Hangman! ")    
    print(f"The secret word have {letters} letters.")
    print(f"You have {number_of_guesses} avaliable guesses, choose wisely.")
    
    while number_of_guesses > 0:
        available_letters = get_available_letters(letter_guessed)
        print("Available letters: ",available_letters) 
        ## another while loop to get letters only in available letters  
        print("SECRET WORD SO FAR: ",get_guessed_word(secret_word,letter_guessed))
        print("")
        print("--------------------------------------------------")
        
        letter_guess = input("Guess a letter from the available list: ").lower()
        
        while letter_guess not in available_letters:
            if warnings > 0:
                warnings -= 1
            else:
                number_of_guesses -= 1
                print("You lost one guess.")  
                print(f"You still have {number_of_guesses} more guesses") 
            if number_of_guesses == 0:
                break
            print(f"WARNING! Choose a valid letter. You have {warnings} more warnings.")
            letter_guess = input("Choose an available letter: ").lower()             
        letter_guessed.append(letter_guess)
        
        if is_word_guessed(secret_word, letter_guessed):
            print("")
            print("")
            print("YOU WON!")
            print("The secret word is:",secret_word)
            print("Your score is:", number_of_guesses * unique_letters)
            break        
        
        if letter_guess in secret_word:
            print("Good job! Right choice.")
            print(f"You still have {number_of_guesses} more guesses")   
        
        if letter_guess not in secret_word:
            print("Wrong letter.")            
            #lose an aditional guess for wrong vowels
            if letter_guess in vowels:
                number_of_guesses -= 1
            number_of_guesses -= 1
            if number_of_guesses == 0:
                print("No more guesses. YOU LOSE.") 
                print("The secret word was actually:",secret_word)
                break
            print(f"You have {number_of_guesses} more guesses")          
        

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word, letters_guessed, available_letters):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    if len(my_word) != len(other_word):
        return False
    
    for i in range(0, len(my_word)):
        if my_word[i] != '_' and my_word[i] != other_word[i]:
            return False     
        if my_word[i] == '_' and other_word[i] in letters_guessed:
            return 
        if my_word[i] == '_' and other_word[i] not in available_letters:
            return False   
    
    return True


def show_possible_matches(my_word, letters_guessed, available_letters):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
     
    for i in wordlist:
        if match_with_gaps(my_word, i, letters_guessed, available_letters):
            print(i)
            

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
   
    letters = len(secret_word)    
    number_of_guesses = 6
    letters_guessed = []   
    warnings = 3
    vowels = ['a','e','i','o','u']
    unique_letters = len(list(set(secret_word)))
    
    print("")
    print("Welcome to the game Hangman! ")    
    print(f"The secret word have {letters} letters.")
    print(f"You have {number_of_guesses} avaliable guesses, choose wisely.")
    
    while number_of_guesses > 0:
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: ",available_letters) 
        ## another while loop to get letters only in available letters  
        print("SECRET WORD SO FAR: ",get_guessed_word(secret_word,letters_guessed))
        print("")
        print("--------------------------------------------------")
        
        letter_guess = input("Guess a letter from the available list: ").lower()
        
        while letter_guess not in available_letters:
            if letter_guess == '*':
                user_word_with_no_spaces = get_guessed_word(secret_word,letters_guessed).replace(' ', '')
                print("")
                print("HINT!")
                print("Possible combination of words:")
                show_possible_matches(user_word_with_no_spaces, letters_guessed, available_letters)
                break
            if warnings > 0:
                warnings -= 1
            else:
                number_of_guesses -= 1
                print("You lost one guess.")  
                print(f"You still have {number_of_guesses} more guesses") 
            if number_of_guesses == 0:
                break
            print(f"WARNING! Choose a valid letter. You have {warnings} more warnings.")
            letter_guess = input("Choose an available letter: ").lower()             
        letters_guessed.append(letter_guess)   
        
        if is_word_guessed(secret_word, letters_guessed):
            print("")
            print("")
            print("YOU WON!")
            print("The secret word is:",secret_word)
            print("Your score is:", number_of_guesses * unique_letters)
            break        
        
        if letter_guess in secret_word:
            print("Good job! Right choice.")
            print(f"You still have {number_of_guesses} more guesses")   
        
        if letter_guess not in secret_word and letter_guess != '*':
            print("Wrong letter.")            
            #lose an aditional guess for wrong vowels
            if letter_guess in vowels:
                number_of_guesses -= 1
            number_of_guesses -= 1
            if number_of_guesses == 0:
                print("No more guesses. YOU LOSE.") 
                print("The secret word was actually:",secret_word)
                break
            print(f"You have {number_of_guesses} more guesses")  



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.    
   
    #secret_word = choose_word(wordlist)    
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
