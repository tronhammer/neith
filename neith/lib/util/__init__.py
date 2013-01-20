print "Util modules being read in..."

__all__ = ["logger", "status", "clientToken"]

from logger import *
from status import *
from clientToken import *

# Actual Util definitions

logger.log("Building Util Module")      
namespace = "tronnet"

# pass through
log = logger.log
printException = logger.printException