## Suppose we have a text with many email addresses
# Open database connection
# prepare a cursor object using cursor() method
import re,os
import MySQLdb
import glob

#files = glob.glob("/var/www/html/shatkonLabs/em-camp/crowl/*.html")
#print os.path.dirname(os.path.realpath(__file__))
db = MySQLdb.connect("localhost","root","redhat8892","compaining" )
cursor = db.cursor()
cursor.execute('''SELECT filename FROM urls WHERE status = 0''' )
files = cursor.fetchall()
print files

def getEmails(fileName):
	try:
		with open(fileName, 'r') as myfile:
			str = myfile.read().replace('\n', '')
	except:
		print "not found"
		str = "purple <alice@google.com, blah monkey bob@abc blah dishw"
	#print str

	#str = 'purple \"<alice@google.com\", blah monkey bob@abc blah dishwasher'

	## Here re.findall() returns a list of all the found email strings
	#emails = re.findall(r'(?<!\d)(?:\+91|91|091|0|0091|00)?\W*(?P<mobile>[789]\d{9})(?!\d)', str) 
		## ['alice@google.com', 'bob@abc.com'] 
	return re.findall(r'[\w\.-]+@[\w\.-]+', str)

for fileName in files:
	fileName = str(fileName)
	fileName = fileName[2:-3]
	print fileName
	emails = getEmails(fileName)
	print emails  
	page_url = "http://fddgfghfhgh.com"
	local_url = fileName
	for email in emails:
		# do something with each found email string
		print email
		try:
			cursor.execute('''INSERT INTO emails(email, page_url, local_url) VALUES (%s, %s, %s)''',
					  (email, page_url, local_url))
		except:
			print "duplicate"
		db.commit()
		print "inserted successfully"
		
	cursor.execute('''UPDATE urls SET status = 1 WHERE filename = (%s)''',(fileName))	
	db.commit()
	
    
    
'''
#^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$

#!/usr/bin/python
# Select qSQL with id=4.
cursor.execute("SELECT qSQL FROM TBLTEST WHERE id = 4")
# Fetch a single row using fetchone() method.
results = cursor.fetchone()
qSQL = results[0]
cursor.execute(qSQL)

# Fetch all the rows in a list of lists.
qSQLresults = cursor.fetchall()
for row in qSQLresults:
    id = row[0]
    city = row[1]
#SQL query to INSERT a record into the table FACTRESTTBL.
# Commit your changes in the database
# disconnect from server
'''
db.close() 
