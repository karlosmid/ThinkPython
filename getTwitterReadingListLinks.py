import httplib
import time
import random
import urlparse
def getUsingHttp(forDomainName,thisLink,debug = False):
    if debug: 
        httplib.HTTPConnection.debuglevel = 1 
    conn = httplib.HTTPConnection(forDomainName)
    conn.request("GET", thisLink)
    httpResponse = conn.getresponse()
    httpResponseStatus = httpResponse.status
    httpResponseReason = httpResponse.reason
    httpResponseLocation = '' 
    if httpResponseReason == '301':
        httpResponseLocation = httpResponse.getheader('Location')
    httpResponseBody = httpResponse.read()
    conn.close()
    return [httpResponseStatus, httpResponseReason,httpResponseLocation,httpResponseBody]
def prepareBlogPostLink(blogDomainName,forBlogPostGroup,forMonth,forYear,forBlogPostNo):
    if forBlogPostNo == 23:
        blogPostUrl =\
          "/"+forYear+"/"+forMonth+"/"+forBlogPostGroup+'22_22'+".html" 
    else: 
        blogPostUrl =\
         "/"+forYear+"/"+forMonth+"/"+forBlogPostGroup+str(forBlogPostNo)+".html" 
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
    LinkWithTitle = []
    for item in forLinksInList:
        parsedUrl = urlparse.urlparse(item)
        httpResponse = getUsingHttp(parsedUrl.netloc,parsedUrl.path)
        if httpResponse[HTTP_STATUS] == '301':
            parsedUrl = urlparse.urlparse(httpResponse[HTTP_LOCATION])
            httpResponse = getUsingHttp(parsedUrl.netloc,parsedUrl.path)
        titleStart = httpResponse[HTTP_BODY].find('<title>')
        titleEnd = httpResponse[HTTP_BODY].find('</title>')
        title = httpResponse[HTTP_BODY][titleStart+len('<title>'):titleEnd]
        print title
if __name__ == "__main__":
    HTTP_STATUS = 0
    HTTP_REASON = 1
    HTTP_LOCATION = 2
    HTTP_BODY = 3 
    totalLinkList = []
    blogDomainName = "zagorskisoftwaretester.blogspot.com"
    forBlogPostGroup = "my-twitter-reading-list-"
    forBlogPostTitle = "My twitter reading list #"
    forPostsNumberRange = range(11,12)
    forYear = '2011'
    forMonth = '08'
    endMark = "Posted by"
    for blogPostNo in forPostsNumberRange:
        link =\
        prepareBlogPostLink(blogDomainName,forBlogPostGroup,forMonth,forYear,blogPostNo)
        time.sleep(random.choice([3,5,1,4,2]))
        httpResponse = getUsingHttp(blogDomainName,link)
        print httpResponse[HTTP_STATUS],httpResponse[HTTP_REASON],link
        totalLinkList = totalLinkList +\
            parsePageForLinks(httpResponse[HTTP_BODY],forBlogPostTitle,endMark)
        getPageTitle(totalLinkList)
    file = open('diigoLinks'+forMonth+forYear+'.txt','w')
    file.write('\n'.join(totalLinkList))
    file.close()
