import bpy
import EventHandler
from bpy import context

#handler_key uniquely identifies each event handler that is registered in memory, so that we can easily manage them (ie. avoid duplicate event handlers)

handler_key = "01"
def lastModifiedHandler(scene):
    print(len(context.selected_objects))

class LastModified:
    instance = None
    @staticmethod
    def getInstance():
        if (LastModified.instance == None):
            LastModified()
        return LastModified.instance
    def __init__(self):
        eventHandler = EventHandler.EventHandler(bpy.app.handlers.scene_update_post)
        if (LastModified.instance != None):
            print("Instance already exists, removing event handler now...")
            eventHandler.remove(key)
        else:
            LastModified.instance = self
            eventHandler.add(lastModifiedHandler, handler_key)







