#!/bin/bash

HOURS=$(date +%H)

if [ $HOURS -eq 0 ] || [ $HOURS -eq 12 ]; then
  ICON="󱑖"
elif [ $HOURS -eq 1 ] || [ $HOURS -eq 13 ]; then
  ICON="󱑋"
elif [ $HOURS -eq 2 ] || [ $HOURS -eq 14 ]; then
  ICON="󱑌"
elif [ $HOURS -eq 3 ] || [ $HOURS -eq 15 ]; then
  ICON="󱑍"
elif [ $HOURS -eq 4 ] || [ $HOURS -eq 16 ]; then
  ICON="󱑎" 
elif [ $HOURS -eq 5 ] || [ $HOURS -eq 17 ]; then
  ICON="󱑏"
elif [ $HOURS -eq 6 ] || [ $HOURS -eq 18 ]; then
  ICON="󱑐"
elif [ $HOURS -eq 7 ] || [ $HOURS -eq 19 ]; then
 ICON="󱑑"
elif [ $HOURS -eq 8 ] || [ $HOURS -eq 20 ]; then
  ICON="󱑒"
elif [ $HOURS -eq 9 ] || [ $HOURS -eq 21 ]; then
  ICON="󱑓"
elif [ $HOURS -eq 10 ] || [ $HOURS -eq 22 ]; then
  ICON="󱑔"
elif [ $HOURS -eq 11 ] || [ $HOURS -eq 23 ]; then
  ICON="󱑕"

fi

echo $HOURS:$(date +%M) $ICON
