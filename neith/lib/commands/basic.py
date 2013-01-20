from util import *
from status import *
from client import *
from command import *

# Command Classes Available
Util.log("Building Basic Command class", 5 )
class BasicCommand( Command ):
    name = "basic"
    response = {
        "data": {},
        "status":{
            "command": "basic",
            "code":0
        }
    }