from pynput.mouse import Button, Controller as MouseController
import logging

# Disable pynput logging to avoid spam
logging.getLogger("pynput").setLevel(logging.WARNING)

class InputController:
    def __init__(self):
        self.mouse = MouseController()
    
    def move_mouse(self, dx, dy):
        """Move the mouse by dx, dy."""
        try:
            self.mouse.move(dx, dy)
        except Exception as e:
            print(f"Error moving mouse: {e}")

    def click_mouse(self, button_name):
        """Click a mouse button ('left' or 'right')."""
        try:
            if button_name == 'left':
                self.mouse.click(Button.left)
            elif button_name == 'right':
                self.mouse.click(Button.right)
        except Exception as e:
            print(f"Error clicking mouse: {e}")

    def scroll_mouse(self, dy):
        """Scroll the mouse vertically."""
        try:
            self.mouse.scroll(0, dy)
        except Exception as e:
            print(f"Error scrolling: {e}")
