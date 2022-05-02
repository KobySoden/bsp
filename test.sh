#!/bin/bash




for ((i=0; i<30; i++))
	do
	#get seed value
	seed=$(./surf)

	#get random numbers
	python randomizer.py $seed
done


