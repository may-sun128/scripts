#!/usr/bin/bash

# Functions

print_time () {
	echo '----------Time----------'
	echo 'The time should be' $1 > $HOME/.scripts/sleepy/insomnia.log
	echo 'The time/date is:' $(date) > $HOME/.scripts/sleepy/insomnia.log
}

# Variables

sleep_time==$(date +%s -d 'today 23:00')
wake_time==$(date +%s -d 'tomorrow 06:00')

# Main

# sleep until 11pm
sleep $sleep_time
# suspend to memory and set wake time 
rtcwake -m mem -a -t $wake_time
echo "running after sleep..."
date 
amixer set Master 40%

