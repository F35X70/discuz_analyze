# -*- coding: utf-8 -*-
import re
def ReadContent(file_name):
	with file(file_name,"r") as file_open:
		file_lines = file_open.readlines()
		for x in xrange(len(file_lines)):
			file_lines[x] = file_lines[x].strip("\n")
			file_lines[x] = file_lines[x].split(";")
	return file_lines
if __name__ == '__main__':
	feedback_name = "discuz.txt"
	file_content = ReadContent(feedback_name)
	for i in file_content:
		print i