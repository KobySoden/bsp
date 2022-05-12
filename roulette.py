import sys
import os

class Roulette():
    def __init__(self):
        self.numbers = []
        for i in range(1,len(sys.argv)):
            #print(i)
            #print(sys.argv[i])
            val = sys.argv[i]
            val = val.replace(",", "") 
            val = val.replace("[", "")
            val = val.replace("]", "")
            self.numbers.append(int(val))
        
        #self.numbers = sys.argv[1:-1].replace("[","").replace("]","").replace(" ","").split(",")
       # print(self.numbers)

        for i in range(len(self.numbers)):
            self.numbers[i] = int(self.numbers[i])
        self.money = int(sys.argv[-2])
        if sys.argv[-1] == "1":
            self.firstrun = True
        else:
            self.firstrun = False
        self.reds = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        self.blacks = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
        self.greens = [0,37]
        if self.firstrun:
            self.welcome()
        else:
            self.spin()
    
    def welcome(self):
        print("Welcome to Team D's Roulette Game!")
        print("You'll start with $100 to play with.")
        inp = input("Type 1 to see the betting odds, or type 2 to begin the game. ")
        while inp not in ["1", "2"]:
            print("Please input a 1 or a 2.")
            inp = input("Type 1 to see the betting odds, or type 2 to begin the game. ")
        if inp == "1":
            print("Betting on red/black or even/odd pays 1 to 1.")
            print("Betting on green pays 17 to 1.")
            print("Betting on an individual number pays 35 to 1.")
        else:
            self.spin()
            return
        inp = input("Begin game?: y/n ")
        while inp not in ["y", "n"]:
            inp = input("Begin game?: y/n ")
        if inp == "y":
            self.spin()
        else:
            self.exit(False)
    def spin(self):
        print("You have $" + str(self.money) + " remaining.")
        inp = input("Type 1 to bet on a color, 2 to bet on even/odd, or 3 to bet on an individual number. ")
        while inp not in ["1", "2", "3"]:
            print("Please input 1, 2, or 3.")
            inp = input("Type 1 to bet on a color, 2 to bet on even/odd, or 3 to bet on an individual number. ")
        if inp == "1":
            inp = input("Type 1 to bet on red, 2 to bet on black, or 3 to bet on green. ")
            while inp not in ["1", "2", "3"]:
                print("Please input 1, 2, or 3.")
                inp = input("Type 1 to bet on red, 2 to bet on black, or 3 to bet on green. ")
            bet = self.getbet()
            print("Spinning...")
            spin_result = self.numbers.pop()
            print("Landed on ", spin_result, "!")
            if (inp == "1" and spin_result in self.reds) or (inp == "2" and spin_result in self.blacks):
                print("You win $", bet, "!")
                self.money += int(bet)
            elif inp == "3" and spin_result in self.greens:
                print("You win $", 17*int(bet),"!")
                self.money += 17 * int(bet)
            else:
                print("You lose.")
                self.money -= int(bet)
        elif inp == "2":
            inp = input("Type 1 to bet on even or 2 to bet on odd. ")
            while inp not in ["1","2"]:
                print("Please input 1 or 2.")
                inp = input("Type 1 to bet on even or 2 to bet on odd. ")
            bet = self.getbet()
            print("Spinning...")
            spin_result = self.numbers.pop()
            print("Landed on ", spin_result, "!")
            if spin_result == 37:
                if inp == "1":
                    print("You win $", bet, "!")
                    self.money += int(bet)
                else:
                    print("You lose.")
                    self.money -= int(bet)
            elif (inp == "1" and spin_result % 2 == 0) or (inp == "2" and spin_result % 2 == 1):
                print("You win $", bet, "!")
                self.money += int(bet)
            else:
                print("You lose.")
                self.money -= int(bet)
        elif inp == "3":
            inp = input("Please type the number you would like to bet on. ")
            legal_inputs = list(range(0, 38))
            for i in range(len(legal_inputs)):
                legal_inputs[i] = str(legal_inputs[i])
            legal_inputs.append("00")
            while inp not in legal_inputs:
                print("Please input a number from 0 to 36 including 00.")
                inp = input("Please type the number you would like to bet on. ")
            if inp == "00":
                inp = "37"
            bet = self.getbet()
            print("Spinning...")
            spin_result = self.numbers.pop()
            print("Landed on ", spin_result, "!")
            if int(inp) == spin_result:
                print("You win $", 35 * int(bet), "!")
                self.money += 35 * int(bet)
            else:
                print("You lose.")
                self.money -= int(bet)
        if self.money == 0:
            print("You ran out of money! Game over.")
            self.exit(False)
            return
        cont = input("Continue? y/n: ")
        while cont not in ["y","n"]:
            cont = input("y/n?: ")
        if cont == "n":
            self.exit(False)
        else:
            if len(self.numbers) == 0:
                self.exit(True)
            else:
                self.spin()
    def getbet(self):
        bet = input("How much would you like to bet? ")
        valid_bet = False
        while not valid_bet:
            if not bet.isnumeric():
                print("Please input a number.")
                bet = input("How much would you like to bet? ")
            elif int(bet) > self.money:
                print("Please input a number less than or equal to your current balance ($", self.money, ")")
                bet = input("How much would you like to bet? ")
            else:
                valid_bet = True
        return int(bet)
    def exit(self, cont):
        if not cont:
            print("Thanks for playing!")
            f = open("tmp", "w")
            f.write(str(0))
            f.close()
        else:
            f = open("tmp", "w")
            f.write(str(self.money))
            f.close()
        
            
    
x = Roulette()
