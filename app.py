from flask import Flask, render_template, request, jsonify
from game_logic import initialize_game, make_guess

app = Flask(__name__)

# Store the game state
game_state = initialize_game()

# Home route that renders the game
@app.route('/')
def index():
    return render_template('index.html', 
                           placeholder=game_state['placeholder'], 
                           lifes=game_state['lifes'],
                           message=game_state['message'])

# Handle the guess route
@app.route('/guess', methods=['POST'])
def guess():
    global game_state
    guess = request.form['guess'].lower()

    # Update the game state after the guess
    game_state = make_guess(game_state, guess)

    if 'error' in game_state:
        return jsonify({'error': game_state['error']})

    return jsonify({
        'lifes': game_state['lifes'],
        'placeholder': game_state['placeholder'],
        'game_over': game_state['game_over'],
        'message': game_state['message']
    })

# Restart the game route
@app.route('/restart', methods=['POST'])
def restart():
    global game_state
    game_state = initialize_game()  # Restart the game
    return jsonify({
        'lifes': game_state['lifes'],
        'placeholder': game_state['placeholder'],
        'game_over': game_state['game_over'],
        'message': game_state['message']
    })

if __name__ == '__main__':
    app.run(debug=True)
