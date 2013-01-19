import json

from util import *


# A Command object holds all the information of a command but doesnt have the power to execute it
# A Client object must be used to execute a command in order to establish and verify permissions
Util.log("Building Command class", 5 )
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
        Util.log("Creating a Command of type " + self.name, 5 )
        try:
            Util.log("Attempting to set Command settings...", 4 )
            if type(cmd) is str:
                Util.log("Settings are a string \""+ cmd +"\"", 5 )
                Util.log("Attempting to parse string into JSON object", 5 )
                self.cmd = json.loads( cmd )
                Util.log("All gravy")
                Util.log( self.cmd )
                Util.log("Got json object with command name \""+self.cmd['name']+"\"!", 5 )
                self.name = self.cmd['name']
                self.raw = cmd    
            elif type(cmd) is dict:
                Util.log("Settings are a dict, \"" + cmd['name'] +"\"", 5 )
                self.cmd = cmd
                self.name = cmd['name']
                self.raw = json.dumps( cmds )
            elif isinstance(cmd, Command):
                Util.log("Settings are an existing Command", 5 )
                self.cmd = cmd.cmd
                self.name = cmd.name
                self.raw = cmd.raw
            else:
                Util.log("Settings are not recognized", 5 )
                if name:
                    self.name = name
                    
            if self.name not in Commands.client:
                Util.log("Command is allowed for clients", 4 )
        except:
            Util.log("Unexpected error:" + str(sys.exc_info()[0]), 2 )
            Util.log("There was an issue loading the Command settings!", 1 )
            traceback.print_exc(file=sys.stdout)
            self.legit = 0
    
    def __catchsetcalls__(self, key, value, setter):
        mutables = ['message','name','code','data']
        Util.log("Checking if attribute "+key+" is in response code", 4 )
        if key in mutables:
            Util.log("Key exists! \""+key+"\" attribute will be given the property \""+value+"\"", 4 )
            if (key == 'message'):
                self.response['status']['message'] = value
            elif (key == 'name'):
                self.response['status']['name'] = value
            elif (key == 'code'):
                self.response['status']['code'] = value
            elif (key == 'data'):
                self.response['data'] = value
            Util.log("Response list updated!")
        else:
            Util.log("Item is not in response mutable list, setting value...", 5)
            setter(self, key, value)
            
    def __setitem__(self, key, value):
        self.__catchsetcalls__(key, value, dict.__setitem__)
    
    def __setattr__(self, key, value):
        self.__catchsetcalls__(key, value, dict.__setattr__)
