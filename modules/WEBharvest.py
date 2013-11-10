#!/usr/bin/env python
# Author: Chimera Security
# URL: http://www.chimera-security.com
# Tweet!: @ChimeraSecurity

# Project: OSINTharvest
# Module: WEBharvest
# Version: 0.1 (20/09/13)
# Readme: ../OSINTharvest/Readme.txt

# Import required libs
import re           # required for regex
import urllib2      # required for http

# Determine regex for IP / HNAMEs
IP = r"\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b"
#HNAME = 

# src defines the source web page, possibly change for user input?
src = urllib2.urlopen("http://blog.threatexpert.com/2010/01/trojanhydraq-part-ii.html")
data = src.read()

# search and print matching strings
result = re.compile(IP)
print result.findall(data)