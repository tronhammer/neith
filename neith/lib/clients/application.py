from .. import util
from client import *

util.log("Building App Client class")
class AppClient( Client ):
    type = "application"
    allowed_commands = ["info"]
