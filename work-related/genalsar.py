#!/usr/bin/env python
import os
import errno
from sys import argv as arg
from glob import glob
import datetime

def main():
    #path to the sar folder recieved from command-line 1st arg
    path = os.path.abspath(str(arg[1]))
    #get only sarxx files from the directory
    sar_files = get_sar_files(path)

    try :
        #deletes all_sar.txt if existed 
        os.remove(f"{path}/all_sar.txt")
        #creates all_sar.txt if not existed
        all_sar = open(f"{path}/all_sar.txt",'a')
        #appends sarxx file to all_sar.txt line by line
        for sar_file in sar_files:
            current_sar_file = open(sar_file,'r')
            for line in current_sar_file:
                all_sar.write(line)

        current_sar_file.close()
        all_sar.close()
    except OSError:
        pass
    print("complete!")


def get_sar_files(path:str)->list[str]:
    #fetchs only sarXX.file into the list
    files_list = [file for file in glob(f"{path}/sar[0-9][0-9]")]
    #sorts sarXX.file from the list above by created date
    files_list.sort(key = lambda file: os.stat(file).st_birthtime)
    #raises an error if sar files not found in the directory
    if len(files_list) == 0:
        raise FileNotFoundError(os.strerror(errno.ENOENT),f"no sar files found in {path}")
    #list file names and time of createtion
    for file in files_list:
        print(file, datetime.datetime.fromtimestamp(os.stat(file).st_birthtime))
    
    return files_list


main()
