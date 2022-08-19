import pyautogui
import time
import sys
from datetime import datetime

pyautogui.FAILSAFE = False
minutes_before_jiggle = None

# Check to make sure there's only one arg 
# If not, set minutes_before_jiggle to 1

# Hard-coding arguments for now instead of getting them from the command line
'''
if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    minutes_before_jiggle = 1
else:
    minutes_before_jiggle = int(sys.argv[1])
'''

def jiggle(minutes_before_jiggle: int, timeout_hour: str):
    running = True
    while running:
        # HH:MM:SS
        current_time: str = datetime.now().strftime('%X')
        # If it's after 12am, stop script 
        current_hour = current_time.split(':')[0]
        if current_hour == timeout_hour:
            # Apparently, setting running to false does not exit the while loop
            # I guess it gets evaluated only at the beginning of the loop, since python is interpreted
            #running = False
            # Using the exit function instead--note sure if this is best practice
            print('Timed out.')
            exit()
        
        x = 0
        # Wait until time to jiggle
        while(x < minutes_before_jiggle):
            time.sleep(60)
            x += 1

        # Actually move mouse
        for i in range(0,100):
            pyautogui.moveTo(0,i*4)
        pyautogui.moveTo(1,1)

        # Not sure what this does
        for i in range(0,3):
            pyautogui.press("shift")

        # Log movements to console
        #print("Movement made at {}".format(datetime.now().time()))

def main():
    # start immediately (first arg), timeout at 1am (second arg)
    jiggle(0, '01')

    db.dprint('Built')

if __name__ == '__main__':
    main()