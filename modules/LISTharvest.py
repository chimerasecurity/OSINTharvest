#!/usr/bin/env python
# Author: Chimera Security
# URL: http://www.chimera-security.com
# Tweet!: @ChimeraSecurity

# Project: OSINTharvest
# Module: LISTharvest
# Version: 0.1 (20/09/13)
# Readme: ../OSINTharvest/Readme.txt

# Import the libs
import os           # Needed for download paths
import datetime     # Needed for timestamps in logs
import urllib       # Needed for downloads

# Set output directory
OUTPUT_DIR = 'output/LISTharvest/'              # location of downloads
SOURCELIST = 'sources/LISTharvest_sources.txt'  # defined sources in text file
LOGFILE    = 'logs/OSINTharvest.log'            # logging output

# to be uncommented during testing as not to write logs to repo
# LOGFILE   = 'xxx.log'


# Open up the log file, write the header
f = open(LOGFILE, 'w')

# write the module launch to log w/timestamp
f.write( now.strftime("%Y-%m-%d %H:%M:%S") + " - LISTharvest" + " - Module launched")

# print launch message
print("Launching LISTharvest. Please wait..")

# For every line in the source, do the following
for source in open(SOURCELIST):

    # Define <now>
    now = datetime.datetime.today()
    
    # Grab the filename from the source list
    name = source.rsplit(',', 1)[-1]
    
    # Define the url
    url = source.rsplit(',', 1)[-0]
    
    # Combine the name and output dir
    filename = os.path.join(OUTPUT_DIR, name)
    
    # Download
    urllib.urlretrieve(url, filename)
    
    # Show outcome of download
    f.write( now.strftime("%Y-%m-%d %H:%M:%S") + " - LISTharvest" + " - Download Successful: " + name)

    
# Show overall outcome of script
print("===================================\nAll downloads completed successfully\n")

# write out completion entry to log
f.write( now.strftime("%Y-%m-%d %H:%M:%S") + " - LISTharvest" + " - All downloads complete")

# close the log file
f.close()    