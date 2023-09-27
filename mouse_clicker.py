import pyautogui as auto
import time
from pynput.keyboard import *

#  ======== settings ========
delay = 0.001  # in seconds
resume_key = Key.f1
pause_key = Key.f2
exit_key = Key.esc
#  ==========================

# Global flag to control the right_click function
pause = True
running = True

def on_press(key):
    global running, pause
    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exited]")

def display_controls():
    print("// AutoClicker by iSayChris")
    print("// - Settings: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("// - Controls:")
    print("\t F1 = Resume")
    print("\t F2 = Pause")
    print("\t Esc = Exit")
    print("-----------------------------------------------------")
    print('Press F1 to start ...')
    
def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            auto.rightClick(auto.position())
            auto.PAUSE = delay
    lis.stop()


if __name__ == "__main__":
    main()