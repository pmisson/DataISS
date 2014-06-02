#!/usr/bin/env python
import urllib2
import webbrowser
import os
import os, sys
from geopy import geocoders
try:
    import Image
except ImportError:
    from PIL import Image
    
from matplotlib.mlab import normpdf
#import matplotlib.numerix as nx
import pylab as p
import csv

import numpy as np
import matplotlib.cm as cm
import  matplotlib.pyplot as plt
import asciitable

from numpy import *
def getdata(ms,y):
    opener1 = urllib2.build_opener()
    #y=237318
    madre='http://eol.jsc.nasa.gov/scripts/sseop/photo.pl?mission='+ms+'&roll=E&frame='+str(y)
    small='http://eol.jsc.nasa.gov/sseop/images/ESC/small/'+ms+'/'+ms+'-E-'+str(y)+'.jpg'
    large='http://eol.jsc.nasa.gov/sseop/images/ESC/large/'+ms+'/'+ms+'-E-'+str(y)+'.jpg'
    thumbnail='http://eol.jsc.nasa.gov/sseop/images/thumb/'+ms+'/'+ms+'-E-'+str(y)+'.jpg'
    nombrefinal=madre#+prueba
    page2 = opener1.open(nombrefinal)
    my_picture = page2.read()
    coords=my_picture.find('MapCoordinate.pl')
    lat=my_picture[coords:coords+28].split('=')[1].split('&')[0]

    lon=my_picture[coords+28:coords+34].split('>')[0].split('=')[1]
    name=my_picture.find("Camera as Recorded in the Camera File:")
    if name ==-1:
        name=my_picture.find("Camera</a>:")
        cameramodel=my_picture[name+16:name+57].split('</b>')[0]
    else:
        cameramodel=my_picture[name+42:name+64].split('</b>')[0]
        
    focal=my_picture.find("Camera Focal Length:")
    if focal == -1:
        focal=my_picture.find("Focal")
        if focal ==-1:
            print 'no focal'
        else:    
            focal=my_picture[focal:focal+64].split()[2]
            
    else:
        focal=my_picture[focal:focal+64].split('<b>')[1].split('</b>')[0]
            
    date=my_picture.find("GMT Date")
    date=my_picture[date:date+64].split('<b>')[1].split('</b>')[0]
    hour=my_picture.find("GMT Time")
    hour=my_picture[hour:hour+64].split('<b>')[1].split('</b>')[0]
    nlat=my_picture.find("Nadir Latitude")
    nlon=my_picture.find("Nadir Longitude") 
    if nlat ==-1:
        nlat=my_picture.find("Nadir Point Latitude")
        nlon=nlat+35
        
    nlat=my_picture[nlat:nlat+64].split('<b>')[1].split('</b>')[0]
    nlon=my_picture[nlon:nlon+64].split('<b>')[1].split('</b>')[0]
    alt=my_picture.find("Spacecraft Altitude")
    alt=my_picture[alt:alt+64].split('<b>')[1].split('</b>')[0]
    sunazt=my_picture.find("Sun Azimut")
    sunazt=my_picture[sunazt:sunazt+64].split('<b>')[1].split('</b>')[0]
    sunelv=my_picture.find("Sun Elevation Angle")
    sunelv=my_picture[sunelv:sunelv+64].split('<b>')[1].split('</b>')[0]
    
    country=my_picture.find('Country')
    city=my_picture.find('Features')
    if country==-1:
     NASA=0
    else: 
     country=my_picture[country:country+100].split('<b>')[1].split('</b>')[0]
     city=my_picture[city:city+100].split('textfield=')[1].split('&')[0]
     NASA=1

    exif="http://eol.jsc.nasa.gov/sseop/camera/"+ms+"/"+ms+"-E-"+str(y)+".txt"
    
    try:
        page2 = opener1.open(exif)
        my_picture = page2.read()
        shu=my_picture.find("Shutter:")
        try: 
            shu=my_picture[shu:shu+64].split('\t\t\t')[1].split('\r')[0]
        except IndexError:
         try:
            shu=my_picture[shu:shu+64].split('\r')[0].split()[1]
         except IndexError:
          try:
            shu=my_picture.find("ExposureTime")
            shu=my_picture[shu:shu+64].split('\r')[0].split()[2]
          except IndexError:
           try:
            shu=my_picture.find("Exposure Time")
            shu=my_picture[shu:shu+64].split('\r')[0].split(':')[1]
           except IndexError:    
            shu=np.nan
            print 'no EXP'
            
        ap=my_picture.find("Aperture:")
        try: 
            ap=my_picture[ap:ap+64].split('\t\t\t')[1].split('\r')[0]
        except IndexError:
         try:
            ap=my_picture[ap:ap+64].split('\r')[0].split()[1]
         except IndexError:
          try:
           ap=my_picture.find("FNumber") 
           ap=my_picture[ap:ap+64].split('\r')[0].split()[2]
          except IndexError:
           try:
            ap=my_picture.find("F Number") 
            ap=my_picture[ap:ap+64].split('\r')[0].split(':')[1]
           except IndexError:
            ap=np.nan
            print 'no AP'            
            
        ISO=my_picture.find("ISO Speed:")
        try:
            ISO=my_picture[ISO:ISO+64].split('\t\t\t')[1].split('\r')[0]
        except IndexError:
         try:
            ISO=my_picture[ISO:ISO+64].split('\r')[0].split()[2]
         except IndexError:
           try:
            ISO=my_picture.find("ISO")
            ISO=my_picture[ISO:ISO+64].split('\r')[0].split(':')[1]
           except IndexError:
            ISO=np.nan
            print 'no ISO'
            
        MODEL=my_picture.find("MODEL:")
        try:
            MODEL=my_picture[MODEL:MODEL+64].split('\t\t\t\t')[1].split('\r')[0]
        except IndexError:
         try:
            MODEL=my_picture[MODEL:MODEL+64].split('\r')[0].split('\t')[1]
         except IndexError:
          try:
           MODEL=my_picture.find("Model")
           MODEL=my_picture[MODEL:MODEL+64].split('\r')[0].split(':')[1]
          except IndexError:
            MODEL=""
            print 'no MODEL'            
            
    except urllib2.HTTPError:
        print 'No exif'
        MODEL=""
        ISO=np.nan
        ap=""
        shu=""
    if MODEL=="":
        MODEL=cameramodel
    if alt=="":
        alt=np.nan    
    if sunelv=="":
        sunelv=np.nan
    if sunazt=="":
        sunazt=np.nan
    if lat=="":
        lat=np.nan
    if lon=="":
        lon=np.nan
    if nlat=="":
        nlat=np.nan
    if nlon=="":
        nlon=np.nan   

    return lat,lon,nlat,nlon,MODEL,date,hour,alt,sunazt,sunelv,shu,ap,ISO,city,country,NASA,madre,small,large,thumbnail


    
def getcity(city):
    g=geocoders.Nominatim()
    (place, point) = g.geocode(city)
    latcity=point[0]
    loncity=point[1]
    return latcity,loncity

#fot1=mlab.rec_append_fields(fot1,'FLUXERR_TEOup',np.zeros(fot1.size))

def getcityGMaps(city):
    opener1 = urllib2.build_opener()
    maps = opener1.open('http://maps.google.com/maps?q='+city)
    maps
    my_city = maps.read()
    latcity=my_city.find('viewport_center_lat=')
    latcity=my_city[latcity:latcity+30].split('=')[1].split(';')[0]
    loncity=my_city.find('viewport_center_lng=')
    loncity=my_city[loncity:loncity+30].split('=')[1].split(';')[0]
    return latcity,loncity
    
def getcityBing(city):
    opener1 = urllib2.build_opener()
    maps = opener1.open('https://www.bing.com/maps/?where1='+city)
    maps
    my_city = maps.read()
    latcity=my_city.find('.Maps.Location(')
    latcity=my_city[latcity:latcity+30].split('(')[1].split(',')[0]
    loncity=my_city.find('.Maps.Location(')
    loncity=my_city[loncity:loncity+100].split('(')[1].split(')')[0].split(',')[1]
    return latcity,loncity
