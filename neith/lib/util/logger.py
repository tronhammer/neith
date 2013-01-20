import sys, traceback
from pprint import pprint

pprint("Building Logger class")
level = 5
debug = 1
    
# Support for Internationalization
    
def log(msg, lvl=3):
    assert isinstance(lvl, int)
    if lvl <= level:
        pprint(msg)
            
def printException():
    log("Unexpected error:" + str(sys.exc_info()[0]), 2 )
    traceback.print_exc(file=sys.stdout)