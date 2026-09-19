import pyautogui
import time
import os

while True:
    x, y = pyautogui.position()
    print(f'({x}, {y})')
    time.sleep(0.1)
    os.system('cls')