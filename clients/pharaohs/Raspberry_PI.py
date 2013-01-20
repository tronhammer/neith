#!/usr/bin/env python 

""" 
Dest client
This will be used to connect a dest ("destiny"/"destination") client to Neith ("The weaver of destinies")
"""

import sys, socket, os, inspect, traceback, json, getopt

exit_clear = 0
sock = None

def main(argv):
    global sock
    
    # Settable via command line
    _defined = {
        'port': 9099,
        'host': 'localhost',
        'command':''
    }
    
    _builtin = {}
    
    _settings = dict( _defined.items() + _builtin.items() )
    
    # Get passed arguments and map them
    try:                                
        opts, args = getopt.getopt(argv, "h:p:c:?", ["host=", "port=", "command=", "help"])
    except getopt.GetoptError:          
        usage()
        sys.exit(2)                     
    for opt, arg in opts:                
        if opt in ("--help"):      
            usage()
            sys.exit(0)
        elif opt in ("-c", "--command"): 
            _settings['command'] = arg
        elif opt in ("-h", "--host"): 
            _settings['host'] = arg
        elif opt in ("-p", "--port"):
            _settings['port'] = int(arg)
    
    start( _settings )
    
def start( config ):
    global sock
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.gaierror:
        sys.exit()
        
    sock.connect(( socket.gethostbyname( config['host'] ) , config['port'] ))
    
    open( config['command'] )
                
def open( command ):
    global sock
    socket_listen = 1
    address = None
    socket_client = None
    open_clients = {}
    socket_size = 1024
    
    
    print "Requesting a token..."
    sock.sendall('{"name":"connect"}')
    
    while socket_listen:

        # eventually we will loop this until we get a specified token for end of input
        data = sock.recv( socket_size )
        data = data.strip()
        
        if data:
            print "Received data!"
            print data
            
            data = json.loads( data )
            if type(data) is dict and 'data' in data:
                data = data['data']
                if data['token']:
                    print "Got token!"
                    if not command:
                        command = raw_input("Execute command: ")
                    command = json.loads( command )
                    command['token'] = data['token']
                    command = json.dumps( command )
                    print "Executing command! "
                    print command
                    sock.sendall( command )
                else:
                    print "Object didnt have token, exiting out"
                    socket_listen = 0
                    break;
            else:
                print "Object didnt have data, exiting out"
                socket_listen = 0
                break;


def usage():
    global exit_clear
    exit_clear = 1
    print "This is the help text for the Neith dest.py command which will connect this device to the Neith engine."
    print "Typical usage:"
    print "     python dest.py [-p port]  [-h address]"
    print ""
    print "Arguments:"
    print "     -?, --help                 Displays this help text"
    print "     -h, --host=address         Allows you to specify which directory the config files should be loaded from"
    print "     -p, --port=port            Allows you to change the port that the Neith engine runs on"
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
    finally:
        sock.sendall("exit")
        sock.close()
    
else:
    print "Sorry, this cannot be run as a module, it must be run directly!"

sys.exit(0)
