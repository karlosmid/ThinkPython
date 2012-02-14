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
            linkAcctual = forBlogPost[current:linkEnd-1]
            if 'twitter.com' not in linkAcctual:
                links.append(linkAcctual)
            current = linkEnd
    return links
if __name__ == "__main__":
    totalLinkList = []
    forLinkUrlDomainName = "t.co"
    blogDomainName = "zagorskisoftwaretester.blogspot.com"
    forBlogPostGroup = "my-twitter-reading-list-"
    forBlogPostTitle = "My twitter reading list #"
    forPostsNumberRange = range(11,12)
    forYear = '2011'
    forMonth = '08'
    endMark = "Posted by"
    for blogPostNo in forPostsNumberRange:
        result = parsePageForLinks(\
        getBlogPostPageSource(blogDomainName,forBlogPostGroup,forMonth,forYear,blogPostNo),forBlogPostTitle,endMark)
        totalLinkList = totalLinkList + result  
    file = open('diigoLinks'+forMonth+forYear+'.txt','w')
    file.write('\n'.join(totalLinkList))
    file.close()
