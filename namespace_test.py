# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jul 15, 2011 7:57:54 PM$"

import mymodule1
import mymodule2
print "My name is %s" % __name__
if __name__ == "__main__":    
    print (mymodule2.myage - mymodule1.myage) == (mymodule2.year - mymodule1.year)
