import string
from words import choose_word
from images import IMAGES
'''
Important instruction
* function and variable name snake_case -> is_prime
* contant variable upper case PI
'''

def is_word_guessed(secret_word, letters_guessed):
    for letters in letters_guessed:
        if letters in secret_word:
            secret_word = secret_word.replace(letters, "")
        if len(secret_word) == 0:
            return True
    return False


# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    '''
    letters_left = string.ascii_lowercase
    for s in letters_guessed:
        letters_left = letters_left.replace(s,"")
    return letters_left

def image_show(lives):
    print(IMAGES[lives])

def is_valid(guess, available_letters):
    if len(guess) == 1 and guess in available_letters:
        return True
    return False

def hangman(secret_word):
    '''
    secret_word (string) : secret word to guessed by the user.
    Steps to start Hangman:
    * In the beginning of the game user will know about the total characters in the secret_word    
    * In each round user will guess one character 
    * After each character give feedback to the user
      * right or wrong
    * Display partial word guessed by the user and use underscore in place of not guess word    
    '''
    total_lives = 8
    lives = 0
    flag = False
    letters_guessed = []
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(str(len(secret_word))), end='\n\n')
    
    while(lives < total_lives):
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {} ".format(available_letters))

        guess = input("Please guess a letter: ")
        letter = guess.lower()

        if guess == "hint" and not flag:
            flag = True
            for s in secret_word:
                if s not in letters_guessed:
                    print("Hint: ",s)
                    letters_guessed.append(s)
                    print("Good guess: {} ".format(get_guessed_word(secret_word, letters_guessed)))
                    if is_word_guessed(secret_word, letters_guessed) == True:
                        print(" * * Congratulations, you won! * * ", end='\n\n')
                        break
                    break
            continue

        elif guess == "hint" and flag:
            print("You can use Hint only 1 time")

        if is_valid(guess, available_letters) == False:
            print("Sorry, the input is invalid. Please Try Again !", "\n")
            continue

        if letter in secret_word:
            letters_guessed.append(letter)
            print("Good guess: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            if is_word_guessed(secret_word, letters_guessed) == True:
                print(" * * Congratulations, you won! * * ", end='\n\n')
        else:
            print("Oops! That letter is not in my word: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            letters_guessed.append(letter)
            print("")
            image_show(lives)
            lives += 1
            remain_lives = total_lives - lives
            print("Lives Remaining : ",str(remain_lives))
            if(remain_lives == 0):
                print("Sorry, out of lives better luck next time")


# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
print(secret_word)
hangman(secret_word)