#!/bin/bash

handle() {
  case $1 in
      *card*) /home/me/.config/scripts/pipewire.py a ;;
      *server*) /home/me/.config/scripts/pipewire.py a ;;
  esac
}

pactl subscribe | while read -r line; do handle "$line"; done
