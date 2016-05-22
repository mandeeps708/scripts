#!/bin/sh

# Save all mdb files to a list
ls *.mdb > list

while read line;
do 
	# save database tables in corresponding dbname.tab file
	mdb-tables $line -1 >$line.tab
	echo $line

	# create a new directory for each database
	mkdir $line-DIR

	while read table
	do
		echo $table
		echo "============"
		
		# export table to csv file in corresponding directory
		mdb-export $line "$table" >$line-DIR/$table.csv
	done<$line.tab; 
done<list
