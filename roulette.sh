#!/bin/bash


get_random_numbers(){
	#get seed value
	seed=$(./surf)

	#get random numbers
	numbers=$(python randomizer.py $seed)
	
	#print out responses
	#echo $numbers
}

#welcome user and ask how much money they want to play with
echo "           Welcome to D casino!     		 "
echo "How much money would you like to play with?"

#read in money from user
read money
echo "You are playing with $money dollars"

#while loop for python game
while [ $money -gt 0 ]
do
	get_random_numbers
		
	echo $numbers
	#python roullete goes here 
	money=0	
	#if user wants to stop playing
	#break

done 

#goodbye message
echo "Thanks for playing!"
echo "You finished with $money dollars"


#random tests
export MONEY='4'
printenv | grep MONEY
