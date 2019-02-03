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

def setCursorToFloor(obj):
    # Begin by setting cursor to center of mass
    obj.select = True
    bpy.ops.object.origin_set(type = "ORIGIN_CENTER_OF_MASS")
    
    # Calculate where the floor of the mesh is located and set the 3d cursor to that location
    offset = mathutils.Vector((0, 0, obj.dimensions.z/2))
    objFloor = obj.location - offset
    context.scene.cursor_location = objFloor
    
    # Set origin of the mesh to its floor
    bpy.ops.object.origin_set(type = "ORIGIN_CURSOR")
    obj.select = False

def alignMesh(options, objOne, objTwo):
    xoffset = options["xoffset"]
    yoffset = options["yoffset"]
    zoffset = options["zoffset"]
    snapAxis = options["snapAxis"]
    
    newLocationVector = [objOne.location.x + xoffset, objOne.location.y + yoffset, objOne.location.z + zoffset]
    if (snapAxis == "X"):
        newLocationVector[0] += objOne.dimensions[0]
    elif(snapAxis == "Y"):
        newLocationVector[1] += objOne.dimensions[1]
    elif(snapAxis == "Z"):
         newLocationVector[2] += objOne.dimensions[2]
         
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
                alignMesh({
                    "xoffset":xoffset, 
                    "yoffset":yoffset, 
                    "zoffset":zoffset, 
                    "snapAxis":self.axesEnum 
                }, objOne, objTwo)
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
    



    
    
    
    