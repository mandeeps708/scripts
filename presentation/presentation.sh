#The purpose of this script is to take input from a file 'list', 
#then find and replace the 'variable()'' with names fetched from file 'list'.

#!/bin/bash
let count=1
while read line
do
sed -i -e s/'variable('$count')'/$line/ filename
((count++))
done<list

# http://github.com/mandeeps708
