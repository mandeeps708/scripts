#!/bin/sh
#This script takes the screenshot of area selected by two mouse clicks and 
#saves it in a folder say ~/Desktop/screenshots. This location can be modified 
#by changing the path variable below. Add shortcut to this script in the 
#System Settings> Keyboard shortcuts.
path=~/Desktop/screenshots
mkdir -p $path
gnome-screenshot --file=$path/Myscreenshot`date +%I.%M.%S`.png -B -a
