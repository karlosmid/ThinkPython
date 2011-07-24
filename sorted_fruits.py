# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jul 24, 2011 6:24:43 PM$"

if __name__ == "__main__":
    fFruits = open('unsorted_fruits.txt','r')
    lFruits = []
    for fruit in fFruits:
        lFruits.append(fruit)
    fFruits.close()
    fFruitsSorted = open('sorted_fruits.txt','w')
    lFruits.sort()
    for fruit in lFruits:
        fFruitsSorted.write(fruit)
    fFruitsSorted.close()
