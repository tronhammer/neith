import string, random
from datetime import date

import logger

#######################################################  --> TOKENs <--  #######################################################
logger.log("Building Client Token class")
class ClientToken:
    seed = (string.ascii_lowercase + string.ascii_uppercase + string.digits)
    type = "connect"
        
    def __init__(self, type="connect"):
        logger.log("Creating a Token of type " + type, 3 )
        dateObj = date.today()
        dateToken = str( dateObj.year ) + str( dateObj.month ) + str( dateObj.day) 
        randToken = ''.join( random.choice( self.seed ) for x in range(5) )
        logger.log("Building token string", 4 )
        self.token = str(randToken) + str(dateToken)
        self.setType( type )
    
    def __str__(self):
        return self.token
    
    def setType(self, type):
        logger.log("Setting toke type", 3 )
        self.type = type
        if type == "connect":
            self.message = '{"data":{"token":"' + self.token + '"},"status":{"code":0}}'
