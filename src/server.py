from flask import Flask, render_template, request
from flask_socketio import SocketIO
from .controller import InputController
import threading

class RemoteServer:
    def __init__(self, host='0.0.0.0', port=5000):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'secret!'
        self.socketio = SocketIO(self.app, cors_allowed_origins="*", async_mode='threading')
        self.host = host
        self.port = port
        self.controller = InputController()
        self.server_thread = None
        self.log_callback = None

        self._register_routes()
        self._register_socket_events()

    def _register_routes(self):
        @self.app.route('/')
        def index():
            return render_template('index.html')

    def _register_socket_events(self):
        @self.socketio.on('connect')
        def handle_connect():
            self.log(f'Client connected from {request.remote_addr}')

        @self.socketio.on('disconnect')
        def handle_disconnect():
            self.log('Client disconnected')

        @self.socketio.on('mousemove')
        def handle_mousemove(data):
            try:
                dx = data.get('dx', 0)
                dy = data.get('dy', 0)
                self.controller.move_mouse(dx, dy)
            except Exception as e:
                self.log(f"Error moving mouse: {e}")

        @self.socketio.on('mouseclick')
        def handle_mouseclick(data):
            try:
                btn = data.get('button')
                self.controller.click_mouse(btn)
            except Exception as e:
                self.log(f"Error clicking mouse: {e}")

        @self.socketio.on('scroll')
        def handle_scroll(data):
            try:
                dy = data.get('dy', 0)
                self.controller.scroll_mouse(dy)
            except Exception as e:
                self.log(f"Error scrolling: {e}")

    def log(self, message):
        if self.log_callback:
            self.log_callback(message)
        else:
            print(message)

    def set_log_callback(self, callback):
        self.log_callback = callback

    def run(self):
        self.socketio.run(self.app, host=self.host, port=self.port, allow_unsafe_werkzeug=True)

    def start(self):
        """Start the server in a separate thread."""
        self.server_thread = threading.Thread(target=self.run, daemon=True)
        self.server_thread.start()
