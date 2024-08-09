#!/bin/bash

if curl -s "https://www.google.com" >/dev/null; then
  UPDATES=$(checkupdates | wc -l)
  #FLATPAK=$(flatpak remote-ls --updates | wc -l)
  AUR=$(yay -Qu | wc -l)
  sum=$((UPDATES + AUR))
  if [ $sum = 0 ]; then
    echo $sum 󰒙
  else
    echo $sum 󱆣
  fi
fi
