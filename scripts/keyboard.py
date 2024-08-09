#!/bin/python

import subprocess

output = subprocess.getoutput("hyprctl devices")

if "Greek" in output:
    subprocess.run(["eww", "update", "languagepoll=gr 󰌌"])
else:
    subprocess.run(["eww", "update", "languagepoll=de 󰌌"])
