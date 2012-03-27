import getopt, sys, time, json

def usage():
    print 'usage: selectFromLinkDiigoTag.py -i fileWithLinks -r numberOfDiigoLinks -s diigoFileWithTags'
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:r:s:")
    except getopt.GetoptError, err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        sys.exit(2)
    print opts,args 
    for o, a in opts:
        if o == "-i":
            inputFileName = a
            try: 
                fileWithLinks = open(inputFileName,'r')
            except Exception, e:
                print str(e)
                usage()
                sys.exit(2)
            listWithDiigoTags = parseFileWithLinks(fileWithLinks)
            fileWithLinks.close()
            file = open(inputFileName[:-4]+'WithTags.txt','w')
            file.write('\n'.join(listWithDiigoTags))
            file.close()
        elif o == "-r":
            getDiigoLinks(a)
            sys.exit(2)
        elif o == "-s":
            fileWithData = open(a,'r')
            sendToDiigo(fileWithData)
            fileWithData.close()
            sys.exit(2)
        else:
            assert False, "unhandled option"
def sendToDiigo(diigoFileWithLinksAndTags):
    import urllib
    import urllib2
    url = 'https://secure.diigo.com/api/v2/bookmarks'
    diigoApiKey = 'eb850240326fddfd'
    username = 'karlosmid'
    values = {'key':diigoApiKey,
              'url':'',
              'title':'',
              'tags':'',
              'shared':'yes'}
    linkCounter = 0
    for link in diigoFileWithLinksAndTags:
        linkAsList = link.split('___')
        values['url'] = linkAsList[0]
        values['title'] = linkAsList[1]
        values['tags'] = linkAsList[2]
        data = urllib.urlencode(values)
        request = urllib2.Request(url,data)
        authorisedRequest = authoriseRequest(request,username)
        response = urllib2.urlopen(authorisedRequest)
        responseAsJSON = json.load(response)
        if responseAsJSON['code'] != 1:
            print responseAsJSON, values
        else:
            linkCounter = linkCounter + 1
            print linkCounter
        time.sleep(2)
def getDiigoLinks(numberOfDiigoLinks):
    import urllib2
    diigoApiKey = 'eb850240326fddfd'
    username = 'karlosmid'
    request =\
    urllib2.Request('https://secure.diigo.com/api/v2/bookmarks?key='+diigoApiKey+'&user='+username+'&count='+numberOfDiigoLinks)
    authorisedRequest = authoriseRequest(request,username) 
    try: 
        stream = urllib2.urlopen(authorisedRequest)
        print stream.read()
    except urllib2.URLError,e:
        print e
def authoriseRequest(request,username):
    import base64
    fileWithPassword = open('diigo.txt','r')
    password = fileWithPassword.readline()
    fileWithPassword.close()
    base64string = base64.encodestring('%s:%s' % (username, password[:-1]))[:-1]
    request.add_header("Authorization", "Basic %s" % base64string)
    return request
def parseFileWithLinks(fileWithLinks):
    LINK_NAME = 1
    LINK = 0
    diigoList = []
    for item in fileWithLinks:
        itemAsList = item[:-4].split('___')
        printDiigoTags() 
        choice = raw_input('Choose diigo tag for link '+itemAsList[LINK]+\
                           ' with description '+itemAsList[LINK_NAME]+':')
        diigoTag = parse(choice)
        itemAsList.append(diigoTag)
        diigoList.append('___'.join(itemAsList))
    return diigoList
def printDiigoTags():
    print '1:testing 2:programming 3:tools 4:business 5:science 6:brain'
def parse(choice):
    if choice == '1':
        return 'testing'
    elif choice == '2':
        return 'programming'
    elif choice == '3':
        return 'tools'
    elif choice == '4':
        return 'business'
    elif choice == '5':
        return 'science'
    elif choice == '6':
        return 'brain'
    else:
        return 'none'
if __name__ == "__main__":
    main()
