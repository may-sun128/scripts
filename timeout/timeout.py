#!/usr/bin/python

import datetime
import os
import time
import sys 


if len(sys.argv) == 1:
	alarm_input = '00:30'
else:
	alarm_input = sys.argv[1]

def countdown(seconds: int):
	start = 0
	while start < seconds:
		# uncomment to see to seconds count down
		#print(seconds)
		time.sleep(1)
		#os.system('clear')
		seconds -= 1

def get_seconds(target_time):
# Convert the alarm time from [H:M] or [H:M:S] to seconds
	alarm_time = [int(n) for n in target_time.split(":")]
	seconds_hms = [3600, 60, 1] # Number of seconds in an Hour, Minute, and Second
	alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])

	# Get the current time of day in seconds
	now = datetime.datetime.now()
	current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

	# Calculate the number of seconds until alarm goes off
	time_diff_seconds = alarm_seconds - current_time_seconds

	# If time difference is negative, set alarm for next day
	if time_diff_seconds < 0:
		time_diff_seconds += 86400 # number of seconds in a day

	return time_diff_seconds

'''
def check_success():
	f = open('home/mholmes/JunkDrawer/timeout-working/test.txt', 'w', 'x')
	f.write('program has been launched') 
	f.close() 

check_success()
'''
 
time_diff_seconds = get_seconds(alarm_input)

print('set sleeptime...')

countdown(time_diff_seconds)

os.system('systemctl suspend')
#os.system('echo "it worked"')














