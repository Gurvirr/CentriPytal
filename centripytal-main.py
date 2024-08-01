import pygetwindow as gw
from pynput import keyboard
from screeninfo import get_monitors

def on_press(key):
    if key == keyboard.Key.shift:
        active_window = gw.getActiveWindow()
        monitor = get_monitors()[0]
        x = (monitor.width // 2) - (active_window.width // 2)
        y = (monitor.height // 2) - (active_window.height // 2)
        active_window.moveTo(x, y)

with keyboard.Listener(on_press = on_press) as listener:
    listener.join()