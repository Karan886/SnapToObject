import bpy
from bpy import context
from bpy import props

def getNewCoords(xoffset, yoffset, zoffset, snapAxis):
    objOne = context.selected_objects[0]
    objTwo = context.selected_objects[1]
    
    newLocationVector = [objTwo.location.x + xoffset, objTwo.location.y + yoffset, objTwo.location.z + zoffset]
    if (snapAxis == "X"):
        newLocationVector[0] += objTwo.scale.x * 2
    elif(snapAxis == "Y"):
        newLocationVector[1] += bjTwo.scale.y * 2 
    elif(snapAxis == "Z"):
         newLocationVector[2] += objTwo.scale.z * 2
         
    objOne.location = newLocationVector

def updateEnumValue(self, value):
    self.axesEnum = value
def getEnumValue(self):
    return self.axesEnum
def setEnumValue(self, value):
    self.axesEnum = value

class SnapToObject(bpy.types.Operator):
    bl_idname = "view3d.snap_to_object"
    bl_label = "Snap To Object"
    
    axesEnum = ""
    
    axesEnumProperty = props.EnumProperty(
        items = (("X", "x", ""), ("Y", "y", ""), ("Z", "z", "")),
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
        return context.window_manager.invoke_props_dialog(self, width = 400)
    def execute(self, context):
        print(self.axesEnumProperty)
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
    



    
    
    
    