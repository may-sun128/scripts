#!/usr/bin/bash

# this script sets the RTC time and countdowns to it

# `$1` corrosponds to the first command line arg 
# (if getting input at the command line)
echo "Warning: this command must be run as sudo"
# Ex: sudo sleepy.sh 10m" 
echo "started..."
redshift -P -O 2000
sleep $1 
# real command
rtcwake -m mem -a -t $(date +%s -d 'tomorrow 06:00') 
# debugging commad
# rtcwake --dry-run --mode mem --auto --seconds 5
# sleep 30m
#amixer set Master 45%
#python $HOME/repos/python/selenium-white-noise/white-noise.py

# Okay, so some things I did to get rtcwake to work without sudo:
# - added /usr/sbin/rtc to the sudo file (using `sudo visudo`)
# - change the permissions to rtc0 with `sudo chmod ugo+r rtc0`
# - changed the permissions to sys/power/state with read and write permissions
