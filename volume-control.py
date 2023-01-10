#!/usr/bin/python

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

if sys.argv[1] == 'up':
	new_vol = volume + 5
	execute_bash(f'amixer set Master {str(new_vol)}%')
elif sys.argv[1] == 'down':
	new_vol = volume - 5
	execute_bash(f'amixer set Master {str(new_vol)}%')

# print(sys.argv)