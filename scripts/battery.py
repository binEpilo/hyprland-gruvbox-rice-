#!/bin/python

import subprocess

output = subprocess.getoutput("upower -i /org/freedesktop/UPower/devices/battery_BAT0")

charging = True

for line in output.split("\n"):
    if "percentage" in line:
        output_percentage = int(line.strip()[-4:-1].strip())
    elif "state" in line and "discharg" in line:
        charging = False

if charging:
    liste = ["󰢟", "󰢜", "󰂆", "󰂇", "󰂈", "󰢝", "󰂉", "󰢞", "󰂊", "󰂋", "󰂅"]
else:
    liste = ["󰂎", "󰁺", "󰁻", "󰁼", "󰁽", "󰁾", "󰁿", "󰂀", "󰂁", "󰂂", "󰁹"]

if output_percentage < 9:
    icon = liste[0]
elif output_percentage < 18:
    icon = liste[1]
elif output_percentage < 27:
    icon = liste[2]
elif output_percentage < 36:
    icon = liste[3]
elif output_percentage < 45:
    icon = liste[4]
elif output_percentage < 54:
    icon = liste[5]
elif output_percentage < 63:
    icon = liste[6]
elif output_percentage < 72:
    icon = liste[7]
elif output_percentage < 81:
    icon = liste[8]
elif output_percentage < 90:
    icon = liste[9]
elif output_percentage <= 100:
    icon = liste[10]

print(f"{icon} {output_percentage}%")
