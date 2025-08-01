import pyautogui
import keyboard
import time
import PySimpleGUI

# python -i "$(FULL_CURRENT_PATH)"

# int position_x
# int position_y
# return position_x, position_y
def get_pos():
    position_x, position_y = pyautogui.position()
    return position_x, position_y
    

def amountToClick(x, y):
    pyautogui.click(x,y)


def main():
    run = True
    print("Please input what key you want to start the process" )
    pressed_key = keyboard.read_key()
    print(f"Using key {pressed_key}, press esc to exit")
    while run == True:
        if keyboard.is_pressed(pressed_key):
            x,y = get_pos()
            amountToClick(x,y)
        elif keyboard.is_pressed('esc'):
            run = False
        

main()