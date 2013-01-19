from util import *
from client import *

Util.log("Building App Client class")
class AppClient( Client ):
    type = "application"
    allowed_commands = ["info"]
