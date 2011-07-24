# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jul 19, 2011 8:22:43 PM$"

def myreplace(old, new, s):
    """
    Replace all occurences of old with new in the string s.

    >>> myreplace(',', ';', 'this, that, and, some, other, thing')
    'this; that; and; some; other; thing'
    >>> myreplace(' ', '**', 'Words will now be separated by stars.')
    'Words**will**now**be**separated**by**stars.'
    """
    return new.join(s.split(old))
def cleanword(word):
    """
    >>> cleanword('what?')
    'what'
    >>> cleanword('"now!"')
    'now'
    >>> cleanword('?+="word!,@$()"')
    'word'
    >>> cleanword('?+="wo6rd!,@$()"')
    'word'
    """
    return ''.join([char for char in word if char.isalpha()]).lower()
def has_dashdash(s):
    """
    >>> has_dashdash('distance--but')
    True
    >>> has_dashdash('several')
    False
    >>> has_dashdash('critters')
    False
    >>> has_dashdash('spoke--fancy')
    True
    >>> has_dashdash('yo-yo')
    False
    """
    if s.find('--') != -1:
        return True
    else:
        return False
def extract_words(s):
    """
    >>> extract_words('Now is the time!  "Now", is the time? Yes, now.')
    ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now']
    >>> extract_words('she tried to curtsey as she spoke--fancy')
    ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy']
    """    
    WordsWithOutDashDash = ' '.join(s.split('--'))
    cleanWordsLowered = map(cleanword, WordsWithOutDashDash.split())
    return cleanWordsLowered
def wordcount(word, wordlist):
    """
    >>> wordcount('now', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
    ['now', 2]
    >>> wordcount('is', ['now', 'is', 'time', 'is', 'now', 'is', 'the', 'is'])
    ['is', 4]
    >>> wordcount('time', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
    ['time', 1]
    >>> wordcount('frog', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
    ['frog', 0]
    """
    count = [elem for elem in wordlist if elem == word]
    return [word,len(count)]
def wordset(wordlist):
    """
    >>> wordset(['now', 'is', 'time', 'is', 'now', 'is', 'is'])
    ['is', 'now', 'time']
    >>> wordset(['I', 'a', 'a', 'is', 'a', 'is', 'I', 'am'])
    ['I', 'a', 'am', 'is']
    >>> wordset(['or', 'a', 'am', 'is', 'are', 'be', 'but', 'am'])
    ['a', 'am', 'are', 'be', 'but', 'is', 'or']
    """
    count = []
    wordlist.sort()
    for elem in wordlist:
        count.append(wordcount(elem,wordlist))
    step = 0
    rez = []
    for index,elem in enumerate(count):        
        if index == step:
            rez.append(elem[0])
            step = step + elem[1]
    return rez
def longestword(wordset):
    """
    >>> longestword(['a', 'apple', 'pear', 'grape'])
    5
    >>> longestword(['a', 'am', 'I', 'be'])
    2
    >>> longestword(['this', 'that', 'supercalifragilisticexpialidocious'])
    34
    """
    rez = map(len,wordset)
    rez.sort()
    return rezT [-1]
if __name__ == "__main__":
    import doctest
    doctest.testmod()
