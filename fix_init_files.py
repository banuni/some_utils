import os
import shutil
import sys

GOOD_CONTENT = ['# -*- coding: utf-8 -*-\n', 'from __future__ import unicode_literals\n']

def handle_file(path, path_to_good_file):
	data = open(path, 'r').readlines()
	if data == GOOD_CONTENT:
		return False
	if len(data) < 6:
		print(data)
		print (path, len(data))
		# this is a "stop" that lets the user to decide if the file should be overridden
		# you can change this part to your needs
		change = raw_input()
		if change == 'y':
			os.remove(path)
			shutil.copy(path_to_good_file, path)
			return True
	return False
		

def main(path_to_good_file):
	changed = []
	for root, dirs, files in os.walk(os.getcwd()):
		for filename in files:
			path = os.path.join(root, filename)
			if filename == "__init__.py":
				is_changed = handle_file(path, path_to_good_file)
				if is_changed:
					changed.append(path)
	print(changed)
	
if __name__ == "__main__":
	if len(sys.argv) != 2:	
		print "Usage: {} <path_to_good_file>".format(sys.argv[0])
		sys.exit(1)
	main(sys.argv[1])