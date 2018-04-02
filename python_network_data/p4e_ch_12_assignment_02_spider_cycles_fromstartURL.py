from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('enter a starting url - ')

if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'

cycles = input('enter number of cycles - ')

try:
    cycles = int(cycles)
except:
    cycles = 4

position = input('enter position - ')

try:
    position = int(position) - 1
except:
    position = 2

i = 0

while i < cycles:
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position].get('href', None)
    print(tags[position].contents[0])
    i = i + 1
