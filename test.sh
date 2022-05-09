#!/bin/bash


for ((i=0; i<1; i++))
	do
	#get seed value
	seed=$(./surf)

	#get random numbers
	numbers=$(python randomizer.py $seed)
	
	#print out responses
	echo $numbers
done

