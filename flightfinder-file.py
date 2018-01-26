#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
from configparser import SafeConfigParser
from gui import *
from sock import *
from aircraft import *

def main():
    aircrafts = {}
    # Beautifull goddamn banner
    TITLE = 'Flight'
    banner(GREEN, TITLE)
    TITLE = ' Finder'
    banner(WHITE, TITLE)
    TITLE = '  File'
    banner(RED, TITLE)

    # parse parameters
    
    f = open(sys.argv[1])

    known = []
    unknown = []
    
    for linea in f:
        new = True
        try:
            planeID = linea.split(',')[4]
            if not planeID:
                continue
        except:
            continue
        try:
            if planeID in known:
                continue
            elif planeID in unknown:
                new = False
        except:
            logRED( "New Plane " + planeID )

        if new:
            aircrafts[ planeID ] = Plane( planeID )
            logPINK ( "New plane created for %s" % planeID )
 
        try:
            if linea.split(',')[10] != '' and not aircrafts[ planeID ].isKnown:
                logYELLOW( 'Checking ' + planeID )
                aircrafts[ planeID ].isKnown = aircrafts[ planeID ].identify(linea.split(',')[10])
            if aircrafts[ planeID ].isKnown:
                if planeID in unknown: # it may be acknowloedged with the first line 
                    unknown.pop(unknown.index( planeID ))
                known.append ( planeID )
                logBLUE( planeID + " acknowledged")
            if new and not planeID in known:
                unknown.append( planeID )
            if  planeID in unknown and len(linea) > 4 :
                aircrafts[ planeID ].saveLine( linea )
        except ImportError as e:
            logERROR(' Error processing: ')
            logERROR( str(linea))
            logERROR( e )

if __name__ == "__main__":
    main()

