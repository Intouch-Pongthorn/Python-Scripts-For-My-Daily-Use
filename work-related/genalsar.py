import os
import glob
import datetime

#path to the sar folder
path = "/Users/pongthornchumpoo/MFEC/PM_node1_20032023/sa"
#fetchs only sarXX.file into the list
files_list = [file for file in glob.glob(f"{path}/sar[0-9][0-9]")]
#sorts sarXX.file from the list above by created date
files_list.sort(key = lambda t: os.stat(t).st_birthtime)
#print number of sar files and show their names and time of createtion
print(len(files_list))
for file in files_list:
    print(file, datetime.datetime.fromtimestamp(os.stat(file).st_birthtime))

#creates a new file called "all_sar.txt" and append each sarXX file to it
all_sar = open(f"{path}/all_sar.txt",'a')
for file in files_list:
    current_file = open(file,'r')
    for line in current_file:
        all_sar.write(line)

current_file.close()
all_sar.close()



print("complete")