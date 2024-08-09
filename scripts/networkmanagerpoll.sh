#!/bin/bash

handle() {
  if [[ $1 == *"primary"* ]]; then
    if [[ $1 == "'Wired connection 1' is now the primary connection" ]]; then
      eww update internetpoll=󰈀
    elif [[ $1 == *"is now the primary connection" ]]; then
      eww update internetpoll=󰖩
    else
      eww update internetpoll=󰖪
    fi
  fi
}

nmcli monitor | while read -r line; do handle "$line"; done
