#!/usr/bin/env python3
"""This is a crappy binary clock using the keyboard lights."""

import subprocess
import time
import signal
import sys
import threading
import gi
import setproctitle
from gi.repository import Gio

gi.require_version('Gio', '2.0')
Application = Gio.Application.new(
    "G810.BinaryClock", Gio.ApplicationFlags.FLAGS_NONE
)
Application.register()
running = True
# Set process name for easy finding
setproctitle.setproctitle("BinaryClock")

def sig_handler(sig, frame):
    global running
    print(f"Caught: {sig}")
    running = False

signal.signal(signal.SIGTERM, sig_handler)
signal.signal(signal.SIGABRT, sig_handler)
signal.signal(signal.SIGHUP, sig_handler)
signal.signal(signal.SIGINT, sig_handler)
UPDATE_TIME = 1  # Time in seconds.
COLORS = {
    'month':     "FFFF00",
    'day':       "00FFFF",
    'hour':      "FF0000",
    'minute':    "00FF00",
    'second':    "0000FF",
    'seperator': "993F1F", # "FFEEDD"
    'off':       "492824",
    'block':     "993F1F",
    'exit':      "993F1F",
}
KEYS = {
    'month':     ['G6', 'G7', 'G8', 'G9'],
    'day':       ['G1', 'G2', 'G3', "G4", "G5"],
    'hour':      ['1', '2', '3', '4', '5'],
    'minute':    ['7', '8', '9', '0', '-', '='],
    'second':    ['c', 'v', 'b', 'n', 'm', ','],
    "seperator": '6',
}


def SetKeys():
    """Set the required keys to on or off."""
    command_string = "echo -e '\n"
    t = time.localtime()
    td = {
        'month':    t.tm_mon,
        'day':      t.tm_mday,
        'hour':     t.tm_hour,
        'minute':   t.tm_min,
        'second':   t.tm_sec,
    }
    for k in td:
        for i, key in enumerate(KEYS[k][::-1]):
            if td[k] & (1 << i):
                command_string += F"k {key} {COLORS[k]}\n"
            else:
                command_string += f"k {key} {COLORS['off']}\n"
    command_string += "c'"
    subprocess.call(F"{command_string} | g810-led -pp", shell=True)


if len(sys.argv) > 1:
    print("Usage python3 BinaryClock.py")
    sys.exit(1)
subprocess.call(F"g810-led -a {COLORS['block']}", shell=True)
subprocess.call(
    F"g810-led -k {KEYS['seperator']} {COLORS['seperator']}", shell=True
)

def job():
    global running
    while running:
        SetKeys()
        time.sleep(UPDATE_TIME)
    subprocess.call(f"g810-led -a {COLORS['exit']}", shell=True)

t = threading.Thread(target=job)
t.start()
t.join()
