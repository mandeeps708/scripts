#!/bin/sh
#This script is meant for taking screenshots of current screen and 
#storing them at a location say ~/Desktop/screenshots. This folder will 
#be automatically created if there is not one. The path may be changed 
#by changing the variable path below.
#One may add keyboard shortcut to run this script in 'System Settings'.
path=~/Desktop/screenshots
mkdir -p $path
sleep 5
xwd -root | convert - $path/Myscreenshot`date +%I.%M.%S`.png

