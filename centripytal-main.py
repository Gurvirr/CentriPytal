import pygetwindow as gw
from pynput import keyboard

def on_press(key):
    if key == key.shift:
        active_window = gw.getActiveWindow()
        active_window.minimize()

def on_release(key):
    if key == key.shift:
        print("bye")
        
with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
