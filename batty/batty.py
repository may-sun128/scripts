#!/usr/bin/env python3

import subprocess

# Script to print battery life 
# TODO: make it fancy, add tui

def GetBatteryPercent():
    process = subprocess.Popen(['acpi', '-b'],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # convert from binary to string
    stdout_str = stdout.decode('ascii').strip() 

    # convert to list 
    stdout_lst = stdout_str.split()

    # get percent from list
    percent_str = stdout_lst[3].strip(',')
 
    return percent_str

def DisplayBattery(battery_percent):
    charged = ''
    for i in range(battery_percent):
        charged += '//'
    remainder = 10 - battery_percent 
    for i in range(remainder): 
        charged += '--'
    return charged 

percent = GetBatteryPercent() 
status = DisplayBattery(int(percent[0]))

msg = f"Battery: {percent} \n{status}"

print(msg)

