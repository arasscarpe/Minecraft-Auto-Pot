import time
import random
import pyautogui
from pynput import keyboard

pyautogui.FAILSAFE = True  

def random_delay():
    return random.uniform(0.08, 0.14)

def right_click_once():
    time.sleep(random_delay())
    pyautogui.click(button="right")

def on_press(key):
    try:
        if key.char in ['2', '3', '4', '5', '6']: #Sizin Pot Koyduğunuz Tuşlar Hangisiyse Bu Satırdan Değiştirebilirsiniz
            right_click_once()
    except AttributeError:
        pass

print("discord: https://discord.gg/2Kvh2kFSvr :D")
print("Made By FlaxyPasha")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
