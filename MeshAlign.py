#This AddOn helps align/organize a collection of scene meshes so that the artist 
#doesn't have to do all the work. Note: the way objects are positioned depends on where the origin is set.

import bpy
import mathutils
from bpy import context
from bpy import props

def isSelectedValid(objOne, objTwo):
    return objOne.type == "MESH" and objTwo.type == "MESH"

def getSecondObject():
    list = context.selected_objects
    if (list[0].name == context.active_object.name):
        return list[1]
    return list[0]

# Returns the displacement so that origin can be restored
def setOriginToCenter(obj):
    obj.select = True
    prevLoc = obj.location
    bpy.ops.object.origin_set(type = "ORIGIN_CENTER_OF_MASS")  
    displacement = prevLoc - obj.location
    obj.select = False
    return displacement

def restoreOrigin(obj, disp):
    obj.select = True
    context.scene.cursor_location = obj.location + disp
    bpy.ops.object.origin_set(type = "ORIGIN_CURSOR")
    obj.select = False 
    
def alignMesh(options, objOne, objTwo):
    xoffset = options["xoffset"]
    yoffset = options["yoffset"]
    zoffset = options["zoffset"]
    snapAxis = options["snapAxis"]
    
    newLocationVector = [objOne.location.x + xoffset, objOne.location.y + yoffset, objOne.location.z + zoffset]
    if (snapAxis == "X"):
        newLocationVector[0] += objOne.dimensions.x/2 + objTwo.dimensions.x/2
    elif(snapAxis == "Y"):
        newLocationVector[1] += objOne.dimensions.y/2 + objTwo.dimensions.y/2
    elif(snapAxis == "Z"):
         newLocationVector[2] += objOne.dimensions.z/2 + objTwo.dimensions.z/2
         
    objTwo.location = newLocationVector

class SnapToObject(bpy.types.Operator):
    bl_idname = "view3d.snap_to_object"
    bl_label = "Snap To Object" 
    
    axesEnum = props.EnumProperty(
        items = (("X", "x", "xoffset"), ("Y", "y", "yoffset"), ("Z", "z", "zoffset")),
        name = "Snap Axis:",
        default = "X"
    )
    
    axesOffset = props.FloatVectorProperty(
        name = "Offset:",
        description = "",
        default = (0, 0, 0),
        step = 1
    )
    
    # Check if user has selected exactly 2 objects
    @classmethod
    def poll(self, context):
        return len(context.selected_objects) == 2
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
       
    def execute(self, context):
        xoffset = self.axesOffset[0]
        yoffset = self.axesOffset[1]
        zoffset = self.axesOffset[2]
        
        i = 0
        objOne = context.active_object
        objTwo = getSecondObject()
        
        if(isSelectedValid(objOne, objTwo)):
                dispOne = setOriginToCenter(objOne)
                dispTwo = setOriginToCenter(objTwo)
                alignMesh({
                    "xoffset":xoffset, 
                    "yoffset":yoffset, 
                    "zoffset":zoffset, 
                    "snapAxis":self.axesEnum 
                }, objOne, objTwo)
                
                restoreOrigin(objOne, dispOne)
                restoreOrigin(objTwo, dispTwo)
        else:
                self.report({"WARNING"}, "Only aligned objects that are of type mesh.")
            
        return {"FINISHED"}

# Activate operator for use in blender
def register():
    bpy.utils.register_class(SnapToObject)
    
# Disable operator from blender
def unregister():
    bpy.utils.unregister_class(SnapToObject)

# Call register when script is run for testing
if __name__ == "__main__":
    register()
    