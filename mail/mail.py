from email import message
from email.mime.text import MIMEText

#m = message.Message()
m = MIMEText("Some text")
m['From'] = "babymonitor@venus.raspberry"
m['Subject'] = "Baby Monitor"
m["To"] = "damian.nowok@gmail.com"

#print m.as_string()
print m["bcc"]

import sys
sys.exit()

import urllib
import urllib2

dataToSend = {
               'authuser': "damian.nowok@gmail.com",
               'authpass': "fI8x4buk",
               'from': "",
               'to': "",
               'cc': "",
               'bcc': "",
               'subject': "",
               'content': "",
               'html_content': "",
               'custom_headers': "",
               'mime_raw': m.as_string()
             }

try:
    encodedDataToSend = urllib.urlencode(dataToSend)
    req = urllib2.Request("https://api.turbo-smtp.com/api/mail/send", encodedDataToSend)
    response = urllib2.urlopen(req)
    print response.read()
except urllib2.HTTPError as error:
    print error
