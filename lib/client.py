from util import *


Util.log("Building Client Auth class", 5 )
class ClientAuth:
    def authTokenResponse(self):
        connect = ConnectCommand()
        Util.log("Setting auth response...")
        setattr(connect, 'data', {
            'token': str(self.token)
        })
        setattr(connect, 'message', "Your connection has been issued an application token.")
        return json.dumps( connect.response )
    
    def verify(self, token):
        return self.token == token

Util.log("Building Command Execution class", 5 )
class CommandExecution:
    def run(self, cmd):
        Util.log("Client of token \"" + str(self.token) + "\" is calling run on " + cmd.name )
        if cmd.name in self.allowed_commands:
            if cmd.method == "local":
                return cmd.run()    

Util.log("Building Client class", 5 )
class Client( ClientAuth, CommandExecution ):
    token = ""
    
    def __init__(self, token=False):
        Util.log("Creating a new Client of type " + self.type, 3)
        self.token = isinstance(token, Token) and token or Token("connect")
