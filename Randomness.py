#!/usr/bin/env python3
"""
Keyboard randomness.

Just blinks all the keys randomly.
"""
import sys
import subprocess
import time
import random
import string
speed = .25

allkeys = list(string.ascii_letters[0:])
allkeys += ['-', '=', '[', ']', ';', '"', ',', '.', '/', '~', 'tab',
            'capslock', '\\', ' space', 'shiftleft', 'shiftright', 'ctrlleft',
            'ctrlright', 'winleft', 'winright', 'altleft', 'altright', 'menu',
            'center', 'backspace', 'esc', 'logo', 'logo2', 'top', 'bottom',
            'left', 'right', 'ins', 'home', 'pageup', 'pagedown', 'del', 'end',
            'num+', 'num-', 'num*', 'num/', 'numenter', 'num.', 'num_lock',
            'printscr', 'scroll_lock', 'pause', 'space'
            ]

for num in range(0, 11):
    allkeys.append(F"num{num}")
for f in range(1, 13):
    allkeys.append(F"F{f}")
for g in range(1, 10):
    allkeys.append(F"G{g}")
for i in range(0, 11):
    allkeys.append(str(i))


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
