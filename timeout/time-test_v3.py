from datetime import datetime
import subprocess
import time
import sys 

def get_seconds_to_sleep():         
	now  = datetime.now()

	sleep_time = get_sleep_time()

	time_before_sleep = sleep_time - now
	time_before_sleep_seconds = time_before_sleep.total_seconds()
	return time_before_sleep_seconds

def get_sleep_time():
	now  = datetime.now()

	# This is a dumb way of doing this, but it stands for right now. 

	year = int(now.strftime('%Y')) # or %y?
	month = int(now.strftime('%m')) 
	# NOTE, if note bebugging add + 1 to day (so it'll be after midnight)
	day = int(now.strftime('%d')) + 1 # will not work on the last day of the month
	second = int('15')

	if len(sys.argv) == 1:
		 
		# hard code the sleep time if no argument is specified
		hour = int('2')
		minute = int('1')
		

		# time to go to sleep 
		# year month day hour minute second
		# hard-coding for now
		sleep_time = datetime(year, month, day, hour, minute, second)

		return sleep_time
	else: 
		time: str = sys.argv[1]
		
		if time[0] != '0':
			hour = int(time[0] + time[1])
		elif time[0] == 0:
			hour = int(time[1])

		if time[2] != '0':
			minute = int(time[3])
		elif time[2] == 0:
			minute = int(time[2] + time[3])
		
		#minute = time[2] + time[3]

		sleep_time = datetime(year, month, day, hour, minute, second)
		return sleep_time

def main():
	seconds_to_sleep = get_seconds_to_sleep()

	#subprocess_object = subprocess.Popen(f'sleep {seconds_to_sleep} && systemctl suspend', stdout=subprocess.PIPE, shell=True)
	
	print(seconds_to_sleep)
	time.sleep(seconds_to_sleep)

	suspend_command = 'systemctl suspend'
	debug_command = 'echo hello'

	subprocess_object = subprocess.Popen(debug_command, stdout=subprocess.PIPE, shell=True)
	binary_output, err = subprocess_object.communicate()

	print(err)


main()



#***** Debuggin *****

# def dbug_print(s):
# 	print(s)

# def dbug_main():
# 	get_sleep_time()

# dbug_main()



