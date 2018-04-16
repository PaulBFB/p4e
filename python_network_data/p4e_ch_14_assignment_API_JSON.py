import urllib.request
import urllib.parse
import json


serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'
# basic location of the API

#location = input('please enter the place to GeoCode: ')
location = 'University of Tuebingen'
# argument to be passed in

req = serviceurl + urllib.parse.urlencode({'address': location})
# creating the request (analogous a fhandle)
# --> urlencode adds the key/value pair from the dict as parameters to the URL

print('you are requesting the URL:', req)
# bug test encoded url
response = urllib.request.urlopen(req).read()
# 'opening' the url

result = response.decode()
jresult = json.loads(result)

print(jresult['results'][0]['place_id'])
