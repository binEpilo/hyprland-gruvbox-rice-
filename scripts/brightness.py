#!/bin/python

import subprocess, sys

if sys.argv[1] == "--up":
    subprocess.run(["brightnessctl", "s", "350+"])
elif sys.argv[1] == "--down":
    subprocess.run(["brightnessctl", "s", "350-"])

output = subprocess.getoutput(["brightnessctl"])

position_of_percent = output.find("%")


icons = ["󰃞", "󰃟", "󰃝", "󰃠"]

try:
    number = int(output[position_of_percent - 2:position_of_percent])


    if number == 00:
        icon = icons[3]
    elif number < 25:
        icon = icons[0]
    elif number < 50:
        icon = icons[1]
    elif number < 75:
        icon = icons[2]
    elif number < 100:
        icon = icons[3]
except ValueError:
    icon = icons[0]


subprocess.run(["eww", "update", f"brightnesspoll={icon}"])
