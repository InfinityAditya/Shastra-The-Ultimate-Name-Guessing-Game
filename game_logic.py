import random

# Expanded word list for the guessing game
word_list = [
    "flask", "python", "hangman", "coding", "developer", 
    "algorithm", "software", "hardware", "machine", "learning", 
    "artificial", "intelligence", "database", "server", "network", 
    "programming", "debugging", "compiling", "technology", "cloud", 
    "data", "analytics", "AI", "ML", "robot", "automation", "devops", 
    "integrate", "deploy", "interface", "frontend", "backend"
]

def get_new_word():
    """Returns a new random word from the word list."""
    return random.choice(word_list)

def initialize_game():
    """Initializes the game state."""
    chosen_word = get_new_word()
    placeholder = "_ " * len(chosen_word)
    return {
        'chosen_word': chosen_word,
        'placeholder': placeholder,
        'lifes': 6,
        'store_prev': [],
        'game_over': False,
        'message': '',
    }

def make_guess(game_state, guess):
    """Handles the logic for making a guess."""
    chosen_word = game_state['chosen_word']
    store_prev = game_state['store_prev']
    lifes = game_state['lifes']
    placeholder = game_state['placeholder']

    if len(guess) != 1 or not guess.isalpha():
        return {"error": "Please enter a single valid letter."}

    if guess in store_prev:
        return {"error": "You already guessed this letter."}

    store_prev.append(guess)
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter + " "
        elif letter in store_prev:
            display += letter + " "
        else:
            display += "_ "

    game_state['placeholder'] = display.strip()

    if guess not in chosen_word:
        lifes -= 1

    game_state['lifes'] = lifes

    if lifes == 0:
        game_state['game_over'] = True
        game_state['message'] = "You lost! The word was: " + chosen_word
    elif "_" not in game_state['placeholder']:
        game_state['game_over'] = True
        game_state['message'] = "Congratulations! You won!"

    return game_state
