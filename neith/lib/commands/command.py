import sys, json

from .. import util

# A Command object holds all the information of a command but doesnt have the power to execute it
# A Client object must be used to execute a command in order to establish and verify permissions
util.log("Building Command class", 5 )
class Command(dict):
    raw = ""
    name = ""
    data = ""
    status = ""
    method = ""
    
    legit = 1
    
    available_params = [
        "name",
        "response"
    ]
    
    response={
        "data": {},
        "status":{
            "code":0
        }
    }
    
    
    def __init__(self, cmd=None, name=None):
        util.log("Creating a Command of type " + self.name, 5 )
        try:
            util.log("Attempting to set Command settings...", 4 )
            if type(cmd) is str:
                util.log("Settings are a string \""+ cmd +"\"", 5 )
                self.cmd = json.loads( cmd )
                util.log( self.cmd )
                self.name = self.cmd['name']
                self.raw = cmd    
            elif type(cmd) is dict:
                util.log("Settings are a dict, \"" + cmd['name'] +"\"", 5 )
                self.cmd = cmd
                self.name = cmd['name']
                self.raw = json.dumps( cmds )
            elif isinstance(cmd, Command):
                util.log("Settings are an existing Command", 5 )
                self.cmd = cmd.cmd
                self.name = cmd.name
                self.raw = cmd.raw
            else:
                util.log("Settings are not recognized", 5 )
                if name:
                    self.name = name5
        except:
            util.printException()
            self.legit = 0
    
    def __catchsetcalls__(self, key, value, setter):
        mutables = ['message','name','code','data']
        util.log("Checking if attribute "+key+" is in response code", 4 )
        if key in mutables:
            util.log("Key exists! \""+key+"\" attribute will be given the property \""+str(value)+"\"", 4 )
            if (key == 'message'):
                self.response['status']['message'] = value
            elif (key == 'name'):
                self.response['status']['name'] = value
            elif (key == 'code'):
                self.response['status']['code'] = value
            elif (key == 'data'):
                self.response['data'] = value
            util.log("Response list updated!")
        else:
            util.log("Item is not in response mutable list, setting value...", 5)
    
        setter(self, key, value)
            
    def __setitem__(self, key, value):
        util.log("Transfering dict item set", 5 )
        self.__catchsetcalls__(key, value, dict.__setitem__)
    
    def __setattr__(self, key, value):
        util.log("Transfering dict attr set", 5 )
        self.__catchsetcalls__(key, value, dict.__setattr__)
    
    def __str__(self):
        return self.response