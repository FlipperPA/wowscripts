import pyautogui as gui
import cv2


def cast():
    """
    Casts the line and returns the box region of the lure
    """
    cast_icon = gui.locateCenterOnScreen('wow/gofish_icon.png')
    gui.moveTo(cast_icon)
    gui.click()
    gui.PAUSE = 2.0
    return 

def catch(image):
    """
    takes a locateOnScreen object and clicks when the lure drops
    """
    location = gui.locateOnScreen(image, confidence=0.5)
    while location == None:
        location = gui.locateOnScreen(image, confidence=0.5)
    print(location)
    counter = 30
    while gui.locateOnScreen(image, region=location, confidence=0.5) and counter > 0:
        print('no fish yet')
        counter -= 1
    gui.click( x=(location[0] + 40), y=(location[1] + 25) )
    return

def fish(image):
    counter = 10
    while counter > 0:
        cast()
        catch(image)
        counter -= 1

fish('wow/lure_front')
