# Windows Remote Stick (Professional Edition)

A robust, Python-based remote control application that transforms your mobile device into a wireless trackpad for your Windows PC. Now featuring a graphical user interface and simplified connection via QR code.

## 🚀 Features

- **GUI Control Panel**: Easy-to-use desktop interface to start/stop the server.
- **QR Code Connection**: Scan a QR code to instantly connect your mobile device.
- **Large Trackpad Area**: Dedicated space for smooth mouse movement control.
- **Mouse Buttons**: Large Left (L) and Right (R) click buttons.
- **Scroll Strip**: Vertical strip for easy page scrolling.
- **Wi-Fi Connectivity**: Connect over your local network without cables.
- **Real-time Interaction**: Powered by Flask-SocketIO for low-latency control.

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

1. Start the application:
   ```bash
   python run.py
   ```

2. The **Windows Remote Stick** window will open.
3. Click **Start Server**.
4. Scan the **QR Code** with your mobile device, or manually enter the URL displayed.
5. **Control your PC**:
   - **Move**: Touch and drag on the trackpad area.
   - **Click**: Tap the 'L' or 'R' buttons.
   - **Scroll**: Use the vertical 'Scroll' strip on the right side of the trackpad.

## 🧰 Built With

- **Backend**: [Flask](https://flask.palletsprojects.com/), [Flask-SocketIO](https://flask-socketio.readthedocs.io/), [pynput](https://pynput.readthedocs.io/)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **GUI**: Tkinter, [Pillow](https://python-pillow.org/)
- **Utilities**: [qrcode](https://github.com/lincolnloop/python-qrcode)

## 📝 License

This project is open-source. Feel free to modify and adapt it for your needs.
