#!/usr/bin/env python
# Author: Chimera Security
# URL: http://www.chimera-security.com
# Tweet!: @ChimeraSecurity

# Project: OSINTharvest
# Module: LISTharvest
# Version: 0.1 (20/09/13)
# Readme: ../OSINTharvest/Readme.txt

# Import the libs
import os
import datetime
import urllib

# Set output directory
OUTPUT_DIR = 'output/LISTharvest/' # location of downloaded lists..
SOURCELIST = 'sources/LISTharvest_sources.txt' # self explanatory..
LOGFILE    = 'logs/LISTharvest.log' # incase shit goes south..

# Open up the log file, write the header
f = open(LOGFILE, 'w')
f.write("OSINTharvest v0.1\nAuthor: Chimera Security\n\nInitiating logging...\n")

print("Running LISTharvest. Please wait..")
# For every line in the source, do the following
for source in open(SOURCELIST):

    # Create the timestamp and present dl start info
    now = datetime.datetime.today()
    f.write( now.strftime("%Y-%m-%d %H:%M:%S") + " - Initiating Download: " + source)
    
    # Grab the filename from the source list
    name = source.rsplit(',', 1)[-1]
    
    # Define the url
    url = source.rsplit(',', 1)[-0]
    
    # Combine the name and output dir
    filename = os.path.join(OUTPUT_DIR, name)
    
    # Download
    urllib.urlretrieve(url, filename)
    #print( now.strftime("%Y-%m-%d %H:%M:%S") + " - Download Complete: " + name)
    
    # Show outcome of download
    f.write( now.strftime("%Y-%m-%d %H:%M:%S") + " - Download Successful: " + name)

    
# Show overall outcome of script
print("===================================\nAll downloads completed successfully\n")
f.close()    