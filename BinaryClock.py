#!/usr/bin/env python3
""" This is a crappy binary clock using the keyboard lights. """

import subprocess
import time
import sys

UPDATE_TIME = 1 # Time in seconds.
COLORS = {
    'hour'      : "FF0000",
    'minute'    : "00FF00",
    'second'    : "0000FF",
    'seperator' : "FFEEDD",
    'off'       : "000000",
    'block'     : "993F1F",
    'exit'      : "993F1F",
}
KEYS  = {
    'hour'     : ['1','2','3','4','5'],
    'minute'   : ['7','8','9','0','-','='],
    'second'   : ['c', 'v', 'b', 'n', 'm', ','],
    "seperator" : '6',
}

def SetKeys():
    """Set the required keys to on or off."""
    command_string = "echo -e '\n"
    keys = []
    t = time.localtime()
    td = {
        'hour' : t.tm_hour,
        'minute' : t.tm_min,
        'second' : t.tm_sec,
    }
    for k in td:
        for i,key in enumerate(KEYS[k][::-1]):
            if td[k] & (1<<i):
                command_string += F"k {key} {COLORS[k]}\n"
            else:
                command_string += f"k {key} {COLORS['off']}\n"
    command_string += "c'"
    subprocess.call(F"{command_string} | g810-led -pp", shell=True)

if len(sys.argv) > 1:
    print("Usage python3 BinaryClock.py")
    sys.exit(1)
subprocess.call(F"g810-led -a {COLORS['block']}", shell=True)
subprocess.call(F"g810-led -k {KEYS['seperator']} {COLORS['seperator']}", shell=True)
try:
    while True:
        SetKeys()
        time.sleep(UPDATE_TIME)
except KeyboardInterrupt:
    subprocess.call(f"g810-led -a {COLORS['exit']}", shell=True)
print("\033[A")
