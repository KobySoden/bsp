#!/bin/bash

echo "Testing our random number generator"

for ((i=0; i<1000; i++))
	do
	echo "Generating seed value"
	seed=$(./surf)

	#get random numbers
	echo "Generating random numbers"
	numbers=$(python randomizer_test.py $seed)
	
	#print out responses
	python histogram.py $numbers
	echo "trial number: $i"
	echo $numbers
done

echo "summary of values can be found in test.txt"
