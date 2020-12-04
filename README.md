# wowscripts
Using pyautogui to automate different repetitive tasks in World of Warcraft MMORPG. Make anything. Save lifetimes.

## First set up a pyautogui virtual environment and install dependencies

```python
python3 -m venv pyautogui_venv
. pyautogui_venv/bin/activate
pip install pyautogui ipython numpy==1.19.3 pillow
```

## Fishing Script

The fishing script works in three steps:

1. Find the FISH icon on the screen, and click it to cast;
1. Find the lure / bobber icon after the cast;
3. Monitor the square area around the lure for a significant change frame by frame, looking for the "splash" when a fish in on hook.

Some tips before running:

1. Make sure you find a placid place where there aren't any changes in lighting, fish or monsters or other players.
1. From your menu, click "System" and "Graphics". Set "Liquid Detail" to "Low". It'll make it easier for the computer to "see" the lure.
1. Scroll your view in, so you're in first person view and can't see your character on screen, just the water.
1. A good spot for Shadowlands fishing in Maldraxxus, 62.5, 71.75, facing south.

## You're ready to run the script!

```bash
cd fishing
python fish.py
```
