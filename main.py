from PIL import ImageGrab
import pyautogui, time

x = 0
y = 0
green = (75, 219, 106)

time.sleep(5)

pyautogui.click(x, y)

while True:
    px = ImageGrab.grab().load()
    color = px[x, y]
    if color == green:
        pyautogui.click(x, y)
        time.sleep(1)
        pyautogui.click(x, y)