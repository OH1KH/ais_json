#!/usr/bin/python

from settings import URL, NAME
import json
import ais.stream
import socket
import datetime
import requests

IP = '127.0.0.1'
PORT = 6710

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))


while True:
 i = 1
 u = int(datetime.datetime.utcnow().timestamp())
 mmsilist = []

 for msg in ais.stream.decode(sock.makefile('r'),keep_nmea=True):
   parsed = json.loads(json.dumps(msg))
   rxtime =  datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S") #YYYYMMDDHHMMSS

   rxais = {
            'mmsi': parsed['mmsi'],
            'rxtime': rxtime,
            'msgtype': parsed['id']
         }

   if 'name' in parsed:
    	    rxais['shipname'] = parsed['name'].replace("@"," ")
   if 'callsign' in parsed:
    	    rxais['callsign'] = parsed['callsign'].replace("@"," ")
   if 'x' in parsed:
    	    rxais['lon'] = parsed['x']
   if 'y' in parsed:
    	    rxais['lat'] = parsed['y']
   if 'sog' in parsed:
    	    rxais['speed'] = parsed['sog']
   if 'cog' in parsed:
    	    rxais['course'] = parsed['cog']
   if 'true_heading' in parsed:
    	    rxais['heading'] = parsed['true_heading']
   if 'nav_status' in parsed:
    	    rxais['status'] = parsed['nav_status']
   if 'type_and_cargo' in parsed:
    	    rxais['shiptype'] = parsed['type_and_cargo']
   if 'part_num' in parsed:
    	    rxais['partno'] = parsed['part_num']
   if 'vendor_id' in parsed:
    	    rxais['vendorid'] = parsed['vendor_id']
   if 'dim_a' in parsed:
    	    rxais['ref_front'] = parsed['dim_a']
   if 'dim_c' in parsed:
    	    rxais['ref_left'] = parsed['dim_c']
   if 'draught' in parsed:
    	    rxais['draught'] = parsed['draught']
   if 'length' in parsed:
    	     rxais['length'] = parsed['length']
   if 'width' in parsed:
    	    rxais['width'] = parsed['width']
   if 'destination' in parsed:
    	    rxais['destination'] = parsed['destination'].replace("@"," ")
   if 'persons' in parsed:
    	    rxais['persons_on_board'] = parsed['persons']

   
   path = { 
            "name": NAME, 
            "url": URL }


   grp = { 
            "path": [path], 
            "msgs":[rxais]
         }

   if i == 1:
    aisgroup = {
		  "groups":[grp]
		}
    mmsilist.append(rxais['mmsi'])
   else:
     if (rxais['mmsi'] in mmsilist):
      print('dupe',rxais['mmsi'])
     else:
      aisgroup["groups"] += [grp]
      mmsilist.append(rxais['mmsi'])
     
   i += 1
   if ( int(datetime.datetime.utcnow().timestamp()) - u) > 30:
	    break

 rxtime =  datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S") #YYYYMMDDHHMMSS

 output = {
            "protocol": 'jsonais',
            "encodetime": rxtime,
	    "groups": aisgroup["groups"]
          }
    

 post = json.dumps(output)
 print('\n')
#

 try:
 	r = requests.post(URL, files={'jsonais': (None, post)})
      #dump non common packets for debugging
#      if parsed['id'] not in (1,2,3,4):
#        print ('----')
#        print ('NMEA:', parsed['nmea'])
#        print ('Parsed:', parsed)
#        print ('Post:', post)
#        print ('Result:', json.loads(r.text)['description'])
 except requests.exceptions.RequestException as e:
 	 print (e)
