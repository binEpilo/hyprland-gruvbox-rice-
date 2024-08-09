#!/bin/bash

DATE=$(date +'%Y-%m-%d-%H:%M:%S')
grim -g "$(slurp)" /home/me/Pictures/Bildschirmfotos/$DATE.png
wl-copy < /home/me/Pictures/Bildschirmfotos/$DATE.png
