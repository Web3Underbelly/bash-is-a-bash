# main.py (Flask app)

from flask import Flask, render_template
from flask_socketio import SocketIO
from shell_emulator import spawn_shell, process_input

app = Flask(__name__)
app.config['SECRET_KEY'] = '…'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')  # serves React/xterm.js bundle

@socketio.on('pty_input')
def on_pty_input(data):
    child, screen, stream = spawn_shell()
    display = process_input(child, stream, data['input'])
    socketio.emit('pty_output', {'output': display})

if __name__ == '__main__':
    socketio.run(app)
