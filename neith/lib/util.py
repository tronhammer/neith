import sys, traceback
from pprint import pprint

pprint("Building Logger class")
class Logger:
    level = 5
    debug = 1
    
    # Support for Internationalization
    
    @staticmethod
    def log(msg, lvl=3):
        assert isinstance(lvl, int)
        if lvl <= Logger.level:
            pprint(msg)
            
    def printException():
        traceback.print_exc(file=sys.stdout)

pprint("Building Util class")      
class Util( Logger ):
    namespace = "tronnet"
