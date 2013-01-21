#!/usr/bin/env python 

""" 
Neith
This will be the central Command and Control unit
"""

import sys, socket, os, traceback, getopt

# Utilized for importing the config file
from ConfigParser import SafeConfigParser

exit_clear = 0

def main(argv):
    # Settable via command line
    _defined = {
        'config_dir': None,
        'port': None,
        'debug': 0
    }
    
    # Get passed arguments and map them
    try:                                
        opts, args = getopt.getopt(argv, "hdc:p:", ["help", "debug", "config-directory=", "port="])
    except getopt.GetoptError:          
        usage()
        sys.exit(2)                     
    for opt, arg in opts:                
        if opt in ("-h", "--help"):      
            usage()
            sys.exit(0)
        elif opt in ("-d", "--debug"):
            global _debug
            _defined['debug'] = 1 
        elif opt in ("-c", "--config-directory"): 
            _defined['config_dir'] = arg
        elif opt in ("-p", "--port"): 
            _defined['port'] = arg
    
    # Get configurations
    CONFIG_PATH = _defined['config_dir'] or "../config/"
    CONFIG_FILES_PARSER = SafeConfigParser()
    CONFIG_FILES = [ 
        os.path.realpath( os.path.abspath( CONFIG_PATH + "config.ini" ) ), 
        os.path.realpath( os.path.abspath( CONFIG_PATH + "db.ini" ) ),
        os.path.realpath( os.path.abspath( CONFIG_PATH + "os.ini") )
    ]
    CONFIG_FILES_FOUND = CONFIG_FILES_PARSER.read( CONFIG_FILES )
    CONFIG_FILES_MISSING = set(CONFIG_FILES) - set(CONFIG_FILES_FOUND)
    

    # Add Neith Modules to current system path
    # Move to method of startup config class
    for path_name in CONFIG_FILES_PARSER.options("local_sys_paths"):
        cmd_folder = os.path.realpath( os.path.abspath( CONFIG_FILES_PARSER.get('local_sys_paths', path_name ) ) )
        print "About to add folder \""+ cmd_folder +"\" to system path"
        if cmd_folder not in sys.path:
            sys.path.append(cmd_folder)
            
    import neith
    assert neith.loom

    neith.lib.util.log("Starting...", 3)
    neith.loom.weave( _defined )

def usage():
    global exit_clear
    exit_clear = 1
    print "This is the help text for the Neith run.py command"
    print "Typical usage:"
    print "     python run.py [-p port]  [-c config_directory]"
    print ""
    print "Arguments:"
    print "     -h                                  Displays this help text"
    print "     -c, --config-directory=FULLPATH     Allows you to specify which directory the config files should be loaded from"
    print "     -p, --port=                         Allows you to change the port that the Neith engine runs on"
    print ""

if __name__ == "__main__":
    # Global try statement in order to parse all app errors and for fault tolerancy
    try:
        main(sys.argv[1:])
    except ImportError as e:
        print "Imports are jacked up!"
        traceback.print_exc(file=sys.stdout)
    except:
        if not exit_clear:
            print "Unexpected error: " + str(sys.exc_info()[0])
            traceback.print_exc(file=sys.stdout)
    
else:
    print "Sorry, this cannot be run as a module, it must be run directly!"

sys.exit(0)