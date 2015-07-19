class TurboSmtp(object):
    _URL = "https://api.turbo-smtp.com/api/mail/send"

    def __init__(self, user, password):
        self._user = user
        self._password = password

    def send(self, message):
        import urllib
        import urllib2

        turbo_data = {}
        turbo_data["authuser"] = self._user
        turbo_data["authpass"] = self._password
        turbo_data["from"] = message["From"]
        turbo_data["to"] = message["To"]
        turbo_data["cc"] = message["CC"]
        turbo_data["bcc"] = message["BCC"]
        turbo_data["subject"] = message["Subject"]
        turbo_data["mime_raw"] = message.as_string()

        encoded = urllib.urlencode(turbo_data)
        req = urllib2.Request(self._URL, encoded)
        response = urllib2.urlopen(req)
        print response.read()


if __name__ == "__main__":
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
                   'authpass': "***",
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
