# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Sep 29, 2011 8:58:52 PM$"

def encapsulate(val, seq):
    if type(seq) == type(""):
        return str(val)
    if type(seq) == type([]):
        return [val]
    return (val,)


def insert_in_middle(val, seq):
    """
      >>> insert_in_middle(2,['a','b','c','d'])
      ['a', 'b', 2, 'c', 'd']
      >>> insert_in_middle('a','karlo')
      'kaarlo'
      >>> insert_in_middle('ca',('ca','kaj','sto'))
      ('ca', 'ca', 'kaj', 'sto')
    """
    middle = len(seq)/2
    return seq[:middle] + encapsulate(val, seq) + seq[middle:]

def make_empty(seq):
    """
      >>> make_empty([1, 2, 3, 4])
      []
      >>> make_empty(('a', 'b', 'c'))
      ()
      >>> make_empty("No, not me!")
      ''
    """
    if type(seq) == type(""):
        return  ''
    if type(seq) == type([]):
        return []
    return ()
if __name__ == "__main__":
    import doctest
    doctest.testmod()
