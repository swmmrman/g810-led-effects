#!/usr/bin/python3

"""
This is a recreation of the KITT light bar.

It is loosly based on the k2000 script from g810-led.
"""

import sys
import subprocess
import time


if len(sys.argv) > 1:
    if sys.argv[1] == '--help':
        print('k2000 [speed (default:0.02] [colorOff] [colorOn] [colorFade1]\
[colorFade2]')
        sys.exit()


speed = 0.03
colorOff = '000000'
colorOn = 'FF0000'
colorFade1 = 'AA0000'
colorFade2 = '3F0000'
mainColor = '1d0000'
exitColor = "993F1F"

if len(sys.argv) > 1:
    try:
        speed = float(sys.argv[1])
    except TypeError:
        print('Speed arg error')
if len(sys.argv) > 2:
    try:
        colorOff = sys.argv[2]
    except TypeError:
        print('colorOff arg error')
if len(sys.argv) > 3:
    try:
        colorOn = sys.argv[3]
    except TypeError:
        print('colorOn arg error')
if len(sys.argv) > 4:
    try:
        colorFade1 = sys.argv[4]
    except TypeError:
        print('colorFade1 arg error')
if len(sys.argv) > 5:
    try:
        colorFade2 = sys.argv[5]
    except TypeError:
        print('colorFade2 arg error')


def setKeys(**kwargs):
    """Set the keys to be lit or not."""
    pipeValue = "\\n"
    for arg in kwargs:
        value = kwargs[arg]
        if arg == "on":
            pipeValue += 'k ' + value + ' ' + colorOn + '\\n'
        elif arg == "f1":
            pipeValue += 'k ' + value + ' ' + colorFade1 + '\\n'
        elif arg == "f2":
            pipeValue += 'k ' + value + ' ' + colorFade2 + '\\n'
        elif arg == "off":
            pipeValue += 'k ' + value + ' ' + colorOff + '\\n'
    pipeValue = pipeValue + 'c'
    pipeValue = f"echo -e '{pipeValue}'"
    # print(f"{pipeValue}")
    subprocess.call(f"{pipeValue} | g910-led -pp", shell=True)
    time.sleep(speed)


subprocess.call('g910-led -a ' + mainColor, shell=True)
for color in [colorFade2, colorFade1, colorOn, colorFade1, colorFade2,
              colorOff]:
    subprocess.call(f"g910-led -g fkeys {color}", shell=True)
    time.sleep(.2)
setKeys(on='F1')
setKeys(on='F2', f1="F2")
setKeys(on="F3", f1="F2", f2="F1")

try:
    while True:
        for i in range(1, 12):
            h = (i-1) if i - 1 > 0 else 'j'
            g = i-2 if i - 2 > 0 else 'j'
            f = i-3 if i - 3 > 0 else 'j'
            setKeys(on=f"F{i}", f1=f"F{h}", f2=f"F{g}", off=f"F{f}")
        setKeys(on="F11", f1="F12", off="F9")
        for i in range(12, 1, -1):
            j = i+1 if i+1 < 13 else 'j'
            k = i+2 if i+2 < 13 else 'j'
            f = i+3 if i+3 < 13 else 'j'
            setKeys(on=f"F{i}", f1=f"F{j}", f2=f"F{k}", off=f"F{f}")
        setKeys(on="F2", f1="F1", off="F4")
except KeyboardInterrupt:
    subprocess.call(f"g910-led -a {exitColor}", shell=True)
