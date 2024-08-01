import pygetwindow as gw
from pynput import keyboard
from screeninfo import get_monitors

for m in get_monitors():
    monitor_width = m.width
    monitor_height = m.height

def on_press(key):
    if key == keyboard.Key.shift:
        active_window = gw.getActiveWindow()
        x = (monitor_width // 2) - (active_window.width // 2)
        y = (monitor_height // 2) - (active_window.height // 2)
        active_window.moveTo(x, y)

def on_release(key):
    if key == keyboard.Key.shift:
        print("bye")

with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
