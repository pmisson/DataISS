# IPython log file

import urllib2
import webbrowser
opener1 = urllib2.build_opener()
maps = opener1.open('http://maps.google.com/maps?q='+city)
city='Madrid'
maps = opener1.open('http://maps.google.com/maps?q='+city)
maps
my_city = maps.read()
my_city
my_city.find('40.'
)
my_city[149699-10:149699+10]
my_city[149699-20:149699+10]
my_city[149699-20:149699+30]
my_city[149699-40:149699+30]
my_city.find('viewport_center_lat=')
latcity=my_city.find('viewport_center_lat=')
my_city[latcity:latcity+30]
my_city[latcity:latcity+30].split('=')
my_city[latcity:latcity+30].split('=')[1]
loncity=my_city.find('viewport_center_lon=')
my_city[loncity:loncity+30].split('=')[1]
my_city[loncity:loncity+30].split('=')
my_city[loncity:loncity+30]
loncity
my_city[latcity:latcity+10]
my_city[latcity:latcity+100]
loncity=my_city.find('viewport_center_lng=')
my_city[loncity:loncity+30].split('=')
get_ipython().magic(u'logstart')
exit()
