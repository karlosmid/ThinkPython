# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jun 29, 2011 7:11:14 PM$"

import copy

def add_matrices(m1, m2):
    """
    >>> add_matrices(1,[0])
    -1
    >>> add_matrices([1,0],[0])
    -2
    >>> a = [[1, 2], [3, 4]]
    >>> b = [[2, 2], [2, 2]]
    >>> add_matrices(a, b)
    [[3, 4], [5, 6]]
    >>> c = [[8, 2], [3, 4], [5, 7]]
    >>> d = [[3, 2], [9, 2], [10, 12]]
    >>> add_matrices(c, d)
    [[11, 4], [12, 6], [15, 19]]
    >>> c
    [[8, 2], [3, 4], [5, 7]]
    >>> d
    [[3, 2], [9, 2], [10, 12]]
    """
    if not isinstance(m1,list) or not isinstance(m2,list):
        return -1
    elif len(m1) != len(m2):
        return -2
    rez = []
    for row in range(len(m1)):
        rez += [[0]*len(m1[0])]    
    for (iOuter,Outer) in enumerate(m1):
        for (iInner,Inner) in enumerate(Outer):
            try:                
                rez[iOuter][iInner] = m1[iOuter][iInner] + m2[iOuter][iInner]
            except IndexError, e:
                print e.message
                return -2
    print rez

def add_column(matrix):
    """
    >>> m = [[0, 0], [0, 0]]
    >>> add_column(m)
    [[0, 0, 0], [0, 0, 0]]
    >>> n = [[3, 2], [5, 1], [4, 7]]
    >>> add_column(n)
    [[3, 2, 0], [5, 1, 0], [4, 7, 0]]
    >>> n
    [[3, 2], [5, 1], [4, 7]]
    """
    mCopy = copy.deepcopy(matrix)
    for item in mCopy:
        item.append(0)
    print mCopy
def add_row(matrix):    
    """
    >>> m = [[0, 0], [0, 0]]
    >>> add_row(m)
    [[0, 0], [0, 0], [0, 0]]
    >>> n = [[3, 2, 5], [1, 4, 7]]
    >>> add_row(n)
    [[3, 2, 5], [1, 4, 7], [0, 0, 0]]
    >>> n
    [[3, 2, 5], [1, 4, 7]]
    """
    mCopy = copy.deepcopy(matrix)
    mCopy.append([0]*len(matrix[0]))
    print mCopy
if __name__ == "__main__":
    import doctest
    doctest.testmod()    
