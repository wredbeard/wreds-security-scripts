#!/usr/bin/env python3
import os

print("Warning! This program will nuke your file!")
print("\nThe file will be overwritten with 00. Use at your own risk.")
    
fileToOverwrite = input("File name > ")
writeConfirm = input("Are you sure you want to nuke this file? [Y/n]")

if writeConfirm == "Y":
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, fileToOverwrite)
    file_info = os.stat(filename)
    size = file_info.st_size
    
    for i in range(10):   
        f = open(filename, "w")
        f.seek(size)
        f.write("\x00")
        f.close()

    print("File overwritten!")
else:
    print("File not overwritten!")
