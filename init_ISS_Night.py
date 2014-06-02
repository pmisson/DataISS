# IPython log file
# -*-coding:utf-8 -*
from getdata import *
datos=asciitable.read('TablaISS.csv')
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
datos=mlab.rec_append_fields(datos,'ap',np.zeros(datos.size),dt)
datos=mlab.rec_append_fields(datos,'ISO',np.zeros(datos.size),dt)
datos=mlab.rec_append_fields(datos,'Coments',np.zeros(datos.size),dt2)
datos=mlab.rec_append_fields(datos,'NASA',np.zeros(datos.size))
datos=mlab.rec_append_fields(datos,'CoordFLAG',np.zeros(datos.size))
datos=mlab.rec_append_fields(datos,'URL',np.zeros(datos.size),dt2)
for x in range(datos.size):
#for x in arange(320,1432):
    #print datos[x]['City/Region']
    ISSname=datos[x]['ISS-ID'].split('-E-')
    debug=0
    if debug==1:
        try :       
            datos[x].lat,datos[x].lon,datos[x].nlat,datos[x].nlon,datos[x].MODEL,datos[x].date,datos[x].hour,datos[x].alt,datos[x].sunazt,datos[x].sunelv,datos[x].shu,datos[x].ap,datos[x].ISO,city,country,datos[x].NASA,datos[x].URL=getdata(ISSname[0],ISSname[1])
        except IndexError:
            print 'IndexError:'
            print ISSname

        except ValueError:
            print 'ValueError:'    
            print ISSname 
        except urllib2.HTTPError:
            print 'urllib2.HTTPError:'
            print ISSname
    else:
        #print str(ISSname)+' '+ datos[x]['City/Region']
        #
        #print ""
        #print datos[x]['City/Region']
        if 1: 
         try:
            datos[x].lat,datos[x].lon,datos[x].nlat,datos[x].nlon,datos[x].MODEL,datos[x].date,datos[x].hour,datos[x].alt,datos[x].sunazt,datos[x].sunelv,datos[x].shu,datos[x].ap,datos[x].ISO,city,country,datos[x].NASA,datos[x].URL=getdata(ISSname[0],ISSname[1])
         except:
            print getdata(ISSname[0],ISSname[1])
    try:
     datos[x].latcity,datos[x].loncity=getcity(datos[x]['City/Region'])
     print str(ISSname)+' '+ datos[x]['City/Region'] 
    except TypeError:
     #print 'No city'
     try:
       if city==-1:
        (new_place,new_point) = g.reverse((datos[x].nlat,datos[x].nlon))
        if new_place==None:
            new_place=""
        
        datos[x]['City/Region']=new_place.split(',')[-1].encode('utf-8')
        print str(ISSname)+' '+datos[x]['City/Region']+' Reverse1'
       else:       
        datos[x]['City/Region']=city.split('%20')[0].split('-')[0]
        datos[x].latcity,datos[x].loncity=getcity(datos[x]['City/Region'])
        print str(ISSname)+' '+ datos[x]['City/Region']+' NASAname1'
     except geopy.exc.GeocoderTimedOut:
       print str(ISSname)+' '+ datos[x]['City/Region']
       print 'Posible bloqueo'
     except TypeError:
       datos[x]['City/Region']=datos[x]['City/Region'].split('%20')[0].split('-')[0]
       try:
        datos[x].latcity,datos[x].loncity=getcity(datos[x]['City/Region'])
        print str(ISSname)+' '+datos[x]['City/Region']+' Reverse2'
       except TypeError:
        print str(ISSname)+' '+datos[x]['City/Region']+' unknown1'
       except geopy.exc.GeocoderTimedOut:
        print str(ISSname)+' '+datos[x]['City/Region']+' unknown2'
    except AttributeError:
        print str(ISSname)+' '+datos[x]['City/Region']+' unknown4'
       
    except geopy.exc.GeocoderTimedOut:
     try:
       if city==-1:
        (new_place,new_point) = g.reverse((datos[x].nlat,datos[x].nlon))
        if new_place==None:
            new_place=""
        datos[x]['City/Region']=new_place.split(',')[-1].encode('utf-8')
       else:       
        datos[x]['City/Region']=city.split('%20')[0].split('-')[0]
        datos[x].latcity,datos[x].loncity=getcity(datos[x]['City/Region'])
       print str(ISSname)+' '+ datos[x]['City/Region']+' NASAname2'
     except geopy.exc.GeocoderTimedOut:
       print str(ISSname)+' '+ datos[x]['City/Region']
       print 'Posible bloqueo'
     except TypeError:
       print str(ISSname)+' '+datos[x]['City/Region']+'unknown3'
       
       
    if datos[x]['City/Region']=="":
     if city==-1:
        try:
            (new_place,new_point) = g.reverse((datos[x].nlat,datos[x].nlon))
        except geopy.exc.GeocoderTimedOut:
            print str(ISSname)+' '+ datos[x]['City/Region']
            print 'Posible bloqueo'
        if new_place==None:
            new_place=""
        datos[x]['City/Region']=new_place.split(',')[-1].encode('utf-8')
        print str(ISSname)+' '+ datos[x]['City/Region']+' Reverse 3'
     else:
            datos[x]['City/Region']=str(city)+','+str(country)
            #print 'NASAname: '+str(city)+','+str(country)
            
        #datos[x].lat,datos[x].lon,datos[x].nlat,datos[x].nlon,datos[x].MODEL,datos[x].date,datos[x].hour,datos[x].alt,datos[x].sunazt,datos[x].sunelv,datos[x].shu,datos[x].ap,datos[x].ISO=getdata(ISSname[0],ISSname[1])
        
datos.tofile('procesed.csv', sep="\n", format="%s")
