#===============================================================================
# Steam Key Activator for Linux
# v1.0
# Copyright (C) 2015 by Mykro, licensed under GPLv2 for free use/modification.
#
# See the accompanying readme.txt for installation and usage instructions.
#
# Developer Notes:
# - For some reason the built-in Autokey mouse/keyboard classes don't work
#   for me, so this script makes shell calls to xte instead.
# - Tested with Ubuntu 14.04
#===============================================================================

# MODIFY AS NEEDED

# Co-ordinates for the top-left corner of the Steam window.
# These values will vary depending on your desktop & taskbar.
# It is ok to be a couple of pixels out.
steamx = 80
steamy = 35

# YOU SHOULD NOT NEED TO MODIFY BELOW THIS LINE

import time
import sys

while True:
    # Activate the Steam window and move it to our 0,0 position.
    window.activate("Steam.Steam", switchDesktop=True, matchClass=True)
    window.resize_move("Steam.Steam", xOrigin=0, yOrigin=0, width=-1, height=-1, matchClass=True)

    # Position the mouse so that the user can confirm the offset co-ordinates.
    system.exec_command("xte 'mousemove %d %d'" % (steamx,steamy), False)

    # Prompt for a key.
    retCode, steamkey = dialog.input_dialog("Enter Key", 
    "IMPORTANT:\n" +
    "\n" +
    "1) Your mouse cursor should now be at the exact top-left corner of the\n" + 
    "      Steam window in such a way that it has turned into a 'resize' cursor.\n" +
    "      If not, you should click Cancel and edit the script.\n" +
    "\n" +
    "2) After clicking OK, don't touch the mouse/keyboard until this prompt re-appears.\n" +
    "\n" +
    "Please enter a Steam Key:")

    if retCode != 0:
        sys.exit()

    # Re-activate the Steam window just in case
    window.activate("Steam.Steam", switchDesktop=True, matchClass=True)
    window.resize_move("Steam.Steam", xOrigin=0, yOrigin=0, width=-1, height=-1, matchClass=True)

    time.sleep(1)

    # Click on 'Games' menu.
    system.exec_command("xte 'mousemove %d %d'" % (steamx + 180,steamy + 20), False)
    system.exec_command("xte 'mouseclick 1'", False)
    time.sleep(1)

    # Menu drops down.  Click on 'Activate a product' option.
    system.exec_command("xte 'mousemove %d %d'" % (steamx + 180,steamy + 75), False)
    system.exec_command("xte 'mouseclick 1'", False)
    time.sleep(1)
        
    # New window appears.  Click Next button.
    system.exec_command("xte 'mousemove %d %d'" % (steamx + 970,steamy + 790), False)
    system.exec_command("xte 'mouseclick 1'", False)
    time.sleep(1)
   
    # Licence appears.  Click "I agree" button (same position).
    system.exec_command("xte 'mousemove %d %d'" % (steamx + 970,steamy + 790), False)
    system.exec_command("xte 'mouseclick 1'", False)
    time.sleep(1)
    
    # Enter the product code
    system.exec_command("xte 'str %s'" % steamkey, False)
    time.sleep(1)
    
    # Click "Next" button (same position).
    system.exec_command("xte 'mousemove %d %d'" % (steamx + 970,steamy + 790), False)
    system.exec_command("xte 'mouseclick 1'", False)

    # takes a while to activate...
    time.sleep(10)

    # There are three possible UIs now.
    # By happy coincidence the next two button presses work for all three UIs.
    
    # If product already owned: The button is greyed out, but click it anyway.
    # Nothing to install: The button is greyed out, but click it anyway.
    # Something to install: Click "Next" button (same position).
    system.exec_command("xte 'mousemove %d %d'" % (steamx + 970,steamy + 790), False)
    system.exec_command("xte 'mouseclick 1'", False)
    time.sleep(1)
    
    # If product already owned: Click "Finish" button at the far right.
    # Nothing to install: Click "Finish" button at the far right.
    # Something to install: Click "Cancel" button at the far right.
    system.exec_command("xte 'mousemove %d %d'" % (steamx + 1080,steamy + 790), False)
    system.exec_command("xte 'mouseclick 1'", False)
    time.sleep(2)
