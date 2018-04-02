import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


url = input('please enter a valid url - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# print(soup('a'))

tags = soup('a')

for tag in tags:
    print(tag)
    print(tag.get('href', None))
