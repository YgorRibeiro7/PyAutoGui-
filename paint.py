import pyautogui
import time 
import pandas


pyautogui.PAUSE = 1



pyautogui.press("win")

pyautogui.write("bloco de notas")
pyautogui.press("enter")
# pyautogui.moveTo( x=349, y=410, duratiHeon=5) 
pyautogui.dragTo(x=94, y=167, duration= 0.5) 
# pyautogui.moveRel(x=349, y=410, duration=1) 
# pyautogui.click(x=400, y=510, clicks=1, interval=0, button='right')
# pyautogui.click(x=369, y=415, clicks=3, interval=2, button='left')
# pyautogui.click(x=409, y=420, clicks=3, interval=2, button='left')
pyautogui.click(x=474, y=297)
# pyautogui.typewrite('Hello world!\n', interval=0.3) 
pyautogui.click(x=24, y=121)


# pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter'], interva=1)
# pyautogui.click(x=349, y=410)
# distance = 200
# while distance > 0:
#         pyautogui.drag(distance, 0, duration=0.5)   # move right
#         distance -= 5
#         pyautogui.drag(0, distance, duration=0.5)   # move down
#         pyautogui.drag(-distance, 0, duration=0.5)  # move left
#         distance -= 5
#         pyautogui.drag(0, -distance, duration=0.5)  # move up

        
        
        