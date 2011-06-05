# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jun 5, 2011 3:44:27 PM$"

from gasp import *

def guess():    

    number = random_between(1, 1000)
    guesses = 0

    while True:
        guess = input("Guess the number between 1 and 1000: ")
        guesses += 1
        if guess > number:
            print "Too high!"
        elif guess < number:
            print "Too low!"
        else:
            print "\n\nCongratulations, you got it in %d guesses!\n\n" % guesses
            break

if __name__ == "__main__":
    guess()
