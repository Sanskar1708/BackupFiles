import os
import time
import shutil

# Path from where the desired files has to be deleted 
folder = input("Enter the path: ")

# Number of days to check whether a file is older than it nor not
N = int(input("Enter the deleting date time: "))

# Changing the current directory to the given directory
os.chdir(folder)

# Listing all the files and folders present in the given folder
list_of_files = os.listdir()

# Getting current time
current_time = time.time()

# Seconds a day contains
day = 86400

# A loop for every files in the given folder
for i in list_of_files:

    # Getting path of every file and folder
    file_location = os.path.join(os.getcwd(), i)

    # Getting the time when the file was last modified
    file_time = os.stat(file_location).st_mtime

    # If the file is older than the 
    if(file_time < current_time - day*N):
        print(f" Delete : {i}")

        #If i is a file then removing it by os.remove()
        if os.path.isfile(file_location):
            os.remove(file_location)

        # If i is a folder then removing it by shutil.rmtree() 
        elif os.path.isdir(file_location):
            shutil.rmtree(file_location)