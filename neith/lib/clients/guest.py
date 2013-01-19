from util import *
from client import *

Util.log("Building Guest Client class", 5 )
class GuestClient( Client ):
    type = "guest"
    allowed_commands = ["connect"]