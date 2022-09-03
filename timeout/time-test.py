from datetime import datetime
import subprocess
import time

def get_seconds_to_sleep():
	# time to go to sleep 
	# 					  year month day hour minute second
	# hard-coding for now
	sleep_time = datetime(2022, 9, 3, 14, 17, 15)         
	
	now  = datetime.now()
	duration = sleep_time - now
	duration_in_s = duration.total_seconds()
	return duration_in_s

def countdown(seconds_to_sleep):
	i = 0 
	while i < seconds_to_sleep:
		print(i)
		i += 1
		time.sleep(60)


def main():
	seconds_to_sleep = get_seconds_to_sleep()

	subprocess_object = subprocess.Popen(f'sleep {seconds_to_sleep} && systemctl suspend', stdout=subprocess.PIPE, shell=True)
	binary_output, err = subprocess_object.communicate()

	print(err)
	countdown(seconds_to_sleep)

main()




