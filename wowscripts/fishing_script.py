import pyautogui as gui
import cv2

IMAGE_FILE = 'wowscripts/lure_vale.png'
CASTS = 30
CONFIDENCE = .6
GRAYSCALE = True

def cast():
    """
    Casts the line and returns the box region of the lure
    """
    cast_icon = gui.locateCenterOnScreen('wowscripts/gofish_icon.png')
    gui.moveTo(cast_icon)
    gui.click()
    gui.PAUSE = 2.0
    return 

def catch(image):
    """
    takes a locateOnScreen object and clicks when the lure drops
    """
    location = gui.locateOnScreen(image, confidence=CONFIDENCE, grayscale = GRAYSCALE)
    if location == None:
        return
    print(location)
    counter = 30
    while gui.locateOnScreen(image, region=location, confidence=CONFIDENCE - .1, grayscale=GRAYSCALE) and counter > 0:
        print('no fish yet')
        counter -= 1
    gui.click( x=(location[0] + 40), y=(location[1] + 25) )
    if counter == 0:
        print('missed one!')
    return

def fish(image):
    counter = CASTS
    while counter > 0:
        print('Cast {}'.format(counter))
        cast()
        catch(image)
        counter -= 1

fish(IMAGE_FILE)

