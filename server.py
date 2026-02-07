from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from pynput.mouse import Button, Controller as MouseController
import socket
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

mouse = MouseController()

# Disable pynput logging to avoid spam
logging.getLogger("pynput").setLevel(logging.WARNING)

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    print(f'Client connected from {request.remote_addr}')

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@socketio.on('mousemove')
def handle_mousemove(data):
    try:
        dx = data.get('dx', 0)
        dy = data.get('dy', 0)
        # Sensitivity multiplier could be added here
        mouse.move(dx, dy)
    except Exception as e:
        print(f"Error moving mouse: {e}")

@socketio.on('mouseclick')
def handle_mouseclick(data):
    try:
        btn = data.get('button')
        if btn == 'left':
            mouse.click(Button.left)
        elif btn == 'right':
            mouse.click(Button.right)
    except Exception as e:
        print(f"Error clicking mouse: {e}")



@socketio.on('scroll')
def handle_scroll(data):
    try:
        dy = data.get('dy', 0)
        mouse.scroll(0, dy)
    except Exception as e:
        print(f"Error scrolling: {e}")

if __name__ == '__main__':
    ip = get_local_ip()
    print(f"Starting server on http://{ip}:5000")
    socketio.run(app, host='0.0.0.0', port=5000)
