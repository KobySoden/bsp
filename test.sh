#!/bin/bash


for ((i=0; i<1000; i++))
	do
	#get seed value
	seed=$(./surf)

	#get random numbers
	numbers=$(python randomizer_test.py $seed)
	
	#print out responses
	python histogram.py $numbers
	echo "trial number: $i"
	echo $numbers
done

echo "summary of values can be found in test.txt"
