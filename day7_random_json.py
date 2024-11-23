import random

# Step-1: Picking a random word and checking answers
# Randomly chosen word from the word list
from day7 import word_list


# Functionality choice, it chooses from the list
chosen_word = random.choice(word_list)  
print(chosen_word)

placeholder = ""
length_chosen_word = len(chosen_word)
for i in range(1, length_chosen_word + 1):
    placeholder += "_ "

print(placeholder)

store_prev = []
game_over = False
lifes = 6

while not game_over:
    # User guessing a letter
    guess = input("Guess a letter: ").lower()

    # Step-2: Replacing blanks with guesses
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            store_prev.append(guess)
            
        elif letter in store_prev:
            display += letter
        else:
            display += "_ "
    if lifes==6:
        print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')

    if guess not in chosen_word:
        lifes -= 1

        if lifes == 5:
            print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')

        if lifes == 4:
            print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')

        if lifes == 3:
            print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')

        if lifes == 2:
            print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')

        if lifes == 1:
            print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')

        if lifes == 0:
            print("\n\n**You Lost !!**")
            print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')
            game_over=True

    print(display)

    if "_" not in display:
        game_over = True
        print("***You Win!!***")
