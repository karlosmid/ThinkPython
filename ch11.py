# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Sep 29, 2011 8:53:38 PM$"

def swap(x, y):      # incorrect version
     print  "before swap statement: id(x):", id(x), "id(y):", id(y)
     x, y = y, x
     print  "after swap statement: id(x):", id(x), "id(y):", id(y)

if __name__ == "__main__":
    a, b = 0, 1
    print  "before swap function call: id(a):", id(a), "id(b):", id(b)
    print a, b
    swap(a, b)
    print  "after swap function call: id(a):", id(a), "id(b):", id(b)
    print a, b
