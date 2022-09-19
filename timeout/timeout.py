import datetime 
import sys
import subprocess
import time

'''
Most recent version 22-09-19
'''

def trim_zero(h: str):
	if h[0] == '0':
		new_h = h.replace('0', '')
		return new_h
	else:
		return h


def get_sleep_time():
	if len(sys.argv) > 1:
		user_sleep_time: str = sys.argv[1]
		hour = trim_zero(user_sleep_time[:2])
		# print(f'hour = {hour}')
		minute = trim_zero(user_sleep_time[2:])
		# print(f'minute = {minute}')
		return [hour, minute]
	elif len(sys.argv) == 1:
		# default sleep time
		return ['1', '30']


def get_seconds(time: list):
	seconds_to_sleep = 0
	# hours in seconds
	seconds_to_sleep += int(time[0]) * 60 * 60
	seconds_to_sleep += int(time[1]) * 60

	current_seconds = 0
	current_time = datetime.datetime.now()
	current_hour = int(current_time.strftime('%H')) * 60 * 60
	current_moment = int(current_time.strftime('%M')) * 60
	print(f'h={current_moment}')
	current_seconds += current_hour + current_moment

	if current_seconds > seconds_to_sleep:
		seconds = current_seconds - seconds_to_sleep
	else:
		seconds = seconds_to_sleep - current_seconds
	print(seconds)

	return seconds

def countdown(seconds: int):
	start = 0
	while start < seconds:
		print(seconds)
		time.sleep(1)
		seconds -= 1


sleep_time = get_sleep_time()
seconds = get_seconds(sleep_time)
countdown(seconds)

subprocess_object = subprocess.Popen("echo test", stdout=subprocess.PIPE, shell=True)
binary_output, err = subprocess_object.communicate()

print(binary_output.decode('ascii'))








