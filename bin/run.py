#!/usr/bin/env python 

""" 
Neith
This will be the central Command and Control unit
"""

import socket
import sys, os, inspect
import traceback
import glob

# Utilized for importing the config file
from ConfigParser import SafeConfigParser

CONFIG_FILES_PARSER = SafeConfigParser()
CONFIG_FILES = ['config.ini', 'db.ini','os.ini']
CONFIG_FILES_FOUND = CONFIG_FILES_PARSER.read( CONFIG_FILES )
CONFIG_FILES_MISSING = set(CONFIG_FILES) - set(CONFIG_FILES_FOUND)

if __name__ == "__main__":
    # Global try statement in order to parse all app errors and for fault tolerancy
    try:
        # Add Neith Modules to current system path
        # Move to method of startup config class
        for path_name in CONFIG_FILES_PARSER.options("local_sys_paths"):
            cmd_folder = os.path.realpath( os.path.abspath( CONFIG_FILES_PARSER.get('local_sys_paths', path_name ) ) )
            print "About to add folder \""+ cmd_folder +"\" to system path"
            if cmd_folder not in sys.path:
                sys.path.append(cmd_folder)
            
        import neith
        assert neith.app

        neith.lib.util.log("Starting...", 3)
        neith.app.start()
    except ImportError as e:
        print "Imports are jacked up!"
        traceback.print_exc(file=sys.stdout)
    except:
        print "Unexpected error: " + str(sys.exc_info()[0])
        traceback.print_exc(file=sys.stdout)
else:
    print "Sorry, this cannot be run as a module, it must be run directly!"
    
sys.exit(0)