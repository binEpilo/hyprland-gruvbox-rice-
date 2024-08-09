#!/bin/python

import subprocess, sys

volume_list = ["󰕿", "󰖀", "󰕾"]

if sys.argv[1] == "--up":
    subprocess.run(["wpctl", "set-volume", "-l", "1.4", "@DEFAULT_AUDIO_SINK@", "3%+"]) 
elif sys.argv[1] == "--down":
    subprocess.run(["wpctl", "set-volume", "-l", "1.4", "@DEFAULT_AUDIO_SINK@", "3%-"]) 

try:
    volume = int(float(subprocess.getoutput(["wpctl get-volume @DEFAULT_AUDIO_SINK@"])[8:]) * 100)
    print(volume)
    if volume == 0:
        volume_icon = volume_list[0]
    elif volume < 50:
        volume_icon = volume_list[1]
    elif volume <= 140:
        volume_icon = volume_list[2]
except:
    volume_icon = volume_list[0]

subprocess.run(["eww", "update", f"volumepoll={volume_icon}"])
