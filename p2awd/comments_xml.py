import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
  
serviceurl = 'http://py4e-data.dr-chuck.net/comments_326130.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = serviceurl 
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')

#decoding the XML
xml_content = data.decode()

stuff = ET.fromstring(xml_content)

cnt = stuff.findall('comments/comment')
print('User count:', len(cnt))

total = 0
for cnts in cnt:
    total = total + int(cnts.find('count').text)

    
print('Sum:', total)
