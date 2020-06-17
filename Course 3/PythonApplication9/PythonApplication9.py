import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'
address = input('Enter location: ')
url = serviceurl + '?' + urllib.parse.urlencode({'sensor':'false', 'http://py4e-data.dr-chuck.net/json?':  address})
data = urllib.request.urlopen(url).read().decode()
info = json.loads(data)
print ('Retrieving', url, '\nRetrieved', len(data), 'caracters')
for item in info:
    key = item['place_id']
print ('Place id:', key)