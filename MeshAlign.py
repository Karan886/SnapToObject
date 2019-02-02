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



    
    
    
    