"""Library module

Contains a repository of all the Library modules available to the 
Neith Loom Engine. This also contains the definitions for Clients 
and Commands that will largely represent the transactions taking 
place in the Loom"""

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