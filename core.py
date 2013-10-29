#!/usr/bin/env python
# Author: Chimera Security
# URL: http://www.chimera-security.com
# Tweet!: @ChimeraSecurity

# Project: OSINTharvest
# Module: Core
# Version: 0.1 (20/09/13)
# Readme: ../OSINTharvest/Readme.txt

# Import libs
import subprocess

# Set variables
LISTharvest = 'modules/LISTharvest.py'
WEBharvest = 'modules/WEBharvest.py'
PDFharvest = 'modules/PDFharvest.py'


# The cli menu
ans = True #variable for tracking user choice
print("""
________    _________.___ __________________                            
\       \  /   _____/|   |\      \__    ___/                            
 /   |   \ \_____  \ |   |/   |   \|    |                               
/    |    \/        \|   /    |    \    |                               
\_______  /_______  /|___\____|__  /____|                               
        \/        \/             \/                                     
  ___ ___    _____ ______________   _______________ ____________________
 /   |   \  /  _  \\______   \   \ /   /\_   _____//   _____/\__    ___/
/    ~    \/  /_\  \|       _/\   Y   /  |    __)_ \_____  \   |    |   
\    Y    /    |    \    |   \ \     /   |        \/        \  |    |   
 \___|_  /\____|__  /____|_  /  \___/   /_______  /_______  /  |____|   
       \/         \/       \/                   \/        \/            


        Please select a module:
        -------------------------------------------------------
        1. Launch LISTharvest
        2. Launch WEBharvest
        3. Launch PDFharvest
        0. Exit
        -------------------------------------------------------
        """)

while ans:
        try:
                ans= input("Select a module to launch:  ")
        
                if ans == 1:
                    subprocess.call("modules/LISTharvest.py")
                    
                elif ans == 2:
                    subprocess.call("modules/WEBharvest.py")
                   
                elif ans == 3:
                    subprocess.call("modules/PDFharvest.py")
                
                elif ans == 0:
                    print("now exiting..")
                    break
                
                
                else:
                        print("""
                        -----------------------      
                           :Invalid choice:
                        Please choose an option
                        -----------------------
                        1. Launch LISTharvest
                        2. Launch WEBharvest
                        3. Launch PDFharvest
                        -----------------------
                        """)
                
        except KeyboardInterrupt:
                print("  exiting")
                break
        



# how to exec
# subprocess.call("modules/LISTharvest.py", shell=True)