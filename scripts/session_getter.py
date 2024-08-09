#!/bin/python

import subprocess

session = subprocess.getoutput("echo $XDG_SESSION_ID")

with open("/home/me/.config/scripts/session.txt", "w") as file:
    file.write(session)
