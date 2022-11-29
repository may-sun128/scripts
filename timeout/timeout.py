#!/usr/bin/python

import datetime
import os
import time
import sys 


def countdown(seconds: int):
	start = 0
	while start < seconds:
		# uncomment to see to seconds count down
		print(seconds)
		time.sleep(1)
		#os.system('clear')
		seconds -= 1

def get_seconds(target_time: str):
# Convert the alarm time from [H:M] or [H:M:S] to seconds
	alarm_time = [int(n) for n in target_time.split(":")]
	seconds_hms = [3600, 60, 1] # Number of seconds in an Hour, Minute, and Second
	alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])

	# Get the current time of day in seconds
	now = datetime.datetime.now()
	current_time_seconds = sum([a*b for a, b in zip(seconds_hms, [now.hour, now.minute, now.second])])

	# Calculate the number of seconds until alarm goes off
	time_diff_seconds = alarm_seconds - current_time_seconds

	# If time difference is negative, set alarm for next day
	if time_diff_seconds < 0:
		time_diff_seconds += 86400 # number of seconds in a day

	return time_diff_seconds


def main():
	if len(sys.argv) == 1:
		alarm_input = '23:30'
	else:
		alarm_input = sys.argv[1]

	time_diff_seconds = get_seconds(alarm_input)

	print('set sleeptime...')

	countdown(time_diff_seconds)

	suspend_only = 'systemctl suspend'
	# standby, bios clock, time
	suspend_and_wake = "sudo rtcwake -m mem -a -t $(date +%s -d 'tomorrow 06:00')"
	debug = "sudo rtcwake -m on -a -t $(date +%s -d 'tomorrow 06:00')"
	os.system(suspend_and_wake)

	print("Exited")

if __name__ == "__main__":
	main()

