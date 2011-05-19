# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$May 13, 2011 8:41:42 PM$"

def string_formats():
    """
      >>> string_formats()
      5 5 5.000000
      3.00
      7.00      0.50
       $ 3.00n $ 4.50n $11.20
      this that something
      yes no up down
      3 3.000000 3.000000
    """
    print "%s %d %f" % (5,5,5)
    print "%-.2f" % 3
    print "%-10.2f%-10.2f" % (7,1.0/2)
    print " $%5.2fn $%5.2fn $%5.2f" % (3,4.5,11.2)
    print "%s %s %s" % ('this','that','something')
    print "%s %s %s %s" % ('yes','no','up','down')
    print "%d %f %f" % (3,3,3)
def remove_all(sub, s):
    """
      >>> remove_all('an', 'banana')
      'ba'
      >>> remove_all('cyc', 'bicycle')
      'bile'
      >>> remove_all('iss', 'Mississippi')
      'Mippi'
      >>> remove_all('eggs', 'bicycle')
      'bicycle'
    """
    index = 0
    out = ''
    totalDel = []
    if(len(sub)>len(s)):
        return -1
    for elem in s:
        if index > (len(s) - len(sub)):            
            break
        subindex = 0
        found = True
        delList = []
        for subelem in sub:                        
            if subelem != s[index + subindex]:
                found = False
                break
            delList.append(index + subindex)
            subindex = subindex + 1        
        if found:
            totalDel+=delList            
        index = index + 1
    index2 = 0
    for elem in s:
        if index2 not in totalDel:
            out = out + elem
        index2 = index2 + 1
    if len(out)==0:
        print '\''+s+'\''
    else:
        print '\''+out+'\''

def remove(sub, s):
    """
      >>> remove('an', 'banana')
      'bana'
      >>> remove('cyc', 'bicycle')
      'bile'
      >>> remove('iss', 'Mississippi')
      'Missippi'
      >>> remove('egg', 'bicycle')
      'bicycle'
    """
    index = 0
    out = ''
    if(len(sub)>len(s)):
        return -1
    for elem in s:
        if index > len(s) - len(sub):
            break
        subindex = 0
        found = True
        delList = []
        for subelem in sub:
            delList.append(index + subindex)
            if subelem != s[index + subindex]:
                found = False
                break
            subindex = subindex + 1
        if found:            
            index2 = 0
            for elem in s:
                if index2 not in delList:
                    out = out + elem
                index2 = index2 + 1
            break
        index = index + 1
    if len(out)==0:
        print '\''+s+'\''
    else:
        print '\''+out+'\''

def count(sub, s):
    """
      >>> count('is', 'Mississippi')
      2
      >>> count('an', 'banana')
      2
      >>> count('ana', 'banana')
      2
      >>> count('nana', 'banana')
      1
      >>> count('nanan', 'banana')
      0
    """
    count = 0
    index = 0
    if(len(sub)>len(s)):
        return -1
    for elem in s:
        if index > len(s) - len(sub):
            break
        subindex = 0
        found = True
        for subelem in sub:
            if subelem != s[index + subindex]:
                found = False
                break
            subindex = subindex + 1
        if found:
            count = count + 1
        index = index + 1
    print count
def is_palindrome(s):
    """
      >>> is_palindrome('abba')
      True
      >>> is_palindrome('abab')
      False
      >>> is_palindrome('tenet')
      True
      >>> is_palindrome('banana')
      False
      >>> is_palindrome('straw warts')
      True
    """
    i = -1
    reverse =''
    while i >= -len(s):
        reverse = reverse +s[i]
        i=i-1
    if reverse == s:
        print True
    else:
        print False

def remove_letter(letter, strng):
    """
      >>> remove_letter('a', 'apple')
      'pple'
      >>> remove_letter('a', 'banana')
      'bnn'
      >>> remove_letter('z', 'banana')
      'banana'
      >>> remove_letter('i', 'Mississippi')
      'Msssspp'
    """
    out = ''
    for elem in strng:
        if elem != letter:
            out = out + elem
    print '\''+out+'\''
def mirror(s):
    """
      >>> mirror("good")
      'gooddoog'
      >>> mirror("yes")
      'yessey'
      >>> mirror('Python')
      'PythonnohtyP'
      >>> mirror("")
      ''
      >>> mirror("a")
      'aa'
    """
    i = -1
    out =''
    while i >= -len(s):
        out = out +s[i]
        i=i-1
    print '\''+s+out+'\''
def reverse(s):
    """
      >>> reverse('happy')
      'yppah'
      >>> reverse('Python')
      'nohtyP'
      >>> reverse("")
      ''
      >>> reverse("P")
      'P'
    """
    i = -1
    out =''
    while i >= -len(s):
        out = out +s[i]
        i=i-1
    print '\''+out+'\''
if __name__ == '__main__':
    import doctest
    doctest.testmod()
