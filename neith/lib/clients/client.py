import json

from .. import util
from .. import commands

util.log("Building Client Auth class", 5 )
class ClientAuth:
    def authTokenResponse(self):
        connect = commands.ConnectCommand()
        util.log("Setting auth response...")
        setattr(connect, 'data', {
            'token': str(self.token.token)
        })
        setattr(connect, 'message', "Your connection has been issued an application token.")
        return json.dumps( connect.response )
    
    def verify(self, token):
        return self.token == token

util.log("Building Command Execution class", 5 )
class CommandExecution:
    def run(self, cmd):
        util.log("Client of token \"" + str(self.token.token) + "\" is calling run on " + cmd.name )
        if cmd.name in self.allowed_commands:
            if cmd.method == "local":
                return cmd.run()    

util.log("Building Client class", 5 )
class Client( ClientAuth, CommandExecution ):
    token = ""
    
    def __init__(self, token=False):
        util.log("Creating a new Client of type " + self.type, 3)
        self.token = isinstance(token, util.ClientToken) and token or util.ClientToken("connect")
