#!/usr/bin/python

import subprocess
import os

def execute(command: str):
	obj = subprocess.Popen(f"{command}", stdout=subprocess.PIPE, shell=True)
	obj_bin, err = obj.communicate()

	# Not sure what the point of this is
	status = obj.wait()

	val = obj_bin.decode('ascii') 
	return val


# Redshift 
warm = 'redshift -P -O 4000'
warmer = 'redshift -P -O 2500'
warmest = 'redshift -P -O 2000'
cool = 'redshift -P -O 6000'

path = 'home/mholmes/.scripts/temp/temp-status.txt'


def set_status(status):
	f = open('temp-status.txt', "w")
	f.write(status)
	f.close()

def get_status():
	f = open('temp-status.txt', "r")
	status = f.read()
	f.close() 
	return status

def set_env():
	os.chdir('/home/mholmes/.scripts/temp')
	print(os.getcwd())

def main():
	set_env()
	status = get_status().strip()
	# if file is empty
	if status == '':
		print('Error: File was empty.')
	elif status == 'cool':
		execute(warm)
		set_status('warm')
	elif status == 'warm':
		execute(warmer)
		set_status('warmer')
	elif status == 'warmer':
		execute(warmest)
		set_status('warmest')
	elif status == 'warmest':
		execute(cool)
		set_status('cool')
	else:
		print('Error: Unknow Error')

main()