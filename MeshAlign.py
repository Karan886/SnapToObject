import bpy
from bpy import context
from bpy import props

print("----------")

def isSelectedValid():
    for obj in context.selected_objects:
        if obj.type != "MESH":
            return 0
    return 1
    
def alignMesh(xoffset, yoffset, zoffset, snapAxis):
    objOne = context.selected_objects[0]
    objTwo = context.selected_objects[1]
    
    newLocationVector = [objTwo.location.x + xoffset, objTwo.location.y + yoffset, objTwo.location.z + zoffset]
    if (snapAxis == "X"):
        newLocationVector[0] += objTwo.scale.x * 2
    elif(snapAxis == "Y"):
        newLocationVector[1] += objTwo.scale.y * 2 
    elif(snapAxis == "Z"):
         newLocationVector[2] += objTwo.scale.z * 2
         
    objOne.location = newLocationVector

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
        if (isSelectedValid()):
            return context.window_manager.invoke_props_dialog(self, width = 400)
        else:
            self.report({"INFO"}, "All selected objects must be of type MESH")
            return {"CANCELLED"}
       
    def execute(self, context):
        xoffset = self.axesOffset[0]
        yoffset = self.axesOffset[1]
        zoffset = self.axesOffset[2]
        alignMesh(xoffset, yoffset, zoffset, self.axesEnum)
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
    



    
    
    
    