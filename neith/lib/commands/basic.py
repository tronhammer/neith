from .. import util
from command import *

# Command Classes Available
util.log("Building Basic Command class", 5 )
class BasicCommand( Command ):
    name = "basic"
    response = {
        "data": {},
        "status":{
            "command": "basic",
            "code":0
        }
    }