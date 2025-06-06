from flask import Flask, render_template, request, jsonify
from game_logic import get_computer_choice, get_result

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    player = data['player']
    computer = get_computer_choice()
    result = get_result(player, computer)
    return jsonify({"player": player, "computer": computer, "result": result})

if __name__ == '__main__':
    app.run(debug=True)
