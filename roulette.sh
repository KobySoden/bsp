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
echo "You are playing with $money dollars"
echo "In case you don't know, here are your odds!"
echo "Betting on red/black or even/odd pays 1 to 1."
echo "Betting on green pays 17 to 1."
echo "Betting on an individual number pays 35 to 1."
#while loop for python game
#first run
while [ $money -gt 0 ]
do
	get_random_numbers
		
	#python roullete goes here 
	python roulette.py $numbers $money 0	
	
	money=$(cat tmp)

done 

#goodbye message
#echo "Thanks for playing!"
#echo "You finished with $MONEY dollars"


#random tests
#export MONEY='4'
#printenv | grep MONEY
