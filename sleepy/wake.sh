#!/usr/bin/bash

# 15 minutes after wake via insomnia.sh
echo "wake launched" >> log
sleep $(date +%s -d 'tomorrow 06:15') 
amixer set Master 45%
