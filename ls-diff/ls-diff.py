#!/usr/bin/python

import sys
import os

# This script compares the contents of a directory to the previous contents of a directory.
# Deliverables: the difference between the same directory.
	# Useful for a directory like /dev, when adding a new device 

# args:
	# store - write the current directory listing in a temp file
	# compare - compare the current directory contents to the stored value

# Status: NOT WORKING

def set_env():
	os.chdir('/home/mholmes/.scripts/ls-diff/')

def get_longer_list(list_one, list_two):
	if len(list_one) > len(list_two):
		return list_one
	else:
		return list_two

def get_list_differnt_elements(list_one, list_two):
	unique_list = []
	for index, element in enumerate(get_longer_list(list_one, list_two), start=0): 
		if list_one[index] == list_two[index]:
			# print('Indexes are the same.'
			pass
		else:
			if list_one[index] == list_two[index + 1]:
				# print('indexes are not equal')
				unique_list.append(list_two[index])
				list_two.pop(index)
			elif list_one[index + 1] == list_two[index]:
				# print('indexes are not equal')
				unique_list.append(list_one[index])
				list_one.pop(index)
	return unique_list


def test():
	l1 = [1, 2, 3, 4, 5]
	l2 = [1, 2, 0, 3, 4, 5]

	ul = get_list_differnt_elements(l1, l2)
	# print(ul)

def main():
	set_env()

	dir_contents = str(os.system('ls'))
	# print(type(str(os.system('ls'))))
	unqiue_elements = []
	path = '/home/mholmes/.scripts/ls-diff/'
	if sys.argv[1] == 'store':
		f = open('temp', 'w')
		f.write(dir_contents) 
		f.close()
	elif sys.argv[1] == 'compare':
		f = open(path)
		previous_content = f.read()
		f.close()

		l1 = previous_content.split()
		l2 = dir_contents.split()
		unqiue_elements = get_list_differnt_elements(l1, l2)
		print(unqiue_elements)

main()