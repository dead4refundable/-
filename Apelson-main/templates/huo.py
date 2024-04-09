from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/game', methods=['POST'])
def start_game():
    player_name = request.form['name']
    return redirect(url_for('play_game', name=player_name))


@app.route('/game', methods=['GET'])
def play_game():
    return render_template('play_game.html')


@app.route('/play_pygame')
def play_pygame():
    # Запускаем игру в Pygame с помощью subprocess.Popen
    subprocess.Popen(['python', 'Apelson.py'])
    # После запуска игры, делаем редирект обратно на главную страницу или на любую другую страницу
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)