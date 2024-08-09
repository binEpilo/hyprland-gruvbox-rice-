#!/bin/python

import sys, subprocess

output = subprocess.check_output("nmcli", shell=True, encoding="utf-8")

if "proton" in output:
    vpn = "proton"
    icon = "󰟐"
elif "homeserver" in output:
    vpn = "homeserver"
    icon = "󰋜"
else:
    vpn = "no vpn"
    icon = "󱩆"

try:
    new_vpn = sys.argv[1]
    if vpn == "proton":
        subprocess.check_output(["nmcli", "connection", "down", "proton"])
    elif vpn == "homeserver":
        subprocess.check_output(["nmcli", "connection", "down", "homeserver"])
    if new_vpn == "󰟐":
        subprocess.check_output(["nmcli", "connection", "up", "proton"])
    elif new_vpn == "󰋜":
        subprocess.check_output(["nmcli", "connection", "up", "homeserver"])
    new_vpn += "  "
    subprocess.run(["eww", "update", f"vpnpoll={new_vpn}"])
except:
    subprocess.run(["eww", "update", f"vpnpoll={icon}  "])
