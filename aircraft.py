#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import datetime
from gui import *
from ICAO import *


class Plane:
    def __init__ (self, modeS):
        self.path = 'dumps/'
        self.modeS = modeS
        self.isKnown = False
        self.file = open( self.path + self.modeS + '.csv', 'a' )
        self.last = datetime.datetime.now()
        self.data = {}

    def identify ( self, flightID):
        ''' str -> bool
        checks if flightID is a know flight identifier and returns
        boolean'''
        if flightID[:2] in ICAO or flightID[:3] in ICAO:
            try:
                self.file.close()
                os.remove ( self.path + self.modeS + '.csv' )
                logDEBUG( '%s is being removed' % self.modeS )
            except:
                logCRITICAL('Error removing file for ' + self.modeS)
                #pass
            return True
        else:
            pass
        return False

    def saveLine ( self, line ):
        ''' str -> None
        if unknow flight save line to file'''
        icao = line.split(',')[10] 
        if not self.isKnown: 
                self.isKnown = self.__knownICAO__( icao )
        if not self.isKnown:
            self.__dumpLine__( line )
        else:
            try:
                logDEBUG( '%s 2 is being removed' % self.modeS )
                self.file.close()
                self.os.remove( self.path + self.icao + '.csv')
            except:
                logCRITICAL('Error2 removing file for ' + self.modeS)
                pass

    def __dumpLine__( self, line):
        ''' str -> None
        save line to file'''
        self.file.write( line )
        self.file.flush()

    def __knownICAO__( self, icao ):
        ''' str -> bool
        checks if flightID is a know flight identifier and returns bool'''
        if icao[:2] in ICAO or icao[:3] in ICAO:
            logWARNING( 'Known ' + self.modeS )
            return True
        #elif isBlockedFA( self.icao, userFA, apikeyFA):
        #    return True
        return False



if __name__ == "__main__":

    TITLE = 'FlightFinder'
    banner(GREEN, TITLE)
    logERROR( "Use only as library" )


