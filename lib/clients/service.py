from util import *
from client import *

Util.log("Building Service Client class")
class ServiceClient( Client ):
    type = "service"
    allowed_commands = [""]
