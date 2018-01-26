#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from gui import *

class Socket:
    '''Manages the connection to the dump1090 streaming port'''
    def __init__(self, ip, port):
        self.server = (ip, port)
        self.conn = self.connect()
        self.buff = ''

    def connect(self):
        ''' connects to ip,port and returns a pointer to the connection'''
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logINFO('starting up on %s port %s' % (self.server[0], self.server[1]))
        self.sock.connect(self.server)

    def readlines(self):
        '''reads a line from buffer and returns it'''
        # read a line from buffer
        chunk = self.sock.recv(1024)
        msg = chunk.split(b'\r\n')
        if msg[0][:3] != b'MSG':
            msg[0] = self.buff + msg[0]
            self.buff = msg.pop()
        else:
            msg.append(self.buff)
            self.buff = msg.pop(-2)
        return  msg

