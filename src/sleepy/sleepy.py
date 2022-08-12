import subprocess
from evdev import uinput, ecodes as e
import time

def x(command):
    subprocess.run(command)

x(["firefox"," https://mynoise.net/NoiseMachines/thunderNoiseGenerator.php"])

time.sleep(5)

# Not sure if this is working or not
# The vim key binding extension in firefox seems to conflict
# with myNoise's keyboard input 
# I think launching the private instance of firefox will prevent this

# Even then, if the key event doesn't happen, 
# this(https://stackoverflow.com/questions/2575528/simulating-key-press-event-using-python-for-linux) seems easier in general

with uinput.Uinput() as ui: 
    ui.write(e.EV_KEY, e.KEY_k, 1)
    ui.syn()

