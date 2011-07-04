# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jun 29, 2011 7:11:14 PM$"

import copy

def matrix_mult(m1, m2):
   """
   >>> matrix_mult([[1, 2], [3,  4]], [[5, 6], [7, 8]])
   [[19, 22], [43, 50]]
   >>> matrix_mult([[1, 2, 3], [4,  5, 6]], [[7, 8], [9, 1], [2, 3]])
   [[31, 19], [85, 55]]
   >>> matrix_mult([[7, 8], [9, 1], [2, 3]], [[1, 2, 3], [4, 5, 6]])
   [[39, 54, 69], [13, 23, 33], [14, 19, 24]]
   """
   rez = []
   for row in range(len(m1)):
        rez += [[0]*len(m2[0])]
   for i in range (len(m1)):
       for j in range (len(m2[0])):
           rez[i][j] = row_times_column(m1, i, m2, j)
   print rez
def row_times_column(m1, row, m2, column):
    """
    >>> print row_times_column([[1,2],[3,4]],1,[[1,2,3],[1,2,3],[1,2,3]],0)
    -2
    >>> print row_times_column(1,2,[[1,2],[3,4]],4)
    -1
    >>> print row_times_column([[1,2],[2,4]],2,3,4)
    -1
    >>> print row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 0)
    19
    >>> print row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 1)
    22
    >>> print row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 0)
    43
    >>> row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 1)
    50
    """    
    if not isinstance(m1,list) or not isinstance(m2,list):
        return -1
    elif len(m1[0]) != len(m2):
        return -2
    rez = 0    
    for i in range(len(m1[0])):               
        rez = rez + m1[row][i] * m2[i][column]
    return rez

def scalar_mult(s, m):
    """
    >>> scalar_mult(1,2)
    -1
    >>> scalar_mult([1],[[1,2]])
    -1
    >>> a = [[1, 2], [3, 4]]
    >>> scalar_mult(3, a)
    [[3, 6], [9, 12]]
    >>> b = [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
    >>> scalar_mult(10, b)
    [[30, 50, 70], [10, 10, 10], [0, 20, 0], [20, 20, 30]]
    >>> b
    [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
    """
    rez = copy.deepcopy(m)
    if not isinstance(m,list) or not isinstance(s,int):
        return -1
    for (o,outer) in enumerate(m):
        for (i,inner) in enumerate(outer):
            rez[o][i] = s * rez[o][i]
    print rez
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
