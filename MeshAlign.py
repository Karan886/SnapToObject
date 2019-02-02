import bpy
from bpy import context

def getNewCoords(xoffset, yoffset, zoffset, snapAxis):
    objOne = context.selected_objects[0]
    objTwo = context.selected_objects[1]
    
    newLocationVector = [objTwo.location.x + xoffset, objTwo.location.y + yoffset, objTwo.location.z + zoffset]
    if (snapAxis == "X"):
        newLocationVector[0] += objTwo.scale.x
    elif(snapAxis == "Y"):
        newLocationVector[1] += bjTwo.scale.y 
    elif(snapAxis == "Z"):
         newLocationVector[2] += objTwo.scale.z

class SnapToObject(bpy.types.Operator):
    bl_idname = "view3d.snap_to_object"
    bl_label = "Snap To Object"
    
    # Check if user has selected exactly 2 objects
    @classmethod
    def poll(self, context):
        return len(context.selected_objects)
    def invoke(self, context, event):
        newLocationVector(0, 0, 0, "Z")
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
    



    
    
    
    