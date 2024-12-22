import pyautogui
screen_width,screen_height=pyautogui.size()
print(f'the screen width is {screen_width} and the screen height is {screen_height}')
# pyautogui.moveTo(100,200) #moving mouse to specific screen coordinate x,y
# pyautogui.moveRel(50,50) #moving the mouse relative to current position
# pyautogui.click(30,50) #default is current position, x,y value clicks on the specific coordinate
# pyautogui.rightClick()
# pyautogui.doubleClick()
# pyautogui.moveTo(100,100)
# pyautogui.dragTo(100,200,2) # x,y,duration
pyautogui.write("hello world", 0.000000000000001)
