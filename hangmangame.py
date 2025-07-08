from random import randint
import dictionary
from hangman import hangman_list

while True:
    starter = input("""
Do you want to start new game?
    [y] - yes     [n] - no
""")
    if starter == 'n' or starter == 'no':
        print('Okay! Good Bye...')
        break
    elif starter == 'y' or starter == 'yes':
        while True:
            level = input("""
            There are 3 levels of game, choose which you will play:
            -Easy
            -Medium
            -Hard
            """).lower()

            if level == 'easy':
                word = dictionary.easy_words[randint(0, len(dictionary.easy_words))]
                break
            elif level == 'medium':
                word = dictionary.medium_words[randint(0, len(dictionary.medium_words))]
                break
            elif level == 'hard':
                word = dictionary.hard_words[randint(0, len(dictionary.hard_words))]
                break
            else:
                print("You chose incorrect option, repeat please!")
                continue
    else:
        print("You chose incorrect option, repeat please!")
        continue
    state = 0
    word_letters = [i for i in word]
    word_state = ["_" for i in word_letters]
    incorrect_list = []
    
    while True:
        print(hangman_list[state])
        if state == 6:
            print("You lost :(")
            print(f"The word was: {word}")
            break
        elif word_letters == word_state:
            print("You won!")
            break
        print(f"Word: {"".join(word_state)}")
        print(f"Mistakes: {state}")
        letter = input("Enter a letter: ").lower()

        if letter.isalpha() != True or len(letter) != 1:
            continue
        elif letter not in word_letters:
            if letter not in incorrect_list:
                incorrect_list.append(letter)
                state += 1
            else:
                continue
        else:
            indexes = [i for i in range(0, len(word_letters)) if word_letters[i] == letter]
            for i in range(0,len(word_state)):
                if i in indexes:
                    word_state[i] = letter