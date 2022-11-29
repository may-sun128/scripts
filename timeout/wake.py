#!/usr/bin/python

from timeout import *
import pyautogui

# not being used in favor or RTCWake

seconds_to_wake = get_seconds("06:00")
print(seconds_to_wake)
print(f'type = ' + str(type(seconds_to_wake)))
countdown(seconds_to_wake)
print('started timer...')
#countdown(3)
for i in range(5):
    pyautogui.press('enter')


