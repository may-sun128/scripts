import pyautogui
import time
import sys
from datetime import datetime

pyautogui.FAILSAFE = False
minutes_before_jiggle = None

# Check to make sure there's only one arg 
# If not, set minutes_before_jiggle to 1

# DEBUG: Leaving this out for now
'''
if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    minutes_before_jiggle = 1
else:
    minutes_before_jiggle = int(sys.argv[1])
'''

class Debug:
    def __init__(self):
        self.temp = None

    def LogSeconds(self):
        i: int = 0
        while i < 0:
            time.sleep(1)
            print(i)
            i += 1

    def dprint(self, s: str):
        print(s)


def jiggle(minutes_before_jiggle: int):
    running = True
    while(running):
        # HH:MM:SS
        current_time: str = datetime.now().strftime('%X')
        # If it's after 12am, stop script 
        if current_time.split(':')[0] == '0':
            running = False
        
        # x = 0
        # # Wait until time to jiggle 
        # while(x < minutes_before_jiggle):
        #     time.sleep(60)
        #     x += 1

        # Actually move mouse
        for i in range(0,200):
            pyautogui.moveTo(0,i*4)
        pyautogui.moveTo(1,1)

        # Not sure what this does
        for i in range(0,3):
            pyautogui.press("shift")

        # Log movements to console
        #print("Movement made at {}".format(datetime.now().time()))

def main():
    jiggle(1)

    db.dprint('Built')

if __name__ == '__main__':
    main()