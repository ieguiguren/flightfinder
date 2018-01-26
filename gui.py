#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from pyfiglet import Figlet
except:
    #    print ("Error: %s \n" % (e))
    print("Try this ... pip install -r /path/to/requirements.txt")

PINK = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
WHITE = '\033[0m'
ENDC = WHITE
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
WARNING = BOLD + '\033[93m'
ERROR = BOLD + '\033[91m'

def banner( colour, text):
    ''' str, str -> None 
    recieves string colour and string text and prints a banner in such
    colour'''
    Graph = Figlet(font='slant')
    GraphRender = Graph.renderText(text)
    print ( BOLD + colour + GraphRender + ENDC )

def logDEBUG( text ):
    print ( BOLD + WHITE + '[+] ' + ENDC + GREEN + text )

def logINFO( text ): 
    print ( BOLD + WHITE + '[+] ' + ENDC + BLUE + text )

def logWARNING( text ): 
    print ( BOLD + WHITE + '[+] ' + ENDC + YELLOW + text )

def logERROR ( text ): 
    print ( BOLD + WHITE + '[+] ' + ENDC + RED + text )

def logCRITICAL ( text ): 
    print ( BOLD + WHITE + '[+] ' + ENDC + PINK + text )

def logPINK( text ): 
    print ( BOLD + WHITE + '[+] ' + ENDC + PINK  + text )

def logBLUE( text ): 
    print ( BOLD + WHITE + '[+] ' + ENDC + BLUE  + text )

def logGREEN( text ): 
    print ( BOLD + WHITE + '[+] ' + ENDC + GREEN  + text )

def logYELLOW( text ): 
    print ( BOLD + WHITE + '[+] ' + ENDC + YELLOW  + text )

def logRED( text ): 
    print ( BOLD + WHITE + '[+] ' + ENDC + RED  + text )

def logWHITE( text ): 
    print ( BOLD + WHITE + '[+] ' + ENDC + WHITE  + text )
