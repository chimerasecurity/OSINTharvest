#!/usr/bin/env python
# Author: Chimera Security
# URL: http://www.chimera-security.com
# Tweet!: @ChimeraSecurity

# Project: OSINTharvest
# Module: WEBharvest
# Version: 0.1 (20/09/13)
# Readme: ../OSINTharvest/Readme.txt

# Import required li
import re           # required for regex
import urllib2      # required for http
import datetime     # required for timestmps
import os
import csv

OUTPUT_FILE = '../output/WEBharvest/results.csv'   # Output directory
SOURCELIST = '../sources/WEBharvest_sources.txt'   # Sourcelist
LOGFILE = '../logs/OSINTharvest.log'               # logs
now = datetime.datetime.today()

# Determine regex for IP / HNAMEs
IP = r"\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b"

# Open up the log file, write the header
f = open(LOGFILE, 'w')


# write the module launch to log w/timestamp
f.write( now.strftime("%Y-%m-%d %H:%M:%S") + " - WEBharvest" + " - Module launched")

# print launch message
print("Launching WEBharvest. Please wait..")

# For every line in the source, do the following
for source in open(SOURCELIST):

    # Define <now>
    now = datetime.datetime.today()
    
    # Grab the filename from the source list
    name = source.rsplit(',', 1)[-1]
    
    # Define the url
    url = source.rsplit(',', 1)[-0]
    
    # Scrape
    src = urllib2.urlopen(url)
    data = src.read()
    
    # search and print matching strings
    result = re.compile(IP)
    h = result.findall(data)
    
    csv.writer(open(OUTPUT_FILE, 'wb')).writerows(h)
    
    # Show outcome of download
    f.write( now.strftime("%Y-%m-%d %H:%M:%S") + " - WEBharvest" + " - Scrape Successful: " + name)




