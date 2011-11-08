# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Nov 8, 2011 9:05:28 PM$"

#!/usr/bin/env python

import os
import sys


def getroot():
    if len(sys.argv) == 1:
        path = ''
    else:
        path = sys.argv[1]

    if os.path.isabs(path):
        tree_root = path
    else:
        tree_root = os.path.join(os.getcwd(), path)

    return tree_root


def getdirlist(path):
    dirlist = os.listdir(path)
    dirlist = [name for name in dirlist if name[0] != '.']
    dirlist.sort()
    return dirlist


def traverse(path):
    dirlist = getdirlist(path)

    for file in dirlist:
        path2file = os.path.join(path, file)

        if os.path.isdir(path2file):                        
            os.remove(path2file+'/trash.txt')
            if getdirlist(path2file):
                traverse(path2file)        


if __name__ == '__main__':
    root = getroot()
    traverse(root)    
