#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from gui import *
from ConfigParser import SafeConfigParser

try:
    import requests
    import json
except ImportError as e:
    print ("Error: %s \n" % (e))
    print("Try this ... pip install -r /path/to/requirements.txt")
    sys.exit(1)

def getJSON( hexID ):
   ''' str -> js
   returns json from flightradar api
   >>> getJSON('4CA4CC')
   {u'aircraft': {u'item': {u'current': 1}, u'live': None, u'data': [{u'model': {u'text': u'Boeing 737-8JP', u'code': u'B738', u'id': 5022924}, u'hex': u'4CA4CC', u'airline': {u'code': {u'icao': u'NAX', u'iata': u'DY'}, u'name': u'Norwegian'}, u'registration': u'EI-FHJ'}], u'timestamp': 1511868299}, u'flight': None}

   '''
   headers = { "Referer":"https://www.flightradar24.com/data/aircraft", "Origin":"https://www.flightradar24.com", "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0" }
   url = "https://api.flightradar24.com/common/v1/search.json?fetchBy=reg&query=" + hexID
   r = requests.get( url, headers=headers, verify=False )
   j = json.loads(r.text)
   return j['result']['response']

def isBlockedFA( ICAO , userFA, apiKeyFA ):
    ''' str -> bol '''
    auth = ( userFA, apiKeyFA )
    response = requests.get(fxmlUrl + "FlightInfoStatus", params=payload, auth=(auth))
    l = json.loads (response.text)
    return l['FlightInfoStatusResult']['flights'][0]

def main():

    TITLE = 'FlightFinder\nAPIs'
    banner(GREEN, TITLE)
    print "This should be imported as library"

