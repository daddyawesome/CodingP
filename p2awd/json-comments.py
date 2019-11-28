import urllib.request, urllib.parse, urllib.error
import json
import ssl

serviceurl = 'http://py4e-data.dr-chuck.net/comments_326131.json'
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = serviceurl 
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
    
js = json.loads(data)

info = js['comments']
print('User count:', len(info))

total = 0
for item in info:
    total = total + int(item['count'])
    #print('Counts', item['count'])
    
print(total)
