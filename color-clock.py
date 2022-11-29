#!/usr/bin/python

import datetime
import time
from termcolor import colored

colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']

running = True

cnt = 0

while(running):	
	if cnt < len(colors): 	
		print(colored(datetime.datetime.now().strftime('%X'), colors[cnt]))
		time.sleep(3)
	else: 
		cnt = -1 
	cnt += 1
