import pyautogui
from PIL import Image, ImageGrab
from time import sleep
# from numpy import asarray

def isCollide(data):
    for i in range(234, 345):
                for j in range(415, 457):
                    if data[i, j] < 100:
                        return True
                    # data[i, j] = 0
    # return False

def hit(key):
    pyautogui.keyDown(key)

if __name__ == '__main__':
    print("Hey... Dino game is about to start in 5 seconds.")
    sleep(5)
    hit('up')
    while True:
        img = ImageGrab.grab().convert('L')
        data = img.load()
        # print(asarray(img))
        if isCollide(data):
            hit('up')
        isCollide(data)
    # img.show()
