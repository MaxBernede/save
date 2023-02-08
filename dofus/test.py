import pyautogui as pg
import time
import cv2
import os

imageOffset = 25

def checkfrene1():
    try:
        file_name = os.path.join(os.path.dirname(__file__), 'frene.jpg')
        assert os.path.exists(file_name)
        img = cv2.imread(file_name, -1)

        pos = pg.locateOnScreen(img,confidence=0.8)
        pg.moveTo(pos[0]+imageOffset,pos[1]+imageOffset)
        pg.click()
        time.sleep(1)
        checkfrene1()
    except:
        print("No Frene1")
        checkfrene2()
        im1 = pg.screenshot()

def checkfrene2():
    try:
        file_name = os.path.join(os.path.dirname(__file__), 'frene2.jpg')
        assert os.path.exists(file_name)
        img = cv2.imread(file_name, -1)

        pos = pg.locateOnScreen(img,confidence=0.8)
        pg.moveTo(pos[0]+imageOffset,pos[1]+imageOffset)
        pg.click()
        time.sleep(1)
        checkfrene2()
    except:
        print("No Frene2")
        checkfrene3()
        im1 = pg.screenshot()

def checkfrene3():
    try:
        file_name = os.path.join(os.path.dirname(__file__), 'frene3.jpg')
        assert os.path.exists(file_name)
        img = cv2.imread(file_name, -1)

        pos = pg.locateOnScreen(img,confidence=0.8)
        pg.moveTo(pos[0]+imageOffset,pos[1]+imageOffset)
        pg.click()
        time.sleep(1)
        checkfrene3()
    except:
        print("No Frene3")
        im1 = pg.screenshot()

checkfrene1()