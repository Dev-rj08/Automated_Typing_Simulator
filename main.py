import pyautogui
import pyperclip
import time

# Get the text from the clipboard
copied_text = pyperclip.paste()

# Get the current cursor position
cursor_x, cursor_y = pyautogui.position()

# Time to move cursor to the desired location
time.sleep(5)

# Simulate clicking at the cursor position
pyautogui.click(cursor_x, cursor_y)

# Simulate typing the copied text
pyautogui.write(copied_text, interval=0.1)  # You can adjust the interval between key presses

# Press Enter key
pyautogui.press('enter')
