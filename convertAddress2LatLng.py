#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import json

def getLatLng(address):
    try:
        param   = {"address":address.encode('utf-8') if isinstance(address, unicode) else address}
        jsonStr = urllib.urlopen('http://maps.google.com/maps/api/geocode/json?%s&sensor=false' % urllib.urlencode(param)).read().decode('utf-8')
        result  = json.loads(jsonStr)
        latlng  = result['results'][0]['geometry']['location']
        return (latlng['lat'], latlng['lng'])
    except:
        return None

def main():
    address = u'東京都千代田区千代田１−１'
    latLng = getLatLng(address)
    if latLng:
        print str(latLng[0]) + '\t' + str(latLng[1])
    else:
        print ""

#     f = open('./address.txt')
#     lines = f.readlines()
#     for line in lines:
#         latLng = getLatLng(line)
#         if latLng:
#             print str(latLng[0]) + '\t' + str(latLng[1])
#         else:
#             print ""
#     f.close()

if __name__ == '__main__':
    main()

