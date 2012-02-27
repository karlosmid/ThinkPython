import getopt, sys

def usage():
    print 'usage: selectFromLinkDiigoTag.py -i fileWithLinks'
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:")
    except getopt.GetoptError, err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        sys.exit(2)
    inputFileName = None
    for o, a in opts:
        if o == "-i":
            inputFileName = a 
        else:
            assert False, "unhandled option"
    try: 
        fileWithLinks = open(inputFileName,'r')
    except Exception, e:
        print str(e)
        usage()
        sys.exit(2)
    listWithDiigoTags = parseFileWithLinks(fileWithLinks)
    fileWithLinks.close()
    file = open('diigoLinksWithTags.txt','w')
    file.write('\n'.join(listWithDiigoTags))
    file.close()
def parseFileWithLinks(fileWithLinks):
    LINK_NAME = 1
    LINK = 0
    diigoList = []
    for item in fileWithLinks:
        itemAsList = item.split('"')
        printDiigoTags() 
        choice = raw_input('Choose diigo tag for link '+itemAsList[LINK]+\
                           ' with description '+itemAsList[LINK_NAME]+':')
        diigoTag = parse(choice)
        itemAsList.append(diigoTag)
        diigoList.append(' '.join(itemAsList))
    return diigoList
def printDiigoTags():
    print '1:testing 2:programming 3:tools 4:business 5:science 6:brain'
def parse(choice):
    if choice == 1:
        return 'testing'
    elif choice == 2:
        return 'programming'
    elif choice == 3:
        return 'tools'
    elif choice == 4:
        return 'business'
    elif choice == 5:
        return 'science'
    elif choice == 6:
        return 'brain'
    else:
        return 'none'
if __name__ == "__main__":
    main()
