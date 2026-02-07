# Windows Remote Stick

A lightweight, Python-based remote control application that transforms your mobile device into a wireless trackpad for your Windows PC.

## 🚀 Features

- **Large Trackpad Area**: Dedicated space for smooth mouse movement control.
- **Mouse Buttons**: Large Left (L) and Right (R) click buttons.
- **Scroll Strip**: Vertical strip for easy page scrolling.
- **Wi-Fi Connectivity**: Connect over your local network without cables.
- **Real-time Interaction**: Powered by Flask-SocketIO for low-latency control.
- **Connection Logs**: Server-side notifications when clients connect or disconnect.

## 📋 Prerequisites

- Python 3.7+
- A mobile device on the same local network as your PC.

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd windows_stick
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Usage

1. Start the server:
   ```bash
   python server.py
   ```

2. Look at the console output to find the local IP address (e.g., `http://192.168.1.5:5000`).

3. Open the browser on your mobile device and navigate to that address.

4. **Control your PC**:
   - **Move**: Touch and drag on the trackpad area.
   - **Click**: Tap the 'L' or 'R' buttons.
   - **Scroll**: Use the vertical 'Scroll' strip on the right side of the trackpad.

## 🧰 Built With

- **Backend**: [Flask](https://flask.palletsprojects.com/), [Flask-SocketIO](https://flask-socketio.readthedocs.io/), [pynput](https://pynput.readthedocs.io/)
- **Frontend**: HTML5, CSS3 (Flexbox), Vanilla JavaScript
- **Communication**: WebSockets via Socket.io

## 📝 License

This project is open-source. Feel free to modify and adapt it for your needs.
