#!/usr/bin/env python
import os
import sys
import urllib2
import webbrowser
from geopy import geocoders
city = sys.argv[1]

opener1 = urllib2.build_opener()
#city='Madrid'
def getcity(city):
    g=geocoders.Nominatim()
    (place, point) = g.geocode(city)
    latcity=point[0]
    loncity=point[1]
    return latcity,loncity
latcity,loncity=getcity(city)

print latcity
print loncity
