#!/bin/python

import subprocess, os, time, sys

output = subprocess.getoutput("hyprctl monitors")
if "ID 0" and "ID 1" in output:
    os.system('sed -i s/"monitor 0"/"monitor 1"/g /home/me/.config/eww/eww.yuck')
    os.system('sed -i s/"workspace = 10, monitor:DP-1"/"workspace = 10, monitor:eDP-1"/g /home/me/.config/hypr/hyprland.conf')
    os.system('sed -i s/"monitor = eDP-1"/"monitor = DP-1"/g /home/me/.config/hypr/hyprlock.conf')
else:
    os.system('sed -i s/"monitor 1"/"monitor 0"/g /home/me/.config/eww/eww.yuck')
    os.system('sed -i s/"workspace = 10, monitor:eDP-1"/"workspace = 10, monitor:DP-1"/g /home/me/.config/hypr/hyprland.conf')
    os.system('sed -i s/"monitor = DP-1"/"monitor = eDP-1"/g /home/me/.config/hypr/hyprlock.conf')

if sys.argv[1] == "restart":
    os.system("killall eww")
    os.system("/home/me/.config/scripts/swaybg.sh")
    os.system("/home/me/.config/scripts/eww.sh")
