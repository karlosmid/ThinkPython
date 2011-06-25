# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jun 25, 2011 3:45:16 PM$"

def exercise02():
    """
    >>> a_list = [None,None,None,42,None,None,'Ni!',None]
    >>> a_list[3]
    42
    >>> a_list[6]
    'Ni!'
    >>> len(a_list)
    8
    >>> b_list = [None,'Stills','Nash']
    >>> b_list[1:]
    ['Stills', 'Nash']
    >>> c_list = ['Young']
    >>> group = b_list + c_list
    >>> group[-1]
    'Young'
    >>> mystery_list = ['peace','justice','equality']
    >>> 'war' in mystery_list
    False
    >>> 'peace' in mystery_list
    True
    >>> 'justice' in mystery_list
    True
    >>> 'oppression' in mystery_list
    False
    >>> 'equality' in mystery_list
    True
    >>> range(5,18,4)
    [5, 9, 13, 17]
    """
    a_list = [None,None,None,42,None,None,'Ni!',None]
    a_list[3]
    a_list[6]
    len(a_list)
    b_list = [None,'Stills','Nash']
    b_list[1:]
    c_list = ['Young']
    group = b_list + c_list
    group[-1]
    mystery_list = ['peace','justice','equality']
    'war' in mystery_list
    'peace' in mystery_list
    'justice' in mystery_list
    'oppression' in mystery_list
    'equality' in mystery_list
    range(5,18,4)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    exercise02()
