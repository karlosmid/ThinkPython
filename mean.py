# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jul 25, 2011 8:15:34 PM$"

if __name__ == "__main__":
    from sys import argv
    inputNumbers = argv[1:]
    print sum(map(float,inputNumbers))/len(inputNumbers)
