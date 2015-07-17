#!/bin/bash
let count=1
while read line
do
sed -i -e s/'variable('$count')'/$line/ filename
((count++))
done<list
