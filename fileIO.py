
import os
import time

directory = r'C:\A'
modification_time = os.path.getmtime(directory)
local_time = time.ctime(modification_time)
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        print(os.path.join(directory, filename, local_time))
    else:
        continue





