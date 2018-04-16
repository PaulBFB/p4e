import json
import urllib.request

url = 'http://py4e-data.dr-chuck.net/comments_84450.json'
handle = urllib.request.urlopen(url)

js = json.loads(handle.read())

counts = []

[counts.append(int(i['count'])) for i in js['comments']]

print(sum(counts))
