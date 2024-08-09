#!/bin/python
import subprocess

output = subprocess.getoutput("nmcli")

if "enp0s20f0u1u1: connected" in output:
    print("󰈀")
    subprocess.getoutput("eww update internetpoll=󰈀")
elif "wlp0s20f3: connected" in output:
    subprocess.getoutput("eww update internetpoll=󰖩")
else:
    subprocess.getoutput("eww update internetpoll=󰖪")
