import pyautogui
import time

# Function to move mouse
def move_mouse(start_x, start_y, end_x, end_y, duration):
    # Move the mouse to the starting position
    pyautogui.moveTo(start_x, start_y, duration=0.5)
    time.sleep(1)  # Wait for 1 second

    # Move the mouse to the ending position
    pyautogui.moveTo(end_x, end_y, duration=duration)



def main():
    print("Moving that mouse.")
    # Define the coordinates and duration
    start_x, start_y = 100, 100  # Starting coordinates
    end_x, end_y = 100, 330      # Ending coordinates
    duration = 0.02                 # Duration in seconds

    # Move the mouse
    move_mouse(start_x, start_y, end_x, end_y, duration)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()

if __name__ == '__main__':
    main()