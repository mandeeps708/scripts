#!/bin/sh
#This script takes the screenshot of current focused window and saves 
#it in a folder say ~/Desktop/screenshots. This location can be modified 
#by changing the path variable below.
path=~/Desktop/screenshots
mkdir -p $path
gnome-screenshot --file=$path/Myscreenshot`date +%I.%M.%S`.png -B -w
