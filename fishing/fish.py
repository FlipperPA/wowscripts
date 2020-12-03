from datetime import datetime, timedelta
import os
from time import sleep

import pyautogui as gui
from pyscreenshot import grab

IMAGE_FILE = os.path.join("lure.png")
CASTS = 500
CONFIDENCE = 0.6
GRAYSCALE = False

# Tweak the threshold depending on the background.
THRESHOLD = 20

# Tweak the iterations depending on how fast your machine can screen capture.
ITERATIONS = 90

def cast():
    """
    Casts the line and returns the box region of the lure
    """
    cast_icon = gui.locateCenterOnScreen(
        os.path.join("fish_icon.png"),
        confidence=0.6,
    )

    if cast_icon is None:
        print("Could not find the fishing icon on screen. Casting again.")

        return

    gui.moveTo(cast_icon)
    gui.click()
    sleep(2)

    return


def find_lure(image):
    """
    Attempts to find the lure by image.
    """
    start = datetime.now()

    print("Finding the lure... ")
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
            return None

    print(f"Found lure at location: {location}...")

    return location


def catch(location):
    """
    takes a locateOnScreen object and clicks when the lure drops
    """
    capture_region = (
        location.x - 10,
        location.y - 10,
        location.x + 10,
        location.y + 10,
    )
    original_image = grab(bbox=capture_region)

    start = datetime.now()

    print(f"Watching location ({location.x}, {location.y})...")

    for x in range(0, ITERATIONS):
        current_image = grab(bbox=capture_region)

        pairs = zip(original_image.getdata(), current_image.getdata())
        if len(original_image.getbands()) == 1:
            # for gray-scale jpegs
            dif = sum(abs(p1 - p2) for p1, p2 in pairs)
        else:
            dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))

        ncomponents = original_image.size[0] * original_image.size[1] * 3
        diff_pct = (dif / 255.0 * 100) / ncomponents
        print(f"{x} Difference (percentage): {diff_pct}")

        if diff_pct > THRESHOLD:
            gui.moveTo(location)
            gui.rightClick()
            sleep(1.0)
            print("We caught a fish!")
            return

    print("Hmmm, we didn't detect a change in the bobber.")
    return


def fish(image):
    for counter in range(1, CASTS + 1):
        print(f"Cast {counter}")
        cast()
        location = find_lure(image)

        if location:
            catch(location)


fish(IMAGE_FILE)
