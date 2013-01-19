#!/usr/bin/env python 

""" 
Neith
This will be the central Command and Control unit
"""

import socket
import sys, os, inspect

LIB = "lib"

# Class structure is a two level paradigm
# Parent (direct utilization object)
#   These are what the app will be using to interact commands
# _SubClass (only meant to be extended into a Parent)
#   These rely on a parent class to function correctly
# _ContainerClass_
#   Used only for static information

try:
    cmd_folder = os.path.realpath(
        os.path.abspath(
            os.path.split(
                inspect.getfile(
                    inspect.currentframe() 
                )
            )[0]
        )
    )
    if cmd_folder not in sys.path:
        sys.path.insert(0, cmd_folder)

     # use this if you want to include modules from a subforder
    cmd_subfolder = os.path.realpath( 
        os.path.abspath( 
            os.path.join( 
                os.path.split( 
                    inspect.getfile( 
                        inspect.currentframe() 
                    ) 
                )[0],
                LIB
            ) 
        )
    )
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)
    
    assert lib
    
    from lib import *
    from util import *
    from app import *

    assert Util
    assert App

    Util.log("Imported Util!")
except ImportError as e:
    print "Imports are jacked up!"
except Exception as e:
    print e.message
            
#######################################################  --> COMMANDS <--  #######################################################





try:
    app = App({
        "socket_host": '',
        "socket_port": 9099,
        "socket_backlog": 5,
        "socket_size": 1024
    })

    Util.log("Starting...", 3)
    app.start()
except:
    Util.log("Unexpected error:" + str(sys.exc_info()[0]), 1 )
    traceback.print_exc(file=sys.stdout)
