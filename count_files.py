#!/usr/bin/python
import os
import os.path
import re 
import sys
import datetime
import shutil
import zipfile
import subprocess
import ConfigParser
import time
import logging
import logging.handlers

extract_log_dir = "D:/Logs"
output_dir = "D:/CPS"
month = "Dec"

# Find the string and work on it 
for f in os.listdir(extract_log_dir):
	print "Starting " + f
	file = open(extract_log_dir + '/' + f,"r")
	f1 = file.readlines()
	important = []
	keep_phrases = ["WARNING",
					"Identity="]

	file1 = open(output_dir + "/" + month + ".txt","a+")

	for line in f1:
		for phrase in keep_phrases:
			if phrase in line:
				file1.writelines(line)
				break
	print "Done With " + f
	

	

