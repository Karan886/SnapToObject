import bpy
import EventHandler
from bpy import context

def handler(scene):
    print(len(context.selected_objects))
    
eventHandler = EventHandler.EventHandler(bpy.app.handlers.scene_update_post)
eventHandler.add(handler, "01")
eventHandler.add(handler, "01")


        






