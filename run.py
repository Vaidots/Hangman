import random
from words import words
from hangman_visual import lives_visual_dict
import string


def welcome_user():
  
    username = None

    while True:

        username = input('Enter your name\n')   # Lets user write his name

        if not username.isalpha():  # Has to be alphabetic character
            print('Username must be alphabets only')
            continue
        else:
            print('welcome '+username)
            break


print('Welcome to Hangman')
welcome_user()


def get_valid_word(words):
   
    word = random.choice(words)  # randomly chooses word from the list

    return word.upper()     # Word come back capital letters


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left')
        print('You alreadyy used these letters: ', ' '.join(used_letters))

        # what current word is 
        output = [letter if letter in used_letters else '_' for letter in word]
        print(lives_visual_dict[lives])
        print('The Current word: ', ' '.join(output))

        user_letter = input('\nGuess a lette r: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('Congratulations! the word is', word, '!!') 
  

# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules


if __name__ == '__main__': 
    hangman()
    

