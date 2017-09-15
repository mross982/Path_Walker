# Import the os module, for the os.walk function
import os
import sys

# Set the directory you want to start from
rootDir = 'G:\Quality\Experience_and_Performance_Improvement\Programs & Projects\DSRIP'

# with open(logDir, 'w') as f:
dirs = 0
files = 0
for dirName, subdirList, fileList in os.walk(rootDir):
    # print('Found directory: ', dirName)
    dirs = dirs + 1
    for fname in fileList:
        files = files + 1
        # print('\t%s' % fname)

print('There were ', str(dirs), ' directories and ', str(files), ' files')

