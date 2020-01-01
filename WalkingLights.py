#!/usr/bin/env python3
"""
Walking light pattern.

This one walks down the keyboard changing colors.
"""
import sys
import subprocess
import time
import random
speed = 1/32  # 32fps

"""building key lists"""
all_keys = ['G6', 'G7', 'G8', 'G9', 'logo', 'esc']
for f in range(1, 13):
    all_keys.append(F"F{f}")
all_keys += ['printscr', 'scroll_lock', 'pause', 'G1', "~"]
for i in range(1, 10):
    all_keys.append(str(i))
all_keys += [
            '0', '-', '=', 'backspace', 'ins', 'pageup', 'home', 'num_lock',
            'num/', 'num*', 'num-', 'G2', 'tab', 'q', 'w', 'e', 'r', 't', 'y',
            'u', 'i', 'o', 'p', '[', ']', '\\', 'delete', 'end', 'pagedown',
            'num7', 'num8', 'num9', 'numplus', 'G3', 'capslock'
            ]
all_keys += list("asdfghjkl:")
all_keys += [';', 'quote', 'enter', 'num4', 'num5', 'num6', 'G4', 'shiftleft']
all_keys += list("zxcvbnm,./")
all_keys += [
            'shiftright', "top", 'num1', 'num2', 'num3', 'numenter', 'G5',
            'ctrlleft', 'winleft', 'altleft', 'space', 'altright', 'winright',
            'menu', 'ctrlright', 'left', 'bottom', 'right', 'num0', 'num.',
            'logo2'
            ]


def setKeys(keys, color):
    """Set the keys color."""
    for key in keys:
        combo = f"'{key}' {color}"
        subprocess.call(f"g810-led -k {combo}", shell=True)
        time.sleep(speed)


randColor = "ff0000"  # seed random color
try:
    while True:
        setKeys(all_keys, randColor)
        time.sleep(1)
        randColor = format(random.randint(0, 255), 'x') + \
            format(random.randint(0, 255), 'x') + \
            format(random.randint(0, 255), 'x')
except KeyboardInterrupt:
    print("\033[F")  # return to clear ^c

subprocess.call("g810-led -a 993F1F", shell=True)
sys.exit(0)
