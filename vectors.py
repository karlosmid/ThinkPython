# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jun 25, 2011 5:09:49 PM$"

def exercise07():
    """
    >>> add_vectors(1,[0,0])
    -1
    >>> add_vectors([1,2,3],[1,2])
    -2
    >>> add_vectors([1, 0], [1, 1])
    [2, 1]
    >>> add_vectors([1, 2], [1, 4])
    [2, 6]
    >>> add_vectors([1, 2, 1], [1, 4, 3])
    [2, 6, 4]
    >>> add_vectors([11, 0, -4, 5], [2, -4, 17, 0])
    [13, -4, 13, 5]
    """
def exercise08():
    """
    >>> scalar_mult([1,2],[1,2])
    -1
    >>> scalar_mult([1,2],5)
    -1
    >>> scalar_mult(5, [1, 2])
    [5, 10]
    >>> scalar_mult(3, [1, 0, -1])
    [3, 0, -3]
    >>> scalar_mult(7, [3, 0, 5, 11, 2])
    [21, 0, 35, 77, 14]
    """
def exercise09():
    """
    >>> dot_product(1,[1,2])
    -1
    >>> dot_product([1,2],[1,2,3])
    -2
    >>> dot_product([1, 1], [1, 1])
    2
    >>> dot_product([1, 2], [1, 4])
    9
    >>> dot_product([1, 2, 1], [1, 4, 3])
    12
    >>> dot_product([2, 0, -1, 1], [1, 5, 2, 0])
    0
    """
def dot_product(u,v):
    if not isinstance(u,list) or not isinstance(v,list):
        return -1
    elif len(u) != len(v):
        return -2
    else:
        rez = []
        for (index,item) in enumerate(u):
            rez.append(item*v[index])
        return sum(rez)

def scalar_mult(s,v):
    if not isinstance(s,int) or not isinstance(v,list):
        return -1    
    else:
        rez = []
        for item in v:
            rez.append(s*item)
        return rez
def add_vectors(u,v):
    if not isinstance(u,list) or not isinstance(v,list):
        return -1
    elif len(u) != len(v):
        return -2
    else:
        rez = []
        for (index,item) in enumerate(u):
            rez.append(item+v[index])
        return rez

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    exercise07()
    exercise08()
    exercise09()
