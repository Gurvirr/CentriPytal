import pygetwindow as gw
from pynput import keyboard
from screeninfo import get_monitors

for m in get_monitors():
    width = int(m.width)
    height = int(m.height)

def on_press(key):
    if key == keyboard.Key.shift:
        active_window = gw.getActiveWindow()
        print(active_window)
        active_window.moveTo(width // 2, height // 2)

def on_release(key):
    if key == keyboard.Key.shift:
        print("bye")

with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
