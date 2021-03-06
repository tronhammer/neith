""":mod:`neith` -- Neith Loom Engine
=============================

.. module:: neith
   :platform: Mac, Unix
   :synopsis: The module builds out the necessary library files required for 
        opening a socket by which Clients can communicate securely commands 
        and results in a continous fashion.
.. moduleauthor:: Sean Murray <smurray@python.invalid>
.. function:: run_unit_test(msg)

Neiths Loom
    The central cortex of the application. Its main function is to accept 
    incomming connections, identify Commands, create Clients, verify 
    Client authentication and token distribution, and if the permission 
    set allows for it, forward commands from one Client to another

Pharaoh
    A Client created by Neiths Loom that has a session access token and 
    a preloaded package of destinies.
    
    These are created via command line interface::
        
        $: neith/bin/create_deity -n "NAME" -c "COMMAND, ..." -d "DISTO_TYPE"
    
    Dieties will then be made available in::
        
        $: neith/deities/clients/DISTRO_TYPE/NAME
        
    The server admin can then distribute the Deity Client to trusted parties
    
Deity
    A Client created by Neiths Loom that has a permanant access token and 
    a preloaded package of destinies. 
    
    These are created via command line interface::
        
        $: neith/bin/create_deity -n "NAME" -c "COMMAND, ..." -d "DISTO_TYPE"
    
    Dieties will then be made available in::
        
        $: neith/deities/clients/DISTRO_TYPE/NAME
        
    The server admin can then distribute the Deity Client to trusted parties

Destiny
    A Command issued from Neiths Loom by which all Dynasties must obay. 
    Commands advocated are generally limited to the capabilities of the 
    Dynasty.

>>> run_unit_test("test_token")
'testo'
"""
print "Neith modules being read in..."

__all__ = ["lib", "app"]

import lib
import app

def run_unit_test(msgo):
    """Return a success of true or false

    >>> lib.util.log("test_token")
    'test_token'
    """
    
    lib.util.log( msgo )
    
# Only time this module should be run directly is for test units
if __name__ == "__main__":
    print "==> RUNNING UNIT TESTS"
    import doctest
    doctest.testmod(verbose=True)