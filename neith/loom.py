"""Loom Module module

Utilized for socket management and command forwarding between Clients 
and the Loom
"""

import sys, socket

# Class structure is a two level paradigm
# Parent (direct utilization object)
#   These are what the app will be using to interact commands
# _SubClass (only meant to be extended into a Parent)
#   These rely on a parent class to function correctly
# _ContainerClass_
#   Used only for static information

from lib import *

#######################################################  --> APPLICATION <--  #######################################################
util.log("Building Application class", 5 )

socket_host = ''
socket_port = 9099
socket_backlog = 5
socket_size = 1024

def weave( config ):
    """Creates a socket on a specified port for listening"""
    util.log("Application calls start", 5 )
    util.log('Creating Socket...', 3 )
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.gaierror:
        util.log( 'Could not connect to socket!', 1 )
        sys.exit()
    util.log( 'Binding to socket on ' + str(config['port'] or socket_port),  )
    sock.bind( (socket_host, int(config['port'] or socket_port) ) )
    sock.listen( socket_backlog )
    open(sock)
    util.log("Exiting out!")
    sock.close()
    sys.exit()
                
def open(sock):
    """Opens the socket for listening and piping Commands to their respective Clients"""
    socket_listen = 1
    socket_client = None
    address = None
    socket_client = None
    open_clients = {}
    
    util.log("Opening the socket", 3 )
    while socket_listen:
        if not socket_client:
            util.log("Accepting Connections...")
            socket_client, address = sock.accept()
        util.log("Listening...", 3)
        # eventually we will loop this until we get a specified token for end of input
        data = socket_client.recv( socket_size )
        util.log("Got some data!" + data, 4)
        if data:
            if data.strip() == "exit":
                util.log("Time to go bye bye", 2)
                socket_listen = 0
                util.log("Closing...", 1)
                socket_client.close()
                break
            else:
                cmd = commands.BasicCommand( data )
                util.log("New Basic Command created", 5)
                util.log(cmd, 5)
                util.log("Checking what command has been requested", 5 )
                if 'token' in cmd:
                    util.log("Got a command for " + cmd.name, 3 )
                    cmd.response['status']['message'] = "Got a command for " + cmd.name
                    socket_client.send( cmd.response )
                    app_client = open_clients[ str(cmd.token) ]
                    if isinstance(app_client, clients.GuestClient):
                        clients[ str(cmd.token) ] = clients.AppClient( clients.GuestClient )
                    app_client.run( cmd )
                elif cmd.name == "connect":
                    util.log("Connect command requested!", 5)
                    util.log("Creating a Guest Client...", 5)
                    app_client = clients.GuestClient()
                    util.log("Made a guest client with token "+ str(app_client.token), 3)
                    open_clients[ str(app_client.token) ] = app_client
                    socket_client.send( app_client.authTokenResponse() )
                else:
                    util.log("Command sent over did not represent any known configuration!", 2 )
                    util.log( cmd , 4 )
                    socket_client.sendall('{"status":{"code":0,"message":"command executed succesfully!"}}')
            util.log("Command "+cmd.name+" executed")