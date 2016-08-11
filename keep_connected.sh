#!/bin/sh

# This script is useful for keeping the Internet connected
# when connected via Mobile tethering.
# Pings http://goo.gl each $time (3) seconds.

# Set time equal to the time after which you want to ping the $website.
# Currently, it's set to 3 seconds.
time=3

# Website to ping.
website=goo.gl

# Wait for $time and ping $website only once.
while true
do
    sleep $time
    ping -c 1 $website
done
