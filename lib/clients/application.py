from util import *

Util.log("Building App Client class")
class AppClient( Client ):
    type = "application"
    allowed_commands = ["info"]
