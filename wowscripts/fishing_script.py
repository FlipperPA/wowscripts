from datetime import datetime, timedelta
import os

import pyautogui as gui
import cv2

IMAGE_FILE = os.path.join("wowscripts", "lure_shadowlands.png")
CASTS = 500
CONFIDENCE = 0.6
GRAYSCALE = False


def cast():
    """
    Casts the line and returns the box region of the lure
    """
    cast_icon = gui.locateCenterOnScreen(
        os.path.join("wowscripts", "gofish_icon.png"),
        confidence=0.6,
    )

    if cast_icon is None:
        print("Could not find the fishing icon on screen. Casting again.")

        return

    gui.moveTo(cast_icon)
    gui.click()

    return


def catch(image):
    """
    takes a locateOnScreen object and clicks when the lure drops
    """
    start = datetime.now()

    print("Watching for lure bob... ")
    location = None
    counter = 0

    while location is None:
        counter += 1
        print(counter, end="... ")
        location = gui.locateCenterOnScreen(
            image, confidence=CONFIDENCE, grayscale=GRAYSCALE
        )
        if datetime.now() > start + timedelta(seconds=30):
            print("Breaking, no image found!")
            return

    print(f"Found one at location: {location}...")

    gui.moveTo(location)
    gui.click()

    return


def fish(image):
    for counter in range(1, CASTS + 1):
        print(f"Cast {counter}")
        cast()
        catch(image)


fish(IMAGE_FILE)
