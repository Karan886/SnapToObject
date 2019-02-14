# Snap To Object Add-On
This project is a small tool made for a 3D art and animation suite called "Blender". Imagine a scenario where you are an artist working on multiple 3D models that need to be organized along the x, y, or z axis in the final scene. ie. designing a small city block may require organizing 3 or 4 building models along the x axis. This tool eases an artist's job by "snapping" selected meshes together - that is, properly stacking them along the specified axis. Currently, this tool works for every two selected meshes(so you cannot stack more than two meshes at a time). The last selected mesh will maintain its location in 3D space, while the first selected mesh will be pulled towards it. Additionally, this tool allows some room for flexibility by allowing artists to add offset values. For example, when each building in the city block have some space between them, you can stack them with some offset between them.

First look at the tool: 
<video src="https://user-images.githubusercontent.com/8737063/52754260-bb9db280-2fae-11e9-85ae-666bbd135b84.gif" width="320" height="200"></video>

Main issues:

1. To implement this tool to work on more than two meshes at a time, we need to know the order in which the artist selected 
those meshes in the first place. This information is not available with the blender python API - (looking into implementing a 
sub-tool for this, if possible).
