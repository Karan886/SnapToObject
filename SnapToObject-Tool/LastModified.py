import bpy
import EventHandler
from bpy import context

class LastModified:
    instance = None
    @staticmethod
    def getInstance():
        if (LastModified.instance == None):
            LastModified()
        return LastModified.instance
    def __init__(self):
        if (LastModified.instance != None):
             raise Exception("This class is a singleton")
        else:
            LastModified.instance = self






