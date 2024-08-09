#!/bin/bash

handle() {
  case $1 in
    monitoradded*) /home/me/.config/scripts/monitor.py restart ;;
    monitorremoved*) /home/me/.config/scripts/monitor.py restart ;;
  esac
}

socat - "UNIX-CONNECT:$XDG_RUNTIME_DIR/hypr/$HYPRLAND_INSTANCE_SIGNATURE/.socket2.sock" | while read -r line; do handle "$line"; done
