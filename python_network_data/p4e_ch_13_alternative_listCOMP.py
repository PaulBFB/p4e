from urllib.request import urlopen
from xml.etree import cElementTree as ET

url = input('enter a URL: ')

if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

raw = urlopen(url).read()

tree = ET.fromstring(raw)

# ' comments = tree.findall('./comments/comment/count') ' <-- goes down the tree from top to create list

# solution with list comprehension:
# create a list
# loop through elements
#   pull text from element
#   make int from all elements
# sum & print

print(sum([int(tag.text) for tag in tree.findall('./comments/comment/count')]))
