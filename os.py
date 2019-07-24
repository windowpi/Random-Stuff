#!/usr/env/bin python3 
import os
import time
import subprocess
import sys

# kilobyte to gigabyte
gb = 1024 ** 3

# print the sytem info
print(os.uname())

# print filesystem size
statvfs = os.statvfs('/')
fileSize = statvfs.f_frsize * statvfs.f_blocks

print ( 'SDCard:', (fileSize / gb), 'GB')

# print cpu temp
def measure_temp():
	temp = os.popen("vcgencmd measure_temp").readline()
	return (temp.replace("temp=", ""))

#print (measure_temp())
while True:   
    sys.stdout.write(measure_temp())
    sys.stdout.flush()
    time.sleep(0.5)
'''	
	print (measure_temp())
	time.sleep(5)
'''

