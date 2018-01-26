#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import socket
import argparse
from configparser import SafeConfigParser
from gui import *
from sock import *
from aircraft import *
from led import Led

#    while true:
#       led.ON()
#       raw_input()
#       led.OFF()
#       raw_input()


def clParser():
    ''' None -> parses parameters and returns an array with them '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--config', dest="configFile",
        default='flightdata.conf', type=str,
        help='Configuration file. Default: flightdata.conf')
    parser.add_argument('-i','--ip', dest="ip",
        default='127.0.0.1', type=str,
        help='IP of the dump1090')
    parser.add_argument('-p','--port', dest="port",
        default=30003, type=int,
        help='Port where dump1090')
    parser.add_argument('-l','--led', dest="led",
        default=17, type=int,
        help='Led GPIO number (not position)'
    parser.add_argument('-f','--file', dest="fich",
        default="important_planes", type=str,
        help='File containing planes ID to light the led ON, one hex id per line')
    args = parser.parse_args()
    return args

def main():
    aircrafts = {}
    # Beautifull goddamn banner
    TITLE = 'Flight\n  Finder'
    banner(GREEN, TITLE)

    # parse parameters
    arg = clParser()
    buff = Socket( arg.ip, arg.port )

    #init led stuff
    led = Led(arg.led)
    f = open(fich)
    for l in f:
        flights.append(l)

    known = []
    unknown = []
    
    while True:
        lineas = buff.readlines()
        for linea in lineas:
            for flight in flights:
                if flight in linea:
                    led.ON
            new = True
            try:
                planeID = linea.split(',')[4]
            except:
                continue
            try:
                if planeID in known:
                    logWHITE( "Plane %s is known" % (planeID))
                    continue
                elif planeID in unknown:
                    new = False
                    logBLUE( "Plane %s is already unknwown" %  (planeID))
            except:
                logRED( "New Plane " + planeID )

            if new:
                aircrafts[ planeID ] = Plane( planeID )
                logPINK ( "New plane created for %s" % planeID )
     
            try:
                if linea.split(',')[10] != '':
                    logYELLOW( 'Checking ' + planeID )
                    aircrafts[ planeID ].isKnown = aircrafts[ planeID ].identify(linea.split(',')[10])
                if aircrafts[ planeID ].isKnown:
                    if planeID in unknown: # it may be acknowloedged with the first line 
                        unknown.pop(unknown.index( planeID ))
                    known.append ( planeID )
                    logYELLOW( planeID + " acknowledged")
                if new:
                    unknown.append( planeID )
                if  planeID in unknown and len(linea) > 4 :
                    #this check >4 is to avoid empty lines which I show somewhen
                    #aircrafts[ planeID ].file.write(linea.decode('utf-8') + '\n')
                    #aircrafts[ planeID ].file.flush()
                    aircrafts[ planeID ].saveLine( linea )
            except ImportError as e:
                logERROR(' Error processing: ')
                logERROR( str(linea))
                logERROR( e )

if __name__ == "__main__":
    main()

