import random as rand

from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

lives = 6

chosen_word = rand.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
guess_letter = []

while not game_over:

    print(f'*********** {lives}/6 Lives Left **********')
    guess = input("Guess a letter: ").lower()

    while len(guess) != 1 or not guess.isalpha():
        guess = input("Please only choose one letter from (a-z): ").lower()

    if guess in guess_letter:
        print(f'You\'ve guess letter \'{guess}\' already!')
    elif guess not in chosen_word:
        lives -= 1
        guess_letter.append(guess)
        print(f'Letter \'{guess}\' is not in the word, you lose a life.')
    else:
        guess_letter.append(guess)

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            guess_letter.append(guess)
        elif letter in guess_letter:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if lives == 0:
        game_over = True
        print(f'Correct word: {chosen_word}')
        print(f"You Lose, Game Over")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
