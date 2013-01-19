from util import *

Util.log("Building Status")
class Status:
    code = 0
    message = 0
    
    def __init__(self, status, code):
        Util.log("Creating a Status...", 5 )
        if type(status) is str:
            self.message = status
            self.code = code    
        elif type(status) is dict:
            self.message = status["message"]
            self.code = status["code"]
        elif isinstance(status, Status):
            self.message = status.message
            self.code = status.code
