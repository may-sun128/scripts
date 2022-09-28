import subprocess

# for i in range(len(apps)):


# obj = subprocess.Popen("pgrep cool-retro-term", stdout=subprocess.PIPE, shell=True)
# obj_bin, err = obj.communicate()

# # Not sure what the point of this is
# status = obj.wait()

# val = obj_bin.decode('ascii') 

# val = val.split()

# print(val)


'''
signal_codes = []
for each app in apps:
	signal_codesl.append(get_signal_codes(app)) 

for each signal_code in signal_codes: 
	kill_process(signal_code)

start_media()
set_sleep_timer()
set_wake_alarm() # really just send keyboard input 
				 # bc the media should still be playing
				 # if in bed, I should just have to turn the speaker on 

'''

apps = ['cool-retro-term', 'firefox', 'vlc']

singal_codes = []

for app in apps:
	obj = subprocess.Popen(f"pgrep {app}", stdout=subprocess.PIPE, shell=True)
	obj_bin, err = obj.communicate()

	# Not sure what the point of this is
	status = obj.wait()

	val = obj_bin.decode('ascii').split()
	if len(val) < 1:
		singal_codes.append(val)
	else:
		for v in val:
			singal_codes.append(v)

print(singal_codes)

for sg in singal_codes:
	obj = subprocess.Popen(f"pgrep {app}", stdout=subprocess.PIPE, shell=True)
	obj_bin, err = obj.communicate()

	# Not sure what the point of this is
	status = obj.wait()

	val = obj_bin.decode('ascii').split()