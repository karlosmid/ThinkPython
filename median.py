# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jul 25, 2011 8:26:09 PM$"

if __name__ == "__main__":
    from sys import argv
    inputNumbers = map(int,argv[1:])
    inputNumbers.sort()
    if len(inputNumbers)%2 == 0:
        print (inputNumbers[len(inputNumbers)/2] +\
        inputNumbers[len(inputNumbers)/2-1])/2.0
    else:
        print inputNumbers[len(inputNumbers)/2]
