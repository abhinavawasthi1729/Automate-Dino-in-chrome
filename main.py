import pyautogui
from PIL import Image, ImageGrab
import time

def screenshot():
    image = ImageGrab.grab().convert('L')
    return image
    

def hit(key):
    pyautogui.keyDown(key)

def iscollideCactus(data):
    for i in range(220,250):
        for j in range(400,470):
            if data[i,j] < 100:
                return True
    return False

def iscollideBird(data):
    for i in range(190,210):
        for j in range(315,395):
            if data[i,j] < 100:
                return True
    return False

if __name__=="__main__":
    time.sleep(3)
    hit("up")
    while True:
        image = screenshot()
        data = image.load()
        if iscollideCactus(data):
            hit("up")
        if iscollideBird(data):
            hit("down")

        #this is bird region
        # for i in range(190,210):
        #     for j in range(315,395):
        #          data[i,j] = 0

        # for i in range(220,250):
        #     for j in range(400,470):
        #         data[i,j] = 0

        # image.show()
        
        # break


            
       

    


