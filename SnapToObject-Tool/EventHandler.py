import bpy
from bpy.app import handlers
from bpy.app import driver_namespace

class EventHandler(object):
    handlerList = None
    handler_keys = None
    def __init__(self, handler_list):
        self.handlerList = handler_list
        self.handler_keys = []
        
    def add(self, handler, key):
        if (key not in driver_namespace):
            driver_namespace[key] = handler
            self.handler_keys.append(key)
            self.handlerList.append(handler)
        else:
            # To prevent the accidental addition of an event handler of the same key
            self.handlerList.remove(driver_namespace[key])
            del driver_namespace[key]
            if (key in self.handler_keys):
                self.handler_keys.remove(key)
    def remove(self, key):
        if (key in diver_namespace):
            self.handlerList.remove(driver_namespace[key])
            del driver_namespace[key]
            if (key in self.handler_keys):
                self.handler_keys.remove(key)
        
    def toString(self):
        for key in self.handler_keys:
            print(key + "," + str(driver_namespace[key])) 
            
    def clear(self):
        for key in self.handler_keys:
            handler = driver_namespace[key]
            self.handlerList.remove(handler)
            del driver_namespace[key]
            self.handler_keys.remove(key)
