import pyautogui, time
from PIL import ImageGrab

time.sleep(5)

position = pyautogui.position()

print(position)

px = ImageGrab.grab().load()
color = px[position]
print(f'green = {color}')