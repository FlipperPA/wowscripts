# wowscripts
Using pyautogui to automate different repetitive tasks in World of Warcraft MMORPG. Make anything. Save lifetimes.

### First set up a pyautogui virtual environment and install dependencies

```python
python3 -m venv pyautogui_venv
. pyautogui_venv/bin/activate
pip install pyautogui ipython numpy==1.19.3 pillow
```
### Run ipython and imports

```python
ipython
import pyautogui
import cv2
```

### You're ready to run the script!
In case you don't normally use ipython (I didn't) I'll explain a few shortcuts here using the fishing script as an example.

## Fishing Script
The fishing script works by locating relevant images on the screen and then interacting with them in the appropriate manner. 

There are three functions. cast() relies on the fishing icon, which I have enclosed as a png. This should be the same for everyone as long as you have the fishing action on one of your action bars.

You can just copy and paste this function into ipython no problem.

catch(image) ... has a catch.

the function relies on images to run. It takes an image file location pointing to a small screenshot of the lure (I use the smallest frame around the lure itself for this ((you can see plenty of example .pngs included)). The function then looks for this image on the screen after the cast. It uses a certain confidence level to allow for approximate images to count. Then, after it finds the lure position, it starts to probe this specific frame on the screen until the image no longer matches as well (like when it sinks and splashes because a fish struck). pyautogui then clicks inside the frame. 

This approach makes it important for you to do a few things to set this up.

1. Make sure you find a placid place where there aren't any changes in lighting, fish or monsters or other players.
1. From your menu, click "System" and "Graphics". Set "Liquid Detail" to "Low". It'll make it easier for the computer to "see" the lure.
1. Scroll is so you're in first person view and can't see your character on screen, just the water.
1. A good spot for Shadowlands fishing in Maldraxxus, 62.5, 71.75, facing south.

So I can foresee a few problems with this initial code:

1. None of the images I took appropriately match where you want to fish: 
    1. Take a small frame screenshot of the area right around the lure and place it in the wowscripts folder
    1. change the fish(image) command at bottom to reflect your file name
    1. Adjust the counter in fish(image) to a smaller number, like 10, so you can do a trial and see how it works

1. Your cast() function doesn't work:
    1. The images are based on my screen size, so there might be a problem if your monitor is quite different than mine. 
    1. Take a screenshot of your fishing icon you have in your action bar
    1. input this name in your cast() function
  
I usually get 80% good casts with this, and if you want to optimize definitely let me know! You can play with the confidence levels (0-1), images, etc. 



this helps because there are sometimes waves or small fish under the water, or light effects that change many elements

catch()


