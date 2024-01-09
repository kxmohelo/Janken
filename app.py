from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Draw !", computer_choice
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You win !", computer_choice
    else:
        return "Computer wins !", computer_choice

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.json['choice']
    computer_choice = get_computer_choice()

    result, computer_choice = determine_winner(user_choice, computer_choice)
    return jsonify({"user_choice": user_choice, "computer_choice": computer_choice, "result": result})

if __name__ == '__main__':
    app.run(debug=True)
