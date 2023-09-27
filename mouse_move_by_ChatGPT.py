import pyautogui as auto
import random
import time

# Define the movement area as the active window
screen_width, screen_height = auto.size()
active_window = auto.getWindowsWithTitle(auto.getActiveWindowTitle())[0]
window_pos_x, window_pos_y = active_window.topleft
window_width, window_height = active_window.size
movement_area = (window_pos_x, window_pos_y, window_width, window_height)

# Define a list of movement paths
movement_paths = [
    [(movement_area[0]+movement_area[2])//2, movement_area[1]],
    [movement_area[0], (movement_area[1]+movement_area[3])//2],
    [(movement_area[0]+movement_area[2])//2, movement_area[1]+movement_area[3]],
    [movement_area[0]+movement_area[2], (movement_area[1]+movement_area[3])//2],
]

try:
    while True:
        # Randomly select a movement path
        movement_path = random.choice(movement_paths)

        # Add some noise to the movement coordinates
        noise = random.randint(-10, 10)
        x = movement_path[0] + noise
        y = movement_path[1] + noise

        # Move the mouse cursor to the new coordinates with a random delay
        auto.moveTo(x, y, random.uniform(0.2, 0.5))

        # Wait for a random delay before the next movement
        time.sleep(random.uniform(0.5, 2.0))

except KeyboardInterrupt:
    print('Script stopped by user.')
