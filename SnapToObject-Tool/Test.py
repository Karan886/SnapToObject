import bpy
import mathutils
from bpy import context
from mathutils import Vector

def setOriginToCenter(objects):
    array = []
    for obj in objects:
        obj.select = True
        prevLoc = Vector((obj.location.x, obj.location.y, obj.location.z))
        bpy.ops.object.origin_set(type = "ORIGIN_CENTER_OF_MASS")  
        displacement = prevLoc - obj.location
        obj.select = False
        array.append(displacement)
    return array

def restoreOrigin(obj, disp):
    obj.select = True
    context.scene.cursor_location = obj.location + disp
    bpy.ops.object.origin_set(type = "ORIGIN_CURSOR")
    obj.select = False 

def getSecondObject():
    list = context.selected_objects
    if (list[0].name == context.active_object.name):
        return list[1]
    return list[0]
    
if (len(context.selected_objects) == 2):
    obj = context.active_object
    obj_two = getSecondObject()
    
    list = context.selected_objects
    for o in list:
        d.select = False
        
    disp = setOriginToCenter([obj, obj_two])
    obj.location.x += 5
    obj_two.location.x += 5
    restoreOrigin(obj, disp[0])
    restoreOrigin(obj_two, disp[1])
    
    