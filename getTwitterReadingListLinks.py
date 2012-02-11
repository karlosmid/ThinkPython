import httplib
import time
import random
def getBlogPostPageSource(blogDomainName,forBlogPostGroup,forMonth,forYear,forBlogPostNo):
    conn =\
    httplib.HTTPConnection(blogDomainName)
    time.sleep(random.choice([3,5,7,4,2])) 
    if forBlogPostNo == 23:
        blogPostUrl =\
          "/"+forYear+"/"+forMonth+"/"+forBlogPostGroup+'22_22'+".html" 
    else: 
        blogPostUrl =\
         "/"+forYear+"/"+forMonth+"/"+forBlogPostGroup+str(forBlogPostNo)+".html" 
    conn.request("GET", blogPostUrl)
    blogResult = conn.getresponse()
    print blogPostUrl, blogResult.status, blogResult.reason
    blogPostPageSource = blogResult.read()
    conn.close()
    return blogPostPageSource
def parsePageForLinks(forBlogPost,forLinkUrlDomainName):        
    links = [] 
    current = 0
    while 1:
        current = forBlogPost.find("http://"+forLinkUrlDomainName+"/",current)
        if current == -1:
            break
        else:
            linkEnd = forBlogPost.find(' ',current)
            links.append(forBlogPost[current:linkEnd-1])
            current = linkEnd
    return links
if __name__ == "__main__":
    totalLinkList = []
    forLinkUrlDomainName = "t.co"
    blogDomainName = "zagorskisoftwaretester.blogspot.com"
    forBlogPostGroup = "my-twitter-reading-list-"
    forPostsNumberRange = range(11,31)
    forYear = '2011'
    forMonth = '08'
    for blogPostNo in forPostsNumberRange:
        result = parsePageForLinks(\
        getBlogPostPageSource(blogDomainName,forBlogPostGroup,forMonth,forYear,blogPostNo),forLinkUrlDomainName)
        totalLinkList = totalLinkList + result  
    file = open('diigoLinks'+forMonth+forYear+'.txt','w')
    file.write('\n'.join(totalLinkList))
    file.close()
