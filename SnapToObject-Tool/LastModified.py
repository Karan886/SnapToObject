import bpy
import EventHandler
from bpy import context

#handler_key uniquely identifies each event handler that is registered in memory, so that we can easily manage them (ie. avoid duplicate event handlers)

handler_key = "01"
lastModifiedMeshName = None
def lastModifiedHandler(scene):
    global lastModifiedMeshName
    activeObjName = context.active_object.name
    if (activeObjName != lastModifiedMeshName):
        print(activeObjName)
        lastModifiedMeshName = activeObjName

class LastModified:
    __instance = None
    __eventHandler = EventHandler.EventHandler(bpy.app.handlers.scene_update_post)
    @staticmethod
    def getInstance():
        LastModified()
        return LastModified.__instance
    def __init__(self):
        if (LastModified.__instance != None):
            print("Instance already exists..")
        else:
            LastModified.__instance = self
            self.__eventHandler.add(lastModifiedHandler, handler_key)
            print("attached event handler...")
            
    def unattachEventHandlers(self):
        self.__eventHandler.clear()
        LastModified.__instance = None
        lastModifiedName = None
        print("All event handlers unattached...")




