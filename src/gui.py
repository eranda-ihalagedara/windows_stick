import tkinter as tk
from tkinter import ttk, scrolledtext
from PIL import Image, ImageTk
from .server import RemoteServer
from .utils import get_local_ip, generate_qr_code
import threading

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Windows Remote Stick")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        # Initialize Server
        self.ip_address = get_local_ip()
        self.port = 5000
        self.server_url = f"http://{self.ip_address}:{self.port}"
        self.server = RemoteServer(host='0.0.0.0', port=self.port)
        self.server.set_log_callback(self.log_message)
        self.server_running = False

        self._create_widgets()

    def _create_widgets(self):
        # Header
        header_frame = ttk.Frame(self.root, padding=20)
        header_frame.pack(fill=tk.X)

        title_label = ttk.Label(header_frame, text="Windows Remote Stick", font=("Helvetica", 18, "bold"))
        title_label.pack()

        # QR Code Area
        self.qr_frame = ttk.Frame(self.root, padding=10)
        self.qr_frame.pack()

        self.qr_label = ttk.Label(self.qr_frame)
        self.qr_label.pack()
        
        # Generate initial QR code
        self.update_qr_code()

        url_label = ttk.Label(self.qr_frame, text=f"Connect to: {self.server_url}", font=("Consolas", 12))
        url_label.pack(pady=5)

        # Controls
        control_frame = ttk.Frame(self.root, padding=10)
        control_frame.pack(fill=tk.X)

        self.start_btn = ttk.Button(control_frame, text="Start Server", command=self.start_server, state=tk.NORMAL)
        self.start_btn.pack(side=tk.LEFT, expand=True, padx=5, fill=tk.X)

        self.stop_btn = ttk.Button(control_frame, text="Stop Server", command=self.stop_server, state=tk.DISABLED)
        # self.stop_btn.pack(side=tk.LEFT, expand=True, padx=5, fill=tk.X) # Flask-SocketIO is hard to stop cleanly, so disabling for now or making it just exit

        # Log Area
        log_frame = ttk.Frame(self.root, padding=10)
        log_frame.pack(fill=tk.BOTH, expand=True)

        log_label = ttk.Label(log_frame, text="Connection Logs:")
        log_label.pack(anchor=tk.W)

        self.log_text = scrolledtext.ScrolledText(log_frame, height=10, state=tk.DISABLED)
        self.log_text.pack(fill=tk.BOTH, expand=True)

    def update_qr_code(self):
        qr_img = generate_qr_code(self.server_url)
        # Resize for display
        qr_img = qr_img.resize((200, 200), Image.Resampling.LANCZOS)
        self.tk_qr_img = ImageTk.PhotoImage(qr_img)
        self.qr_label.config(image=self.tk_qr_img)

    def log_message(self, message):
        def _log():
            self.log_text.config(state=tk.NORMAL)
            self.log_text.insert(tk.END, message + "\n")
            self.log_text.see(tk.END)
            self.log_text.config(state=tk.DISABLED)
        self.root.after(0, _log)

    def start_server(self):
        if not self.server_running:
            self.log_message("Starting server...")
            self.server.start()
            self.server_running = True
            self.start_btn.config(state=tk.DISABLED)
            # self.stop_btn.config(state=tk.NORMAL) 
            self.log_message(f"Server running at {self.server_url}")

    def stop_server(self):
        # Stopping a Flask-SocketIO server gracefully from a thread is tricky.
        # For this version, we might just let it run or require restart.
        pass

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
