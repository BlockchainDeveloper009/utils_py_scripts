import pyautogui
import time

class xyCoordinates:
    def __init__(self,x,y):
        self.x = x;
        self.y = y;

def fullFunction(timeIntervalBetweenCursorMove):
    msTeamsXY = xyCoordinates(700, 1200)
    eightHundredByEighHundredXY = xyCoordinates(800, 800)
    appCoordinateLocation = {
        "msTeamsXY":msTeamsXY,
    "eightHundredByEighHundredXY":eightHundredByEighHundredXY}
    # Move the mouse to a specific position
    print("moveTo100,10")
    pyautogui.moveTo(100, 100, duration=1)

    # Move the mouse relative to the current position
    print("moveTo - 50,50")
    pyautogui.move(0, 0, duration=1)

    # Slowly move the mouse back to the starting position
    print(f'moveTo {appCoordinateLocation["eightHundredByEighHundredXY"].x},{appCoordinateLocation["eightHundredByEighHundredXY"].y}')
    pyautogui.moveTo(appCoordinateLocation["eightHundredByEighHundredXY"].x, appCoordinateLocation["eightHundredByEighHundredXY"].y, duration=1)
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

    print("moveTo & Click 700,1200")
    pyautogui.moveTo(appCoordinateLocation["msTeamsXY"].x, appCoordinateLocation["msTeamsXY"].y, duration=1)
    pyautogui.click()
    # pyautogui.dragTo(800, 800, duration=1)

    # You can get the current mouse position
    current_position = pyautogui.position()
    print(f"Current mouse position: {current_position} - {timeIntervalBetweenCursorMove}")
    time.sleep(timeIntervalBetweenCursorMove)
i=0
while True:
    print(f"i value=> {i}")

    fullFunction(5)
    i+=1

print("program exited")
