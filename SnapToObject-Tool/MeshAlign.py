#This AddOn helps align/organize a collection of scene meshes so that the artist 
#doesn't have to do all the work. Note: the way objects are positioned depends on where the origin is set.

import bpy
import mathutils
from bpy import context
from bpy import props

objOne = None
objTwo = None

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
    prevLoc = mathutils.Vector((obj.location.x, obj.location.y, obj.location.z))
    bpy.ops.object.origin_set(type = "ORIGIN_CENTER_OF_MASS")  
    displacement = prevLoc - obj.location
    obj.select = False
    return displacement

def restoreOrigin(obj, disp):
    obj.select = True
    context.scene.cursor_location = obj.location + disp
    bpy.ops.object.origin_set(type = "ORIGIN_CURSOR")
    obj.select = False 
    
def deselectAll():
    objects = context.selected_objects
    for obj in objects:
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
    elif(snapAxis == "-X"):
        newLocationVector[0] -= objOne.dimensions.x/2 + objTwo.dimensions.x/2
    elif(snapAxis == "-Y"):
        newLocationVector[1] -= objOne.dimensions.y/2 + objTwo.dimensions.y/2
    elif(snapAxis == "-Z"):
        newLocationVector[2] -= objOne.dimensions.z/2 + objTwo.dimensions.z/2
               
    objTwo.location = newLocationVector
    
def snapMeshToLocation(objOne, objTwo, offset, snapDirection):
    xoffset = offset["x"]
    yoffset = offset["y"]
    zoffset = offset["z"]
    
    if(isSelectedValid(objOne, objTwo)):
    # caching 3D cursor location so that it can be restored after snap operation is complete
        cursorLoc = context.scene.cursor_location
        cursorLoc = mathutils.Vector((cursorLoc.x, cursorLoc.y, cursorLoc.z))
        
     # Deselecting all selected objects so that we can manipulate origin and restore
        deselectAll()
                
        dispOne = setOriginToCenter(objOne)
        dispTwo = setOriginToCenter(objTwo)
                
        alignMesh({
            "xoffset":xoffset, 
            "yoffset":yoffset, 
            "zoffset":zoffset, 
            "snapAxis":snapDirection 
            }, 
            objOne, objTwo) 
                 
        restoreOrigin(objOne, dispOne)
        restoreOrigin(objTwo, dispTwo)
                
        # Restore 3D cursor location
        context.scene.cursor_location = cursorLoc
                
    else:
                self.report({"WARNING"}, "Only aligned objects that are of type mesh.")
            
def onOffsetUpdated(self, context):
    global objOne
    global objTwo
    
    objTwo.location = mathutils.Vector((
        objOne.location.x + self.axesOffset[0],
        objOne.location.y + self.axesOffset[1],
        objOne.location.z + self.axesOffset[2]
    ))

class SnapToObject(bpy.types.Operator):
    bl_idname = "view3d.snap_to_object"
    bl_label = "Snap To Object" 
    
    axesEnum = props.EnumProperty(
        items = (
        ("X", "x", "snap to x-axis"), 
        ("Y", "y", "snap to y-axis"), 
        ("Z", "z", "snap to z-axis"),
        ("-X", "-x", "snap to -x axis"),
        ("-Y", "-y", "snap to -y axis"),
        ("-Z", "-z", "snap to -z axis")
        ),
        name = "Snap Axis:", 
        default = "X"
    )
    
    axesOffset = props.FloatVectorProperty(
        name = "Offset:",
        description = "",
        default = (0, 0, 0),
        update = onOffsetUpdated,
        step = 1
    )
    
    # Check if user has selected exactly 2 objects
    @classmethod
    def poll(self, context):
        return len(context.selected_objects) == 2
    
    def invoke(self, context, event):
        global objOne
        global objTwo
        
        offset = {
            "x":self.axesOffset[0],
            "y":self.axesOffset[1],
            "z":self.axesOffset[2]
        }
        objOne = context.active_object
        objTwo = getSecondObject()
        snapMeshToLocation(objOne, objTwo, offset, self.axesEnum)

        return context.window_manager.invoke_props_dialog(self)
       
    def execute(self, context):
        global objOne
        global objTwo
        
        objOne = None
        objTwo = None
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

