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

extract_log_dir = "D:/hack_result/20-26jan"
#extract_log_dir = "D:/logs"
output_dir = "D:/hack_result"
result = "half-5-jan"

# Find the string and work on it 
for f in os.listdir(extract_log_dir):
	print "Starting " + f
	file = open(extract_log_dir + '/' + f,"r")
	f1 = file.readlines()
	important = []
	keep_phrases = ["WhiteHat",
					"MrNervous",
					"whitehat",
					"mrnervous",
					"union", "nslookup", "%20", "exec", "drop", "--", "password",".php", "@@version", "user()", "execute", "declare", "cast", "'", "'+", "varchar", "403", "404", "hat"]

	file1 = open(output_dir + "/" + result + ".txt","a+")

	for line in f1:
		for phrase in keep_phrases:
			if phrase in line:
				file1.writelines(phrase)
				file1.writelines("   ")
				file1.writelines(line)
				break
	print "Done With " + f
	

	

