from util import *

Util.log("Building Connect Command class", 5 )
class ConnectCommand( Command ):
    name = "connect"
    method = "local" # could also be sys, or others
    response = {
        "data": {},
        "status":{
            "command": "connect",
            "code":0
        }
    }