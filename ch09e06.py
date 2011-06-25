# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jun 25, 2011 4:50:09 PM$"

def exercise06():
    """
    >>> junk = [3,7,9,10,13,17,21,24,27]
    >>> 13 in junk
    True
    >>> del junk[4]
    >>> junk
    [3, 7, 9, 10, 17, 21, 24, 27]
    >>> del junk[2:7]
    >>> junk
    [3, 7, 27]
    >>> nlist = [[None,None,17],[None,5],[None,0]]
    >>> nlist[2][1]
    0
    >>> nlist[0][2]
    17
    >>> nlist[1][1]
    5
    >>> import string
    >>> message = 'this??and??that'
    >>> string.split(message, '??')
    ['this', 'and', 'that']
    """
    junk = [3,7,9,10,13,17,21,24,27]
    13 in junk
    del junk[4]
    junk
    del junk[2:8]
    junk
    nlist = [[None,None,17],[None,5],[None,0]]
    nlist[2][1]
    nlist[0][2]
    nlist[1][0]
    import string
    message = "this??and??that"
    string.split(message)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    exercise06()
