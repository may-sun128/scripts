#!/usr/bin/python

import pyautogui
import time
import os


play_x = 1329
play_y = 612

cnn_url = 'https://go.cnn.com/?stream=cnn'

# kill existing firefox processes
os.system('pkill firefox')
time.sleep(3)
				  # --kiosk
os.system(f'firefox --kiosk {cnn_url} &')
time.sleep(5)
for i in range(3):
	pyautogui.moveTo(play_x, play_y)
	time.sleep(1)
pyautogui.click()