#!/usr/bin/env python3
""" This is a crappy binary clock using the keyboard lights. """

import subprocess
import time
import sys

UPDATE_TIME = 1 # Time in seconds.
SEP_COLOR = "FFEEDD"
HOUR_COLOR = "FF0000"
MINUTE_COLOR = "00FF00"
SECOND_COLOR = "0000FF"
OFF_COLOR = "000000"
BLOCK_COLOR = "993F1F"
exitColor = "993F1F"

KEYS  = {
    'hour': ['1','2','3','4','5'],
    'minute' : ['7','8','9','0','-','='],
    'second' : ['d', 'f', 'g', 'h', 'j', 'k'],
    "seprator" : '6',
}

def SetKeys():
    """Set the required keys to on or off."""
    command_string = "echo -e '\n"
    off_keys = []
    on_keys = []
    t = time.localtime()
    td = {
        'hour' : t.tm_hour,
        'minute' : t.tm_min,
        'second' : t.tm_sec,
    }
    for k in td:
        for i,key in enumerate(KEYS[k][::-1]):
            if td[k] & (1<<i):
                on_keys.append(key)
            else:
                off_keys.append(key)
    for key in on_keys:
        command_string += F"k {key} {HOUR_COLOR}\n"
    for key in off_keys:
        command_string += F"k {key} {OFF_COLOR}\n"
    command_string += "c'"
    subprocess.call(F"{command_string} | g810-led -pp", shell=True)

if len(sys.argv) > 1:
    print("Usage python3 BinaryClock.py")
    sys.exit(1)
subprocess.call(F"g910-led -a {BLOCK_COLOR}", shell=True)
subprocess.call(F"g910-led -k {KEYS['seprator']} {SEP_COLOR}", shell=True)
try:
    while True:
        SetKeys()
        time.sleep(1)
except KeyboardInterrupt:
    subprocess.call(f"g910-led -a {exitColor}", shell=True)
print("\033[A")
