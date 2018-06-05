import os, shutil

PATH_TO_GOOD_FILE = r"C:\Users\Nuni\PycharmProjects\mvp\server\DeceptionStation\decoymanager\manuf\test\__init__.py"
GOOD_CONTENT = ['# -*- coding: utf-8 -*-\n', 'from __future__ import unicode_literals\n']

def handle_file(path):
	data = open(path, 'r').readlines()
	if data == GOOD_CONTENT:
		return False
	if len(data) < 6:
		print(data)
		print (path, len(data))
		change = raw_input()
		if change == 'y':
			os.remove(path)
			shutil.copy(PATH_TO_GOOD_FILE, path)
			return True
	return False
		

changed = []
for root, dirs, files in os.walk(os.getcwd()):
	for filename in files:
		path = os.path.join(root, filename)
		if filename == "__init__.py":
			is_changed = handle_file(path)
			if is_changed:
				changed.append(path)
print(changed)
