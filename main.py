import pyautogui
import time

# Text to be typed
textType = "Have an idea to create a script which simulate typing and inputting stored text "

# Delay before starting typing (gives you time to focus on the input field)
time.sleep(5)

# Type out the text
pyautogui.write(textType, interval=0.1)  # You can adjust the interval between key presses
pyautogui.press('enter')
