#!/bin/bash

loginctl terminate-session $(cat /home/me/.config/scripts/session.txt)
