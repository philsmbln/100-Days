import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_guess = []

while not game_over:
    guess = input('Guess a letter: ')

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_guess.append(guess)
        else:
            display += "_"
    print(display)

    if "_" not in display:
        game_over = True
        print('You win!')





