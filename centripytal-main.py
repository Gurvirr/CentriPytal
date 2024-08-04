import pywinctl as pwc
import time
from pynput import keyboard
from screeninfo import get_monitors

key_presses = 0
first_press = time.time()

def on_press(key):
    global key_presses, first_press

    last_press = time.time()

    if last_press - first_press > 1:
        key_presses = 0
    
    if key == keyboard.Key.shift:
        first_press = last_press
        key_presses += 1
    
    if key_presses == 3:
        active_window = pwc.getActiveWindow()
        monitor = get_monitors()[0]
        x = (monitor.width // 2) - (active_window.width // 2)
        y = (monitor.height // 2) - (active_window.height // 2)
        active_window.moveTo(x, y)
        key_presses = 0

with keyboard.Listener(on_press = on_press) as listener:
    listener.join()