#!/usr/bin/python

from settings import IP, PORT, URL, NAME, HOST, USER, PASS
import json
import ais.stream
import socket
import datetime
import requests
import mysql.connector


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

while True:
  i = 1
 
  for msg in ais.stream.decode(sock.makefile('r'),keep_nmea=True):
    rxtime =  datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S") #YYYYMMDDHHMMSS
    parsed = json.loads(json.dumps(msg))
    
    rxais = {
            'msgtype': parsed['id'],
            'mmsi': parsed['mmsi'],
            'rxtime': rxtime
            }

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
    if 'callsign' in parsed:
      rxais['callsign'] = parsed['callsign']
    if 'name' in parsed:
      rxais['shipname'] = parsed['name']
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
      rxais['destination'] = parsed['destination']
    if 'persons' in parsed:
      rxais['persons_on_board'] = parsed['persons']

    print (rxais)     
    i += 1
    if i > 4:
     break

  exit()