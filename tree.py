def printTree( withHeight ):
    spaces = withHeight*' '
    print '%s' % (spaces+'I')
    for i in range(1,withHeight+1):
        spaces = (withHeight - i)*' '
        print '%s' % (spaces+(2*i+1)*'I')
    spaces = withHeight*' '
    print '%s' % spaces+'I'

if __name__ == '__main__':
    printTree(22)
