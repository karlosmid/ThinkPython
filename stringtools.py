# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$May 13, 2011 8:41:42 PM$"

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
            index = 0
            for elem in s:
                if index not in delList:
                    out = out + elem
                index = index + 1
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
