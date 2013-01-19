#!/usr/bin/env python 

""" 
Server
"""

import socket
import sys
import json
import random
import string
from pprint import pprint
from datetime import date

host = ''
port = 9099
backlog = 5
size = 1024
listen = 1

class Token:
	seed = (string.ascii_lowercase + string.ascii_uppercase + string.digits)

	def __init__(self, type):
		
		dateObj = date.today()
		dateToken = str( dateObj.year ) + str( dateObj.month ) + str( dateObj.day) 
		randToken = ''.join( random.choice( self.seed ) for x in range(5) )
		self.token = str(randToken) + str(dateToken)

		self.setType( type )
	
	def setType(self, type):
		if type == "connect":
			self.message = '{"data":{"token":"' + self.token + '"},"status":{"code":0}}'
		

print 'Creating Socket...'

# create an INET, STREAMing socket
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
except socket.gaierror:
	#could not resolve
	print 'Could not connect to socket!'
	sys.exit()

print 'Binding to socket on ' + str(port)

# Bind socket
s.bind((host,port))

# Listen the socket
s.listen(backlog)

while listen:
	print "Listening..."
	client, address = s.accept()
	
	data = client.recv(size)

	print "Got some data!"
	if data:
		token = Token("connect")
		client.send( token.message )
		pprint(data)

		if data.strip() == "exit":
			print "Time to go bye bye"
			listen = 0

			print "Closing..."
			client.close()

			break

		cmd = json.loads(data)
		
		print "Request to call "+cmd['name']
s.close()
sys.exit()
