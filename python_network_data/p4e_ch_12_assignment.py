from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.html'

html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')

comments = []

for tag in tags:
    comments.append(int(tag.contents[0]))

print('count', len(comments))
print('sum', sum(comments))