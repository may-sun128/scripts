#!/usr/bin/python

# this script increases and decreases the system volume

import subprocess
import sys 


def execute_bash(command: str):
	obj = subprocess.Popen(f"{command}", stdout=subprocess.PIPE, shell=True)
	obj_bin, err = obj.communicate()

	# Not sure what the point of this is
	status = obj.wait()

	val = obj_bin.decode('ascii') 
	return val

volume = int(execute_bash('awk -F"[][]" \'/Left:/ { print $2 }\' <(amixer sget Master)').replace('%', '').strip())

if len(sys.argv) == 2:
	if sys.argv[1] == 'up':
		new_vol = volume + 5
		execute_bash(f'amixer set Master {str(new_vol)}%')
	elif sys.argv[1] == 'down':
		new_vol = volume - 5
		execute_bash(f'amixer set Master {str(new_vol)}%')
elif len(sys.argv) == 3:
	if sys.argv[1] == 'up':
		new_vol = volume + int(sys.argv[2])
		execute_bash(f'amixer set Master {str(new_vol)}%')
	elif sys.argv[1] == 'down':
		new_vol = volume - int(sys.argv[2])
		execute_bash(f'amixer set Master {str(new_vol)}%')
else:
	print('Parameter Error')
# print(sys.argv)