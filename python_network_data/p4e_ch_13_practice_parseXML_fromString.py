import xml.etree.cElementTree as ET

stuff = '''<stuff>
<users>
    <user x="2">
        <id>001</id>
        <name>Chuck</name>
    </user>
    <user x="7">
        <id>002</id>
        <name>Brent</name>
    </user>
</users>
</stuff>'''

xml = ET.fromstring(stuff)
users = xml.findall('users/user')

print('count:', len(users))

for tag in users:
    print('Name:', tag.find('name').text)
    print('id:', tag.find('id').text)
    print('ATTR:', tag.get('x'))

