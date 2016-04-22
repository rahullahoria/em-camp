#sudo apt-get install python-pip
import mechanize #sudo pip install python-mechanize
import re
import urllib2
import time

####################################
def savePage( url ):
    headers = {'USER-Agent':'crawltaosof'}
    req = urllib2.Request(url, None,headers)
    try:
        pageObj = urllib2.urlopen(req,timeout=0.51)
        print pageObj.info().getheader('Content-Type')
        if "text/html" in pageObj.info().getheader('Content-Type'):
            page = pageObj.read()
            print page
            f = open("crowl/"+str(time.time())+"_"+url.split("/")[2]+".html","w") #opens file with name of "test.txt"
            f.write(page)
            f.close()
            return 1
    except Exception, err:
        print Exception, err
        return 0
    return 0


def uniqueListConc(first_list,second_list):
    in_first = set(first_list)
    in_second = set(second_list)
    in_second_but_not_in_first = in_second - in_first
    result = first_list + list(in_second_but_not_in_first)
    return result

###################################

br = mechanize.Browser() #initiating a browser

br.set_handle_robots(False) #ignore robots.txt

br.addheaders = [("User-agent","Mozilla/5.0")] #our identity in the web

q = raw_input("enter the keyword::") #keyword/keyphrase

qe=""

alert = ""
for i in range(0,len(q)):
    if q[i] ==" ":
        qe+="+"
    else:
        qe+=q[i]

counter = 0
allLinks = []

for i in range(0,1):
    google_url = br.open("https://www.google.co.in/search?q=" + qe + "&amp;amp;start=" + str(counter))
    search_keyword = google_url.read()
    o = re.findall("(?P<url>https?://[^\s\"<]+)", search_keyword)
    allLinks = uniqueListConc(allLinks,o)
    break
    #print len(o)
    print "."
    '''
    break
    if "rahullahoria" in search_keyword:
        alert = "found"
        break
    '''
    counter+=10

print len(allLinks)
for link in allLinks:
    page = savePage( link )
if alert == "found":
    print "Found at page:: ",i+1
else:
    print "not found"
