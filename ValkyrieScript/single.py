import pyautogui
import time
def onclick(picture):
    point = pyautogui.locateCenterOnScreen(
            picture, confidence=0.8, grayscale=True)
    if point is None:
        print("Not found")
        exit()
    x, y = point
    pyautogui.click(x, y)

def isVictory():
    point = pyautogui.locateCenterOnScreen(
            'images/victory.png', confidence=0.8, grayscale=True)
    if point is None:
         return False
    else:
        print("Is victory")
        x, y = point
        pyautogui.click(x, y)
        return True

if __name__ == "__main__":
    count = 0
    time_start = time.time()
    while True:
        while True:
            if(isVictory()):
                time_end = time.time()
                time.sleep(2)
                break
        print("Count: {}, Runtime: {}".format(count, time_end - time_start))
        onclick('images/restart.png')
        time.sleep(2)
        onclick('images/again.png')
        time.sleep(2)
        count += 1        

