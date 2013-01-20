from .. import util
from client import *

util.log("Building Service Client class")
class ServiceClient( Client ):
    type = "service"
    allowed_commands = [""]
