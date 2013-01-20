from .. import util
from command import *

util.log("Building Info Command class", 5 )
class InfoCommand( Command ):
    name = "info"
    method = "local" # could also be sys, or others
    response = {
        "data": {},
        "status":{
            "command": "info",
            "code":0
        }
    }
    
    def run(self, client):
        assert isinstance(client, Client)
        util.log("Client is attempting to run InfoCommand", 3)
        if client.legit:
            util.log("Client is legit, going to run the local command for InfoCommand", 4)
            setattr(self, 'data', {
                'blah': 'the data you requested',
                'client': client.name +" : "+ client.token
            })
            
        return self.response
