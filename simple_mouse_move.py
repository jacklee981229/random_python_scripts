import pyautogui as auto
import random
import time

while True:
    x = random.randint(600,700)
    y = random.randint(200,600)
    auto.moveTo(x,y,0.2)
    time.sleep(1)
