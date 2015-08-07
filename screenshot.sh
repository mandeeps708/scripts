#!/bin/sh
path=~/Desktop/screenshots
mkdir -p $path
xwd -root | convert - $path/Myscreenshot`date +%I.%M.%S`.png
