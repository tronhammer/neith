import socket
import sys

from util import *
from status import *
from clientToken import *

from client import *
from clients.guest import *
from clients.application import *
from clients.service import *

from command import *

#Conditionally include these based on client type
from commands.basic import *
from commands.connect import *
from commands.info import *

#######################################################  --> APPLICATION <--  #######################################################
Util.log("Building Application class", 5 )
class App:
    socket_host = ''
    socket_port = 9099
    socket_backlog = 5
    socket_size = 1024
    socket_listen = 1
    cmds = {}
    client = None;
    address = None;
    clients = {}
        
    def __init__(self, connection_args, auto_start=False):
        Util.log("Creating Application", 5 )
        for k in connection_args:
            setattr(self, k, connection_args[k])
        if auto_start:
            self.start()

    def start(self):
        Util.log("Application calls start", 5 )
        Util.log('Creating Socket...', 3 )
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.gaierror:
            Util.log( 'Could not connect to socket!', 1 )
            sys.exit()
        Util.log( 'Binding to socket on ' + str(self.socket_port),  )
        self.sock.bind( (self.socket_host, self.socket_port) )
        self.sock.listen( self.socket_backlog )
        self.open()
        Util.log("Exiting out!")
        self.sock.close()
        sys.exit()
                
    def open(self):
        Util.log("Opening the socket", 3 )
        while self.socket_listen:
            if not self.client:
                Util.log("Accepting Connections...")
                self.client, self.address = self.sock.accept()
            Util.log("Listening...", 3)
            data = self.client.recv( self.socket_size )
            Util.log("Got some data!" + data, 4)
            if data:
                if data.strip() == "exit":
                    Util.log("Time to go bye bye", 2)
                    self.socket_listen = 0
                    Util.log("Closing...", 1)
                    self.client.close()
                    break
                else:
                    cmd = BasicCommand( data )
                    Util.log("New Basic Command created", 5)
                    Util.log(cmd, 5)
                    Util.log("Checking what command has been requested", 5 )
                    if 'token' in cmd:
                        Util.log("Got a command for " + cmd.name, 3 )
                        cmd.response['status']['message'] = "Got a command for " + cmd.name
                        self.client.send( cmd.response )
                        app_client = self.clients[ str(cmd.token) ]
                        if isinstance(app_client, GuestClient):
                            self.clients[ str(cmd.token) ] = AppClient( GuestClient )
                        app_client.run( cmd )
                    elif cmd.name == "connect":
                        Util.log("Connect command requested!", 5)
                        Util.log("Creating a Guest Client...", 5)
                        app_client = GuestClient()
                        Util.log("Made a guest client with token "+ str(app_client.token), 3)
                        self.clients[ str(app_client.token) ] = app_client
                        self.client.send( app_client.authTokenResponse() )
                    else:
                        Util.log("Command sent over did not represent any known configuration!", 2 )
                        Util.log( cmd , 4 )
                Util.log("Command "+cmd.name+" executed")
                self.client.sendall('{"status":{"code":0,"message":"command executed succesfully!"}}')