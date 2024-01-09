import pyautogui
import time

def fullFunction():
    # Move the mouse to a specific position
    print("moveTo100,10")
    pyautogui.moveTo(100, 100, duration=1)

    # Move the mouse relative to the current position
    print("moveTo - 50,50")
    pyautogui.move(0, 0, duration=1)

    # Slowly move the mouse back to the starting position
    print("moveTo 800,400")
    pyautogui.moveTo(800, 800, duration=1)

    # You can also perform clicks
    # pyautogui.click()

    # Add a delay to see the movements
    time.sleep(2)

    # Double click
    pyautogui.doubleClick()

    # Right click
    print("rightclick")
    # pyautogui.rightClick()

    # Move the mouse to a specific position and click
    print("moveTo & Click")
    # pyautogui.moveTo(200, 200, duration=1)
    # pyautogui.click()

    # Drag the mouse
    print("moveTo & Click 1000,1200")
    pyautogui.moveTo(700, 1200, duration=1)
    pyautogui.click()
    # pyautogui.dragTo(800, 800, duration=1)

    # You can get the current mouse position
    current_position = pyautogui.position()
    print(f"Current mouse position: {current_position}")
    time.sleep(3)
i=0
while True:
    print(f"i value=> {i}")
    fullFunction()
    i+=1

print("program exited")
