# IPython log file
# -*-coding:utf-8 -*
import time
from getdata import *
datos=asciitable.read('Name_city.csv',delimiter=";")
names=list(datos.dtype.names)
datos=datos[names[:2]]
import matplotlib.mlab as mlab
import geopy
g=geocoders.Nominatim()
dt = np.dtype((str, 35))
dt2 = np.dtype((str, 100))
datos=mlab.rec_append_fields(datos,'lat',np.zeros(datos.size))
datos=mlab.rec_append_fields(datos,'lon',np.zeros(datos.size))
datos=mlab.rec_append_fields(datos,'latcity',np.zeros(datos.size))
datos=mlab.rec_append_fields(datos,'loncity',np.zeros(datos.size))
datos=mlab.rec_append_fields(datos,'nlat',np.zeros(datos.size))
datos=mlab.rec_append_fields(datos,'nlon',np.zeros(datos.size))
datos=mlab.rec_append_fields(datos,'MODEL',np.zeros(datos.size),dt)
datos=mlab.rec_append_fields(datos,'date',np.zeros(datos.size),dt)
datos=mlab.rec_append_fields(datos,'hour',np.zeros(datos.size),dt)
datos=mlab.rec_append_fields(datos,'alt',np.zeros(datos.size))
datos=mlab.rec_append_fields(datos,'sunazt',np.zeros(datos.size))
datos=mlab.rec_append_fields(datos,'sunelv',np.zeros(datos.size))
datos=mlab.rec_append_fields(datos,'shu',np.zeros(datos.size),dt)
datos=mlab.rec_append_fields(datos,'lens',np.zeros(datos.size),dt)
datos=mlab.rec_append_fields(datos,'ap',np.zeros(datos.size),dt)
datos=mlab.rec_append_fields(datos,'ISO',np.zeros(datos.size),dt)
datos=mlab.rec_append_fields(datos,'Coments',np.zeros(datos.size),dt2)
datos=mlab.rec_append_fields(datos,'NASA',np.zeros(datos.size))
datos=mlab.rec_append_fields(datos,'CoordFLAG',np.zeros(datos.size))
datos=mlab.rec_append_fields(datos,'URL',np.zeros(datos.size),dt2)
datos=mlab.rec_append_fields(datos,'small',np.zeros(datos.size),dt2)
datos=mlab.rec_append_fields(datos,'large',np.zeros(datos.size),dt2)
datos=mlab.rec_append_fields(datos,'Thumbnail',np.zeros(datos.size),dt2)
datos=mlab.rec_append_fields(datos,'coordimage',np.zeros(datos.size),dt2)
for x in range(datos.size):
#for x in arange(0,5):
    if (x+1)%50==0:
        time.sleep(100)


    #print datos[x]['City']
    ISSname=datos[x]['ISS-ID'].split('-E-')
    debug=1
    if debug==1:
        try :       
            datos[x].lat,datos[x].lon,datos[x].nlat,datos[x].nlon,datos[x].MODEL,datos[x].date,datos[x].hour,datos[x].alt,datos[x].sunazt,datos[x].sunelv,datos[x].shu,datos[x].lens,datos[x].ap,datos[x].ISO,city,country,datos[x].NASA,datos[x].URL,datos[x].small,datos[x].large,datos[x].Thumbnail,datos[x].coordimage=getdata(ISSname[0],ISSname[1])
        except IndexError:
            print 'IndexError:'
            print ISSname

        except ValueError:
            print 'ValueError:'    
            print ISSname 
        except urllib2.HTTPError:
            print 'urllib2.HTTPError:'
            print ISSname
        except:
            print "otras"
    else:
        #print str(ISSname)+' '+ datos[x]['City']
        #
        #print ""
        #print datos[x]['City']
        if 1: 
         try:
            datos[x].lat,datos[x].lon,datos[x].nlat,datos[x].nlon,datos[x].MODEL,datos[x].date,datos[x].hour,datos[x].alt,datos[x].sunazt,datos[x].sunelv,datos[x].shu,datos[x].lens,datos[x].ap,datos[x].ISO,city,country,datos[x].NASA,datos[x].URL,datos[x].small,datos[x].large,datos[x].Thumbnail,datos[x].coordimage=getdata(ISSname[0],ISSname[1])
         except:
            print getdata(ISSname[0],ISSname[1])
    try:
     datos[x].latcity,datos[x].loncity=getcity(datos[x]['City'])
     print str(ISSname)+' '+ datos[x]['City'] 
     datos[x].CoordFLAG=5
    except TypeError:
     #print 'No city'
     try:
       if city==-1:
        (new_place,new_point) = g.reverse((datos[x].nlat,datos[x].nlon),timeout=10)
        if new_place==None:
            new_place=""
        
        datos[x]['City']=new_place.split(',')[-1].encode('utf-8')
        print str(ISSname)+' '+datos[x]['City']+' Reverse1'
       else:       
        datos[x]['City']=city.split('%20')[0].split('-')[0]
        datos[x].latcity,datos[x].loncity=getcity(datos[x]['City'])
        print str(ISSname)+' '+ datos[x]['City']+' NASAname1'
        datos[x].CoordFLAG=1
     except geopy.exc.GeocoderTimedOut:
       print str(ISSname)+' '+ datos[x]['City']
       print 'Posible bloqueo'
     except TypeError:
       datos[x]['City']=datos[x]['City'].split('%20')[0].split('-')[0]
       try:
        datos[x].latcity,datos[x].loncity=getcity(datos[x]['City'])
        print str(ISSname)+' '+datos[x]['City']+' Reverse2'
        datos[x].CoordFLAG=1
       except TypeError:
        print str(ISSname)+' '+datos[x]['City']+' unknown1'
        datos[x].CoordFLAG=0
       except geopy.exc.GeocoderTimedOut:
        print str(ISSname)+' '+datos[x]['City']+' unknown2'
        datos[x].CoordFLAG=0
    except AttributeError:
        print str(ISSname)+' '+datos[x]['City']+' unknown4'
        datos[x].CoordFLAG=0
       
    except geopy.exc.GeocoderTimedOut:
     try:
       if city==-1:
        (new_place,new_point) = g.reverse((datos[x].nlat,datos[x].nlon),timeout=10)
        if new_place==None:
            new_place=""
        datos[x]['City']=new_place.split(',')[-1].encode('utf-8')
       else:       
        datos[x]['City']=city.split('%20')[0].split('-')[0]
        datos[x].latcity,datos[x].loncity=getcity(datos[x]['City'])
       print str(ISSname)+' '+ datos[x]['City']+' NASAname2'
       datos[x].CoordFLAG=1
     except geopy.exc.GeocoderTimedOut:
       print str(ISSname)+' '+ datos[x]['City']
       print 'Posible bloqueo'
       datos[x].CoordFLAG=0
     except TypeError:
       print str(ISSname)+' '+datos[x]['City']+'unknown3'
       datos[x].CoordFLAG=0
       
       
    if datos[x]['City']=="":
     if city==-1:
        try:
            (new_place,new_point) = g.reverse((datos[x].nlat,datos[x].nlon),timeout=10)
        except geopy.exc.GeocoderTimedOut:
            print str(ISSname)+' '+ datos[x]['City']
            print 'Posible bloqueo'
            datos[x].CoordFLAG=0
        if new_place==None:
            new_place=""
        datos[x]['City']=new_place.split(',')[-1].encode('utf-8')
        print str(ISSname)+' '+ datos[x]['City']+' Reverse 3'
        datos[x].CoordFLAG=1
     else:
            datos[x]['City']=str(city)+','+str(country)
            #print 'NASAname: '+str(city)+','+str(country)
            
        #datos[x].lat,datos[x].lon,datos[x].nlat,datos[x].nlon,datos[x].MODEL,datos[x].date,datos[x].hour,datos[x].alt,datos[x].sunazt,datos[x].sunelv,datos[x].shu,datos[x].ap,datos[x].ISO=getdata(ISSname[0],ISSname[1])
        
#datos.tofile('procesed.csv', sep="\n", format="%s")
asciitable.write(datos,'procesed_b.csv')
