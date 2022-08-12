#!/usr/bin/env python3

# This script displays a human-readible list of directories in PATH at the cmd

import subprocess 

paths_subprocess_object = subprocess.Popen("echo $PATH", stdout=subprocess.PIPE, shell=True)
binaryPaths, err = paths_subprocess_object.communicate()

# Not sure what the point of this is
status = paths_subprocess_object.wait()

paths = binaryPaths.decode('ascii') 

paths_list = paths.split(':') 

print('***** PATHS ******')
for path in paths_list:
    print(path)
