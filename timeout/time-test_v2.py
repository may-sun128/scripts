from datetime import datetime
import subprocess
import time

def get_seconds_to_sleep():
	now  = datetime.now()

	# This is a dumb way of doing this, but it stands for right now. 

	year = int(now.strftime('%Y')) # or %y?
	month = int(now.strftime('%m')) 
	day = int(now.strftime('%d')) + 1 # will not work on the last day of the month 
	hour = int('2')
	minute = int('1')

	# time to go to sleep 
	# year month day hour minute second
	# hard-coding for now
	sleep_time = datetime(year, month, day, hour, minute, 15)         
	
	time_before_sleep = sleep_time - now
	time_before_sleep_seconds = time_before_sleep.total_seconds()
	return time_before_sleep_seconds

def countdown(seconds_to_sleep):
	i = 0 
	while i < seconds_to_sleep:
		print(i)
		i += 1
		time.sleep(60)


def main():
	seconds_to_sleep = get_seconds_to_sleep()

	#subprocess_object = subprocess.Popen(f'sleep {seconds_to_sleep} && systemctl suspend', stdout=subprocess.PIPE, shell=True)
	
	time.sleep(seconds_to_sleep)
	subprocess_object = subprocess.Popen(f'systemctl suspend', stdout=subprocess.PIPE, shell=True)
	binary_output, err = subprocess_object.communicate()

	print(err)

main()




