# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jul 5, 2011 7:25:59 PM$"

def replace(s, old, new):
    """
    >>> replace('Mississippi', 'i', 'I')
    'MIssIssIppI'
    >>> s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
    >>> replace(s, 'om', 'am')
    'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!'
    >>> replace(s, 'o', 'a')
    'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!'
    """
    print "'"+new.join(s.split(old))+"'"
def multiples_of(num, numlist):
    """
    >>> multiples_of('a',[1,2,3,4])
    -2
    >>> multiples_of(2,[1,2,3,4])
    [2, 4, 6, 8]
    >>> multiples_of(2,2)
    -1
    """
    if not isinstance(numlist,list):
        return -1
    if not isinstance(num,int):
        return -2
    print [num*x for x in numlist]
def only_odds(numbers):
    """
    >>> only_odds([1, 3, 4, 6, 7, 8])
    [1, 3, 7]
    >>> only_odds([2, 4, 6, 8, 10, 11, 0])
    [11]
    >>> only_odds([1, 3, 5, 7, 9, 11])
    [1, 3, 5, 7, 9, 11]
    >>> only_odds([4, 0, -1, 2, 6, 7, -4])
    [-1, 7]
    >>> nums = [1, 2, 3, 4]
    >>> only_odds(nums)
    [1, 3]
    >>> nums
    [1, 2, 3, 4]
    """
    print [x for x in numbers if x%2!=0]
def only_evens(numbers):
    """
    >>> only_evens([1, 3, 4, 6, 7, 8])
    [4, 6, 8]
    >>> only_evens([2, 4, 6, 8, 10, 11, 0])
    [2, 4, 6, 8, 10, 0]
    >>> only_evens([1, 3, 5, 7, 9, 11])
    []
    >>> only_evens([4, 0, -1, 2, 6, 7, -4])
    [4, 0, 2, 6, -4]
    >>> nums = [1, 2, 3, 4]
    >>> only_evens(nums)
    [2, 4]
    >>> nums
    [1, 2, 3, 4]
    """
    print [x for x in numbers if x%2==0]
if __name__ == "__main__":
    import doctest
    doctest.testmod()
