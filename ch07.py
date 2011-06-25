# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$May 9, 2011 9:22:29 PM$"

def count_letters_imp(input,letter):    
    count = 0
    index = input.find(letter)
    while  index != -1:
        input = input[index+1:]
        count+=1
        if count == 5:
            break
        index = input.find(letter)
    return count
def count_letters(input,letter):        
    count = 0
    for l in input:
        if l == letter:
            count+=1
    return count
def seven_16_1():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    for letter in prefixes:
        if letter in ['O','Q']:
            print letter+'u'+suffix
        else:
            print letter + suffix
def seven_14_1_2():
    """
    >>> fruit='rambutan'
    >>> type(fruit)
    <type 'str'>
    >>> len(fruit)
    8
    >>> fruit[:3]
    'ram'
    >>> group = "John, Paul, George, and Ringo"
    >>> group[12:group.find('George')+len('George')]
    'George'
    >>> group[group.find('Paul'):group.find('Paul')+len('Paul')]
    'Paul'
    >>> group[:len('John')]
    'John'
    >>> group[group.find('Ringo'):]
    'Ringo'
    """
    fruit='rambutan'
    type(fruit)
    len(fruit)
    fruit[:3]
    group = "John, Paul, George, and Ringo"
    group[12:group.find('George')+len('George')]
    group[group.find('Paul'):group.find('Paul')+len('Paul')]
    group[:len('John')]
    group[group.find('Ringo'):]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    seven_14_1_2()
    seven_16_1()
    print count_letters('banana','a')
    print count_letters_imp('ovojezagorje','etor')
