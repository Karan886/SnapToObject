import bpy
import EventHandler
from bpy import context

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
        if (LastModified.instance != None):
            print("Instance already exists, removing event handler now...")
            eventHandler.add(lastModifiedHandler, handler_key)
        else:
            LastModified.instance = self
            eventHandler = EventHandler.EventHandler(bpy.app.handlers.scene_update_post)
            eventHandler.add(lastModifiedHandler, handler_key)



            






