###
# THIS FILE IS CURRENTLY NOT BEING USED!
##

util.log("Building Commands class", 5 )
class Commands:
    levels = ["guest","application","service"]
    available = {
        "basic": ([1,2], BasicCommand),
        "connect": ([1], ConnectCommand),
        "info": ([2,3], InfoCommand)
    }
