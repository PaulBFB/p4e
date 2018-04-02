from urllib.request import urlopen
from xml.etree import cElementTree as ET


practice = 'http://py4e-data.dr-chuck.net/comments_42.xml'
test = 'http://py4e-data.dr-chuck.net/comments_84449.xml'

choice = input('practice or test? (p/t) - ')

if choice == 'p':
    raw = urlopen(practice).read()
elif choice == 't':
    raw = urlopen(test).read()
else:
    quit()

#print('file hast been opened:', choice)
#print(raw)

xml = ET.fromstring(raw)
counts = xml.findall('.//count')
print('amount of tags:', len(counts))
intcounts = []

for tag in counts:
    intcounts.append(int(tag.text))

print('sum of comments:', sum(intcounts))
