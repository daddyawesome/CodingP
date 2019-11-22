import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

cnt =int(input('Enter count: '))
pos =int(input('Enter position: '))

while cnt > 0:
    alist = list()
    #Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        x = tag.get('href',None)
        alist.append(x)
    print('Retrieve:', alist[pos-1])
    cnt = cnt - 1
    url = alist[pos-1]
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
