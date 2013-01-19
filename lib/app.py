import socket
import sys

from util import *


#######################################################  --> APPLICATION <--  #######################################################
Util.log("Building Application class", 5 )
class App:
    socket_host = ''
    socket_port = 9099
    socket_backlog = 5
    socket_size = 1024
    socket_listen = 1
    cmds = {}
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
        Util.log("Existing out!")
        self.sock.close()
        sys.exit()
                
    def open(self):
        Util.log("Opening the socket", 3 )
        while self.socket_listen:
            Util.log("Listening...", 3)
            client, address = self.sock.accept()
            data = client.recv( self.socket_size )
            Util.log("Got some data!" + data, 4)
            if data:
                if data.strip() == "exit":
                    Util.log("Time to go bye bye", 2)
                    self.socket_listen = 0
                    Util.log("Closing...", 1)
                    client.close()
                    break
                else:
                    cmd = BasicCommand( data )
                    if hasattr(cmd, 'token'):
                        Util.log("Got a command for " + cmd.name, 3)
                        cmd.response['status']['message'] = "Got a command for " + cmd.name
                        client.send( cmd.response )
                        app_client = self.clients[ str(cmd.token) ]
                        if isinstance(app_client, GuestClient):
                            self.clients[ str(cmd.token) ] = AppClient( GuestClient )
                        app_client.run( cmd )
                    elif cmd.name == "connect":
                        app_client = GuestClient()
                        Util.log("Made a guest client with token "+ str(app_client.token), 3)
                        self.clients[ str(app_client.token) ] = app_client
                        client.send( app_client.authTokenResponse() )
                Util.log("Request to call " + cmd.name)