#!/usr/bin/env python
import os
import errno
from sys import argv as arg
from glob import glob
import datetime

def main():
    #path to the sar folder recieved from command-line 1st arg
    path = os.path.abspath(str(arg[1]))
    #path to all_sar.txt i.e. path/all_sar.txt
    alsar_location = os.path.join(path,"all_sar.txt")
    #fetchs only sarxx files from the directory
    sar_files = get_sar_files(path)
    try : 
        #deletes all_sar.txt if exists 
        os.path.exists(alsar_location) and os.remove(alsar_location)
        #opens all_sar.txt (if there's no  all_sar.txt file, this line creates the file)
        all_sar = open(alsar_location,'a')
        print("Writing all_sar.txt.....")
        #appends content from each sarxx file to all_sar.txt line by line
        for sar_file in sar_files:
            current_sar_file = open(sar_file,'r')
            for line in current_sar_file:
                all_sar.write(line)
        current_sar_file.close()
        all_sar.close()
    except OSError:
        pass
    print(f"Complete!...your all_sar.txt is already created in {alsar_location}")


def get_sar_files(path:str)->list[str]:
    #picks only sarXX.file into a list
    files_list = [file for file in glob(f"{path}\sar[0-9][0-9]")]
    #sorts sarXX.file from the list above by modified date
    files_list.sort(key = lambda file: os.stat(file).st_mtime)
    #raises an error if no sar files found in the directory and ends the program
    if len(files_list) == 0:
        raise FileNotFoundError(os.strerror(errno.ENOENT),f"no sar files found in {path}")
    print("Arranging sar files in order.......")
    #echos file names and time of modification on the terminal screen
    for file in files_list:
        print(file, datetime.datetime.fromtimestamp(os.stat(file).st_mtime))
    
    return files_list

if __name__ == "__main__":
    main()
