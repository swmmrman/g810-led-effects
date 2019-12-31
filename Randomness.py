#!/usr/bin/env python3
"""
Keyboard randomness.

Just blinks all the keys randomly.
"""
import sys
import subprocess
import time
import random
speed = .25

allkeys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=',
           '[', ']', ';', '"', ',', '.', '/', '~', 'tab', 'capslock', '\\',
           'space', 'shiftleft', 'shiftright', 'ctrlleft', 'ctrlright',
           'winleft', 'winright', 'altleft', 'altright', 'menu', 'enter',
           'backspace', 'esc'
           ]

for f in range(1, 13):
    allkeys.append(F"F{f}")
for g in range(1, 10):
    allkeys.append(F"G{g}")



def setKeys(keys):
    """Set the keys to be lit or not."""
    pipeValue = "\\n"
    for key in keys:
        randColor = format(random.randint(0, 255), 'x') + format(random.randint(0, 255), 'x') + format(random.randint(0, 255), 'x')
        pipeValue += "k " + key + " " + randColor + "\\n"
    pipeValue = pipeValue + 'c'
    pipeValue = f"echo -e '{pipeValue}'"
    # print(f"{pipeValue}")
    subprocess.call(f"{pipeValue} | g910-led -pp", shell=True)
    time.sleep(speed)


while True:
    try:
        setKeys(allkeys)
    except KeyboardInterrupt:
        subprocess.call(f"g910-led -a 993f1f", shell=True)
        sys.exit()
