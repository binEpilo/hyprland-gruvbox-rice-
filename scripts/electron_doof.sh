#!/bin/bash

if [ $1 == "discord" ]; then
  discord --ozone-platform-hint=wayland
elif [ $1 == "spotify" ]; then
  spotify --enable-features=UseOzonePlatform --ozone-platform=wayland
fi
