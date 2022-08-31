#!/usr/bin/env python3

# This script displays a human-readible list of directories in PATH at the cmd

import subprocess 
from rich.console import Console
from rich.table import Table 

paths_subprocess_object = subprocess.Popen("echo $PATH", stdout=subprocess.PIPE, shell=True)
binaryPaths, err = paths_subprocess_object.communicate()

# Not sure what the point of this is
status = paths_subprocess_object.wait()

paths = binaryPaths.decode('ascii') 

paths_list = paths.split(':') 

# print('***** PATHS ******')
# for path in paths_list:
#     print(path)

table = Table("Global Paths")

for path in paths_list:
    table.add_row(path)

console = Console()
console.print(table)

