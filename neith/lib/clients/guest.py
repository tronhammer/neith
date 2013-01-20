from .. import util
from client import *

util.log("Building Guest Client class", 5 )
class GuestClient( Client ):
    type = "guest"
    allowed_commands = ["connect"]