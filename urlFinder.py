#sudo apt-get install python-pip
import mechanize #sudo pip install python-mechanize
import re,os
import urllib2
import time
import MySQLdb
#db = MySQLdb.connect("localhost","root","redhat8892","compaining" )
#cursor = db.cursor()

####################################
def getUrls(page):
	return re.findall("(?P<url>https?://[^\s\"<]+)", page)
	


def savePage( url, level ):
	db = MySQLdb.connect("localhost","root","redhat8892","compaining" )
	cursor = db.cursor()
	cursor.execute('''SELECT * FROM urls WHERE url = (%s)''',(url) )
	numRows = cursor.rowcount
	if numRows > 0 :
		print "duplicate url"
		return
	#url presnt in db terminate
	print level
	if(level>=3):
		print "killing next level"
		return
	headers = {'USER-Agent':'crawltaosof'}
	req = urllib2.Request(url, None,headers)
	try:
		pageObj = urllib2.urlopen(req,timeout=0.51)
		print pageObj.info().getheader('Content-Type')
		if "text/html" in pageObj.info().getheader('Content-Type'):
			page = pageObj.read()
			fileName = os.path.dirname(os.path.realpath(__file__))+"/crowl/"+str(time.time())+"_"+url.split("/")[2]+".html"
			cursor.execute('''INSERT INTO urls(url, filename) VALUES (%s, %s)''', (url, fileName))
			db.commit()
			f = open(fileName,"w") #opens file with name of "test.txt"
			f.write(page)
			f.close()
			ts = getUrls(page)
			for t in ts:
				for i in range(0,5):
					savePage( t, level+i )
            #print page
			return 1
	except Exception, err:
		print Exception, err
		return 0
	return 0
	db.close()


def uniqueListConc(first_list,second_list):
    in_first = set(first_list)
    in_second = set(second_list)
    in_second_but_not_in_first = in_second - in_first
    result = first_list + list(in_second_but_not_in_first)
    return result

def getGSLinks():
	br = mechanize.Browser() #initiating a browser
	br.set_handle_robots(False) #ignore robots.txt
	br.addheaders = [("User-agent","Mozilla/5.0")] #our identity in the web
	qe=""

	alert = ""
	global q
	for i in range(0,len(q)):
		if q[i] ==" ":
			qe+="+"
		else:
			qe+=q[i]

	counter = 0
	global allLinks

	for i in range(0,3):
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

	#print len(allLinks)
	for link in allLinks:
		page = savePage( link,0 )


###################################
allLinks = []
q = raw_input("enter the keyword::") #keyword/keyphrase

getGSLinks()

