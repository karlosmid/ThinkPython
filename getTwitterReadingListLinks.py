import time
import random
import urlparse
def getUsingHttpProtocol(forDomainName,thisLink,debug = False):
    import httplib 
    if debug: 
        httplib.HTTPConnection.debuglevel = 1 
    conn = httplib.HTTPConnection(forDomainName)
    conn.request("GET", thisLink)
    httpResponse = conn.getresponse()
    httpResponseStatus = httpResponse.status
    httpResponseReason = httpResponse.reason
    httpResponseHeaderLocation = httpResponse.getheader('Location')
    httpResponseBody = httpResponse.read()
    conn.close()
    return [httpResponseStatus, httpResponseReason,httpResponseHeaderLocation,httpResponseBody]
def prepareBlogPostLink(forBlogPostGroup,forMonth,forYear,forBlogPostNo):
    if forBlogPostNo == 23:
          path = forBlogPostGroup+'22_22' 
    elif forBlogPostNo == 35:
        path = 'jamesmarcusbach-james-marcus-bach-heres'
    elif forBlogPostNo == 45:
        path = 'michaelbolton-michael-bolton-blogged-at'
    elif forBlogPostNo == 49:
        path = 'my-twitter-reding-list-49'
    elif forBlogPostNo == 66:
        path = 'vaidyatcr-vaidyanathan-b-visit-to'
    elif forBlogPostNo == 124:
        path = 'my-twitter-reading-list124'
    else: 
        path = forBlogPostGroup+str(forBlogPostNo) 
    blogPostUrl =\
         "/"+forYear+"/"+forMonth+"/"+path+".html" 
    return blogPostUrl
def parsePageForLinks(forBlogPost,forBlogPostTitle,endMark):        
    links = [] 
    current = 0
    end = forBlogPost.find(endMark,current)
    current = forBlogPost.find(forBlogPostTitle,current)
    current = forBlogPost.find(forBlogPostTitle,current+1)
    while 1:
        current = forBlogPost.find("href",current)
        if current == -1:
            break
        elif current >= end:
            break
        else:
            linkEnd = forBlogPost.find(' ',current)
            linkAcctual = forBlogPost[current+len("href=\""):linkEnd-1]
            if 'twitter.com' not in linkAcctual:
                links.append(linkAcctual)
            current = linkEnd
    return links
def getPageTitle(forLinksInList):
    noOfLinksToParse = len(forLinksInList) 
    print 'Number of links to parse: '+str(len(forLinksInList)) 
    LinkWithTitle = []
    for item in forLinksInList:
        parsedUrl = urlparse.urlparse(item)
        try:
            httpResponse = getUsingHttpProtocol(parsedUrl.netloc,parsedUrl.path,debug =\
                                        False)
        except Exception, error:
            print 'Unable to parse: '+ item +'because of error: ',error
        counter = 5
        while httpResponse[HTTP_STATUS] == 301 and counter>0:
            counter = counter - 1 
            if httpResponse[HTTP_LOCATION] not in ['.pdf','.png']:
                time.sleep(random.choice([1,2])) 
                parsedUrl = urlparse.urlparse(httpResponse[HTTP_LOCATION])
                try: 
                    httpResponse =\
                    getUsingHttpProtocol(parsedUrl.netloc,parsedUrl.path,debug = False)
                except Exception, error:
                    print 'Unable to parse: '+httpResponse[HTTP_LOCATION]+\
                    'because of: ',error
            else:
                title = httpResponse[HTTP_LOCATION]
                break
            if httpResponse[HTTP_STATUS] == 200: 
                titleStart = httpResponse[HTTP_BODY].find('<title>')
                titleEnd = httpResponse[HTTP_BODY].find('</title>')
                title =\
                httpResponse[HTTP_BODY][titleStart+len('<title>'):titleEnd]
            else:
                title =\
                str(httpResponse[HTTP_STATUS])+str(parsedUrl.netloc+parsedUrl.path)
        LinkWithTitle.append(item+'___'+title+'___')
        noOfLinksToParse = noOfLinksToParse - 1
        print 'No of links left to parse: '+str(noOfLinksToParse)
    return LinkWithTitle
if __name__ == "__main__":
    HTTP_STATUS = 0
    HTTP_REASON = 1
    HTTP_LOCATION = 2
    HTTP_BODY = 3 
    totalLinkList = []
    blogDomainName = "zagorskisoftwaretester.blogspot.com"
    forBlogPostGroup = "my-twitter-reading-list-"
    forBlogPostTitle = "My twitter reading list #"
    forPostsNumberRange = range(132,138)
    forYear = '2012'
    forMonth = '01'
    endMark = "Posted by"
    for blogPostNo in forPostsNumberRange:
        link =\
        prepareBlogPostLink(forBlogPostGroup,forMonth,forYear,blogPostNo)
        time.sleep(random.choice([3,5,1,4,2]))
        try: 
            httpResponse = getUsingHttpProtocol(blogDomainName,link)
        except Exception, error:
            print error, parsedUrl
        print httpResponse[HTTP_STATUS],httpResponse[HTTP_REASON],link
        totalLinkList = totalLinkList +\
            parsePageForLinks(httpResponse[HTTP_BODY],forBlogPostTitle,endMark)
    file = open('diigoLinks'+forMonth+forYear+'.txt','w')
    file.write('\n'.join(getPageTitle(totalLinkList)))
    file.close()
