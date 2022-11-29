from timeout import *


alarm_input = "23:30"

time_diff_seconds = get_seconds(alarm_input)

print('set sleeptime...')

countdown(time_diff_seconds)

os.system('systemctl suspend')