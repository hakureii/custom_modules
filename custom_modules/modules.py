#!/data/data/com.termux/files/usr/bin/env python

import sys
import tty
import termios
import fcntl
import os
import errno
import time
import json

def getch(timeout=None):
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        # Set the file descriptor to non-blocking mode
        fcntl.fcntl(fd, fcntl.F_SETFL, os.O_NONBLOCK)
        if timeout is None:
            ch = sys.stdin.read(1)
        else:
            start_time = time.time()
            while True:
                try:
                    ch = sys.stdin.read(1)
                    if ch:
                        break
                    elif time.time() - start_time > timeout:
                        break
                    else:
                        time.sleep(0.05)  # Adjust sleep time as needed
                except IOError as e:
                    if e.errno != errno.EAGAIN:
                        raise
                    elif time.time() - start_time > timeout:
                        break
                    else:
                        time.sleep(0.05)  # Adjust sleep time as needed
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

class Color:
    def __init__(self):
        cd = os.path.dirname(__file__)

        with open(os.path.join(cd, "./Colors.json")) as file:
            self.colors = json.load(file)
    hello = ""
    def get(self, color: str="RES") -> str:
        """
        ['RES', 'GREY', 'RED', 'GRE', 'YEL',
        'BLU', 'PUR', 'CYA', 'WHI', 'BGREY',
        'BRED', 'BGRE', 'BYEL', 'BBLU', 'BPUR',
        'BCYA', 'BWHI', 'UGREY', 'URED', 'UGRE',
        'UYEL', 'UBLU', 'UPUR', 'UCYA', 'UWHI']
        """
        return self.colors[color]
